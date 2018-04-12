import argparse
import ConfigParser
import json
import swagger_client
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.models.logical_router import LogicalRouter
from swagger_client.models.logical_router_port import LogicalRouterPort
from swagger_client.models.resource_reference import ResourceReference
from swagger_client.models.ip_subnet import IPSubnet
from swagger_client.models.logical_port import LogicalPort
from swagger_client.models.static_route import StaticRoute
from swagger_client.models.static_route_next_hop import StaticRouteNextHop
from swagger_client.models.switching_profile_type_id_entry import SwitchingProfileTypeIdEntry
from swagger_client.models.advertisement_config import AdvertisementConfig
from swagger_client.models.tag import Tag
from swagger_client.models.nat_rule import NatRule
from argparse import RawTextHelpFormatter
from libutils import check_for_parameters,find_edge_cluster,find_logical_router,find_logical_switch,parse_tags

def create_router(client, name, router_type, edge_cluster=None, t0=None, tag=None):

    if edge_cluster:
        edge_cluster_id, edge_cluster = find_edge_cluster(client, edge_cluster)
        router = LogicalRouter(display_name=name, router_type=router_type, edge_cluster_id=edge_cluster_id, high_availability_mode='ACTIVE_STANDBY')
    else:
        router = LogicalRouter(display_name=name, router_type=router_type, high_availability_mode='ACTIVE_STANDBY')

    if router_type == 'TIER0':
        router.tags = parse_tags(tag)

    api_instance = swagger_client.LogicalRoutingAndServicesApi(client)
    result = api_instance.create_logical_router(router)

    if router_type == 'TIER1':
        lrp_t0 = create_router_port(client, 'LinkedPort_' + name, 'linkt0', t0)
        lrp_t1 = create_router_port(client, 'LinkedPort_' + t0, 'linkt1', name, logical_router_port_id=lrp_t0.id)
        advertisement_config = api_instance.read_advertisement_config(logical_router_id=result.id)
        advertisement_config.advertise_nsx_connected_routes = True
        advertisement_config.enabled = True
        api_instance.update_advertisement_config(result.id, advertisement_config)

    return result

def _create_router(client, **kwargs):
    needed_params = ['router_type', 'name']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_router(client, kwargs['name'], kwargs['router_type'], kwargs['edge_cluster'], kwargs['t0'], kwargs['tag'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print '{} router {} created'.format(kwargs['router_type'], kwargs['name'])
    else:
        print 'Creation of {} router {} failed'.format(kwargs['router_type'], kwargs['name'])

def create_router_port(client, name, router_port_type, logical_router, logical_switch=None, ip_address=None, mask=None, logical_router_port_id=None):

    logical_router_id, logical_router = find_logical_router(client, logical_router)

    lrp = LogicalRouterPort(resource_type='LogicalRouterUpLinkPort', display_name=name, logical_router_id=logical_router_id).to_dict()

    if router_port_type == 'uplink':
        lrp['resource_type'] = 'LogicalRouterUpLinkPort'
        lrp['edge_cluster_member_index'] = [0]
    elif router_port_type == 'downlink':
        lrp['resource_type'] = 'LogicalRouterDownLinkPort'
    elif router_port_type == 'linkt1':
        lrp['resource_type'] = 'LogicalRouterLinkPortOnTIER1'
        lrp['edge_cluster_member_index'] = [0]
    elif router_port_type == 'linkt0':
        lrp['resource_type'] = 'LogicalRouterLinkPortOnTIER0'

    if ip_address and mask:
        lrp['subnets'] = [IPSubnet(ip_addresses=[ip_address], prefix_length=int(mask))]

    if logical_switch:
        logical_switch_id, logical_switch_params = find_logical_switch(client, logical_switch)
        switching_api = swagger_client.LogicalSwitchingApi(client)
        profiles = _switching_profiles()
        switch_port = switching_api.create_logical_port(LogicalPort(admin_state="UP", logical_switch_id=logical_switch_id, switching_profile_ids=profiles))
        lrp['linked_logical_switch_port_id'] = ResourceReference(target_id=switch_port.id)

    if logical_router_port_id:
        lrp['linked_logical_router_port_id'] = ResourceReference(target_id=logical_router_port_id)

    res = dict((k,v) for k,v in lrp.iteritems() if v is not None)

    api_instance = swagger_client.LogicalRoutingAndServicesApi(client)
    return api_instance.create_logical_router_port(res)

def _create_router_port(client, **kwargs):
    needed_params = ['router_port_type', 'name', 'logical_router']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_router_port(client, kwargs['name'], kwargs['router_port_type'], kwargs['logical_router'], kwargs['logical_switch'], kwargs['ip_address'], kwargs['mask'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'Router port {} of type {} created on router {}'.format(kwargs['name'], kwargs['router_port_type'], kwargs['logical_router'])
    else:
        print 'Creation of router port {} of type {} on router {} failed'.format(kwargs['name'], kwargs['router_port_type'], kwargs['logical_router'])

def create_static_route(client, logical_router, network, next_hop):

    logical_router_id, logical_router = find_logical_router(client, logical_router)

    static_route = StaticRoute(network=network, next_hops=[StaticRouteNextHop(administrative_distance=1, ip_address=next_hop)])

    api_instance = swagger_client.LogicalRoutingAndServicesApi(client)
    return api_instance.add_static_route(logical_router_id=logical_router_id, static_route=static_route)

def _create_static_route(client, **kwargs):
    needed_params = ['logical_router', 'network', 'next_hop']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_static_route(client, kwargs['logical_router'], kwargs['network'], kwargs['next_hop'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'Static route created on {} from {} to {}'.format(kwargs['logical_router'], kwargs['network'], kwargs['next_hop'])
    else:
        print 'Creation of static route on {} from {} to {} failed'.format(kwargs['logical_router'], kwargs['network'], kwargs['next_hop'])

def create_nat_rule(client, action, logical_router, original_ip, translated_ip):

    logical_router_id, logical_router = find_logical_router(client, logical_router)

    if action == 'SNAT':
        nat_rule = NatRule(action=action, enabled=True, rule_priority=1024, match_source_network=original_ip, translated_network=translated_ip)
    else:
        nat_rule = NatRule(action=action, enabled=True, rule_priority=1024, match_destination_network=original_ip, translated_network=translated_ip)

    api_instance = swagger_client.LogicalRoutingAndServicesApi(client)
    return api_instance.add_nat_rule(logical_router_id=logical_router_id, nat_rule=nat_rule)

def _create_nat_rule(client, **kwargs):
    needed_params = ['action', 'logical_router', 'original_ip', 'translated_ip']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_nat_rule(client, kwargs['action'], kwargs['logical_router'], kwargs['original_ip'], kwargs['translated_ip'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print '{} rule created on {} for {} -> {}'.format(kwargs['action'], kwargs['logical_router'], kwargs['original_ip'], kwargs['translated_ip'])
    else:
        print 'Creation of {} rule on {} for {} -> {} failed'.format(kwargs['action'], kwargs['logical_router'], kwargs['original_ip'], kwargs['translated_ip'])

def _switching_profiles():
    profiles = []
    profiles.append(SwitchingProfileTypeIdEntry(key='SwitchSecuritySwitchingProfile', value='fbc4fb17-83d9-4b53-a286-ccdf04301888'))
    profiles.append(SwitchingProfileTypeIdEntry(key='SpoofGuardSwitchingProfile', value='fad98876-d7ff-11e4-b9d6-1681e6b88ec1'))
    profiles.append(SwitchingProfileTypeIdEntry(key='IpDiscoverySwitchingProfile', value='0c403bc9-7773-4680-a5cc-847ed0f9f52e'))
    profiles.append(SwitchingProfileTypeIdEntry(key='MacManagementSwitchingProfile', value='1e7101c8-cfef-415a-9c8c-ce3d8dd078fb'))
    profiles.append(SwitchingProfileTypeIdEntry(key='PortMirroringSwitchingProfile', value='93b4b7e8-f116-415d-a50c-3364611b5d09'))
    profiles.append(SwitchingProfileTypeIdEntry(key='QosSwitchingProfile', value='f313290b-eba8-4262-bd93-fab5026e9495'))
    return profiles


def construct_parser(subparsers):
    parser = subparsers.add_parser('routing', description="Functions for logical switches",
                                   help="Functions for logical switches",
                                   formatter_class=RawTextHelpFormatter)

    parser.add_argument("command", help="""
    create_router: create a new logical switch
    create_router_port: create a new router port on an existing router
    create_static_route: creates a new static route
    create_nat_rule: create a NAT rule on a given router
    """)

    parser.add_argument("-t",
                        "--router_type",
                        help="Type of router, TIER0 or TIER1")
    parser.add_argument("-n",
                        "--name",
                        help="display name for created routing component")
    parser.add_argument("-ec",
                        "--edge_cluster",
                        help="Name of the edge cluster to attach to")
    parser.add_argument("-rpt",
                        "--router_port_type",
                        help="The type of router port to create. (uplink, downlink, loopback)")
    parser.add_argument("-ls",
                        "--logical_switch",
                        help="Name of the logical switch to attach to")
    parser.add_argument("-lr",
                        "--logical_router",
                        help="Name of the logical router to create router port on")
    parser.add_argument("-ip",
                        "--ip_address",
                        help="IP Address of the router port")
    parser.add_argument("-mask",
                        "--mask",
                        help="Mask of the IP address for the router port")
    parser.add_argument("-network",
                        "--network",
                        help="Network for a static route")
    parser.add_argument("-next_hop",
                        "--next_hop",
                        help="Next hop of a static route")
    parser.add_argument("-oip",
                        "--original_ip",
                        help="Original IP for NAT entry (source IP for SNAT, destination IP for DNAT)")
    parser.add_argument("-tip",
                        "--translated_ip",
                        help="Translated IP for NAT Rule")
    parser.add_argument("-a",
                        "--action",
                        help="NAT Action (SNAT or DNAT)")
    parser.add_argument("-t0",
                        "--t0",
                        help="Tier-0 Router to connect Tier-1 router to during creation")
    parser.add_argument("-tag",
                        "--tag",
                        help="Tag to be added to the T0 Router in the form 'key=value'",
                        action="append")

    parser.set_defaults(func=_routing_main)


def _routing_main(args):
    if args.debug:
        debug = True
    else:
        debug = False

    config = ConfigParser.ConfigParser()
    assert config.read(args.ini), 'could not read config file {}'.format(args.ini)

    configuration = Configuration()
    configuration.host = config.get('nsxv', 'nsx_manager')
    configuration.username = config.get('nsxv', 'nsx_username')
    configuration.password = config.get('nsxv', 'nsx_password')
    configuration.verify_ssl = False
    client = ApiClient(configuration)

    try:
        command_selector = {
            'create_router': _create_router,
            'create_router_port': _create_router_port,
            'create_static_route': _create_static_route,
            'create_nat_rule': _create_nat_rule
            }
        command_selector[args.command](client, router_type=args.router_type,
                                       name=args.name, edge_cluster=args.edge_cluster,
                                       router_port_type=args.router_port_type, logical_switch=args.logical_switch,
                                       logical_router=args.logical_router, ip_address=args.ip_address,
                                       mask=args.mask, network=args.network,
                                       next_hop=args.next_hop, original_ip=args.original_ip,
                                       translated_ip=args.translated_ip, action=args.action,
                                       t0=args.t0, tag=args.tag,
                                       verbose=args.verbose)
    except KeyError:
        print('Unknown command')


def main():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    construct_parser(subparsers)
    args = main_parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
