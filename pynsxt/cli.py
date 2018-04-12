#!/usr/bin/env python
# coding=utf-8
#
__author__ = 'tcraft'

import argparse
import library.nsx_switching as switching
import library.nsx_routing as routing
import library.nsx_pool as pool
import library.nsx_setup as setup
import urllib3

def main():
    urllib3.disable_warnings()

    parser = argparse.ArgumentParser(description='PyNSXv Command Line Client for NSX for vSphere')
    parser.add_argument("-i",
                        "--ini",
                        help="nsx configuration file",
                        default="nsx.ini")
    parser.add_argument("-v",
                        "--verbose",
                        help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-d",
                        "--debug",
                        help="print low level debug of http transactions",
                        action="store_true")

    subparsers = parser.add_subparsers()
    switching.construct_parser(subparsers)
    routing.construct_parser(subparsers)
    pool.construct_parser(subparsers)
    setup.construct_parser(subparsers)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
