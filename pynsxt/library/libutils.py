import swagger_client
from swagger_client.models.tag import Tag

def check_for_parameters(mandatory, args):
    param = None
    try:
        for param in mandatory:
            if not args[param]:
                print'You are missing the mandatory parameter: {}'.format(param)
                return None
    except KeyError:
        print 'You are missing the mandatory parameter: {}'.format(param)
        return None

    return True


def find_transport_zone(client, name):
    api_instance = swagger_client.NetworkTransportApi(client)
    zones = api_instance.list_transport_zones()._results

    for zone in zones:
        if zone._display_name == name:
            return zone._id, zone
    return None, None

def find_edge_cluster(client, name):
    api_instance = swagger_client.NetworkTransportApi(client)
    clusters = api_instance.list_edge_clusters()._results

    for cluster in clusters:
        if cluster._display_name == name:
            return cluster._id, cluster
    return None, None

def find_logical_router(client, name):
    api_instance = swagger_client.LogicalRoutingAndServicesApi(client)
    routers = api_instance.list_logical_routers()._results

    for router in routers:
        if router._display_name == name:
            return router._id, router
    return None, None

def find_logical_switch(client, name):
    api_instance = swagger_client.LogicalSwitchingApi(client)
    switches = api_instance.list_logical_switches()._results

    for switch in switches:
        if switch._display_name == name:
            return switch._id, switch
    return None, None

def find_all_nat_rules(client, logical_router_id):
    api_instance = swagger_client.LogicalRoutingAndServicesApi(client)
    nat_rules = api_instance.list_nat_rules(logical_router_id)
    return nat_rules.results

def parse_tags(tag):
    tags = []
    if tag:
        if isinstance(tag, list):
            for t in tag:
                tags.append(Tag(scope=t.split('=')[0], tag=t.split('=')[1]))
        elif isinstance(tag, str):
            tags.append(Tag(scope=tag.split('=')[0], tag=tag.split('=')[1]))
    return tags
