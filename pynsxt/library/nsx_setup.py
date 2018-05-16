import argparse
import ConfigParser
import json
import swagger_client
import sys
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from argparse import RawTextHelpFormatter
from libutils import find_logical_switch,find_logical_router,find_all_nat_rules

def _validate(client, **kwargs):

    error = False
    #validate switches
    switch_names = ["vlan-uplink", "infrastructure-ls", "deployment-ls", "services-ls", "dynamic-services-ls"]
    for switch in switch_names:
        logical_switch_id, logical_switch_params = find_logical_switch(client, switch)
        if not logical_switch_id:
            print 'Logical Switch {} is missing'.format(switch)
            error = True

    #validate routers
    router_names = ["router-t0", "infrastructure-t1", "deployment-t1", "services-t1", "dynamic-services-t1"]
    for router in router_names:
        logical_router_id, logical_router_params = find_logical_router(client, router)
        if not logical_router_id:
            print 'Logical Router {} is missing'.format(router)
            error = True

        if logical_router_params.router_type == 'TIER0':
            error |= _validate_nats(client, logical_router_id)
            #validate router port -> vlan-uplink
            #validate Static route

    #validate IP Block
    #validate IP Pool

    if error:
        sys.exit(1)

def _validate_nats(client, logical_router_id):
    nat_rules = find_all_nat_rules(client, logical_router_id)
    snats = ['192.168.1.0/24','192.168.2.0/24','192.168.3.0/24','192.168.4.0/24']
    for snat in snats:
        ok = False
        for rule in nat_rules:
            if rule.action == 'SNAT' and rule.match_source_network == snat:
                ok = True
                break

        if ok == False:
            print 'SNAT rule for {} is missing'.format(snat)
            error = True

    dnats = ['192.168.1.10']
    for dnat in dnats:
        ok = False
        for rule in nat_rules:
            if rule.action == 'DNAT' and rule.translated_network == dnat:
                ok = True
                break

        if not ok:
            print 'DNAT rule for {} is missing'.format(dnat)
            error = True
    return error

def construct_parser(subparsers):
    parser = subparsers.add_parser('setup', description="Functions for the overall setup of NSXT",
                                   help="Functions for the overall setup of NSXT",
                                   formatter_class=RawTextHelpFormatter)

    parser.add_argument("command", help="""
    validate: create a new ip block
    """)

    parser.add_argument("-c",
                        "--cidr",
                        help="CIDR for the ip block")

    parser.set_defaults(func=_setup_main)


def _setup_main(args):
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
            'validate': _validate,
            }
        command_selector[args.command](client, verbose=args.verbose)
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
