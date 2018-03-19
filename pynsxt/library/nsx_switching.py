import argparse
import ConfigParser
import json
import swagger_client
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.models.logical_switch import LogicalSwitch
from argparse import RawTextHelpFormatter
from libutils import check_for_parameters,find_transport_zone

def create_switch(client, name, transport_zone, vlan=None):

    transport_zone_id, tz = find_transport_zone(client, transport_zone)
    if not vlan:
        switch = LogicalSwitch(admin_state="UP", transport_zone_id=transport_zone_id, display_name=name, replication_mode="MTEP")
    else:
        switch = LogicalSwitch(admin_state="UP", transport_zone_id=transport_zone_id, display_name=name, vlan=vlan)
    api_instance = swagger_client.LogicalSwitchingApi(client)
    return api_instance.create_logical_switch(switch)

def _create_switch(client, **kwargs):
    needed_params = ['transport_zone', 'name']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_switch(client, kwargs['name'], kwargs['transport_zone'], kwargs['vlan'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'Switch {} created in Transport Zone {}'.format(kwargs['name'], kwargs['transport_zone'])
    else:
        print 'Creation of switch {} failed in Transport Zone {}'.format(kwargs['name'], kwargs['transport_zone'])


def construct_parser(subparsers):
    parser = subparsers.add_parser('switch', description="Functions for logical switches",
                                   help="Functions for logical switches",
                                   formatter_class=RawTextHelpFormatter)

    parser.add_argument("command", help="""
    create: create a new logical switch
    """)

    parser.add_argument("-t",
                        "--transport_zone",
                        help="nsx transport zone")
    parser.add_argument("-n",
                        "--name",
                        help="logical switch name, needed for create, read and delete")
    parser.add_argument("-vlan",
                        "--vlan",
                        help="VLAN number to use. Only needed if connecting this switch to a VLAN Transport Zone")

    parser.set_defaults(func=_switching_main)


def _switching_main(args):
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
            'create': _create_switch,
            }
        command_selector[args.command](client, transport_zone=args.transport_zone,
                                       name=args.name, vlan=args.vlan, verbose=args.verbose)
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
