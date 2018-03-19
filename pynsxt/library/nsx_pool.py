import argparse
import ConfigParser
import json
import swagger_client
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.models.ip_block import IpBlock
from swagger_client.models.ip_pool import IpPool
from swagger_client.models.ip_pool_subnet import IpPoolSubnet
from swagger_client.models.ip_pool_range import IpPoolRange
from swagger_client.models.tag import Tag
from argparse import RawTextHelpFormatter
from libutils import check_for_parameters,find_transport_zone

def create_ip_block(client, name, cidr, foundation):

    ip_block = IpBlock(display_name=name, cidr=cidr, tags=[Tag(scope='ncp/cluster', tag=foundation)])

    api_instance = swagger_client.PoolManagementApi(client)
    return api_instance.create_ip_block(ip_block)

def _create_ip_block(client, **kwargs):
    needed_params = ['name', 'cidr', 'foundation']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_ip_block(client, kwargs['name'], kwargs['cidr'], kwargs['foundation'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'IP Block {} created with CIDR {}'.format(kwargs['name'], kwargs['cidr'])
    else:
        print 'Creation of IP Block {} failed for CIDR {}'.format(kwargs['name'], kwargs['cidr'])

def create_ip_pool(client, name, cidr, foundation, start, end):

    ip_pool = IpPool(display_name=name, tags=[Tag(scope='ncp/cluster', tag=foundation), Tag(scope='ncp/external', tag='true')], subnets=[IpPoolSubnet(cidr=cidr, allocation_ranges=[IpPoolRange(start=start, end=end)])])

    api_instance = swagger_client.PoolManagementApi(client)
    return api_instance.create_ip_pool(ip_pool)

def _create_ip_pool(client, **kwargs):
    needed_params = ['name', 'cidr', 'foundation', 'start', 'end']
    if not check_for_parameters(needed_params, kwargs):
        return None

    result = create_ip_pool(client, kwargs['name'], kwargs['cidr'], kwargs['foundation'], kwargs['start'], kwargs['end'])

    if result and kwargs['verbose']:
        print result
    elif result:
        print 'IP Pool {} created with CIDR {}'.format(kwargs['name'], kwargs['cidr'])
    else:
        print 'Creation of IP Pool {} failed for CIDR {}'.format(kwargs['name'], kwargs['cidr'])



def construct_parser(subparsers):
    parser = subparsers.add_parser('pool', description="Functions for ip pools",
                                   help="Functions for ip pools",
                                   formatter_class=RawTextHelpFormatter)

    parser.add_argument("command", help="""
    create_ip_block: create a new ip block
    create_ip_pool: create a new ip pool
    """)

    parser.add_argument("-c",
                        "--cidr",
                        help="CIDR for the ip block")
    parser.add_argument("-n",
                        "--name",
                        help="display name of the ip block")
    parser.add_argument("-s",
                        "--start",
                        help="Starting IP address for a range")
    parser.add_argument("-e",
                        "--end",
                        help="Ending IP address for a range")

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
    args.foundation = config.get('pcf', 'pcf_foundation')
    client = ApiClient(configuration)

    try:
        command_selector = {
            'create_ip_block': _create_ip_block,
            'create_ip_pool': _create_ip_pool,
            }
        command_selector[args.command](client, cidr=args.cidr,
                                       name=args.name, foundation=args.foundation,
                                       start=args.start, end=args.end,
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
