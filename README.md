# PyNSXT
This is a Python library that can be used as a CLI to run commands against a VMWare NSX-T installation. It exposes operations for working with logical switches, logical routers, and pools. It uses version 2.1 of NSX-T for the swagger client.

## Pre-Requisites
To use the library, you will need to have `setuptools` installed via `pip` to compile the swagger client.

```
pip install --upgrade setuptools
python pynsxt/setup.py install --user
```

## Usage

### INI File
For variables that get re-used on multiple calls, this library utilizes an `.ini` file to prevent the need to add these parameters to every CLI command.

```
[nsxv]
nsx_manager =
nsx_username =
nsx_password =

[pcf]
pcf_foundation =
```

### General Usage
```
usage: cli.py [-h] [-i INI] [-v] [-d] {switch,routing,pool} ...

PyNSXv Command Line Client for NSX for vSphere

positional arguments:
  {switch,routing,pool}
    switch              Functions for logical switches
    routing             Functions for logical switches
    pool                Functions for ip pools

optional arguments:
  -h, --help            show this help message and exit
  -i INI, --ini INI     nsx configuration file
  -v, --verbose         increase output verbosity
  -d, --debug           print low level debug of http transactions
```

### Logical Switches
```
usage: cli.py switch [-h] [-t TRANSPORT_ZONE] [-n NAME] [-vlan VLAN] command

Functions for logical switches

positional arguments:
  command               
        create: create a new logical switch

optional arguments:
  -h, --help            show this help message and exit
  -t TRANSPORT_ZONE, --transport_zone TRANSPORT_ZONE
                        nsx transport zone
  -n NAME, --name NAME  logical switch name, needed for create, read and delete
  -vlan VLAN, --vlan VLAN
                        number of VLAN to use. Only needed if connecting this switch to a VLAN Transport Zone
```

### Logical Routers
```
usage: cli.py routing [-h] [-t ROUTER_TYPE] [-n NAME] [-ec EDGE_CLUSTER]
                      [-rpt ROUTER_PORT_TYPE] [-ls LOGICAL_SWITCH]
                      [-lr LOGICAL_ROUTER] [-ip IP_ADDRESS] [-mask MASK]
                      [-network NETWORK] [-next_hop NEXT_HOP]
                      [-oip ORIGINAL_IP] [-tip TRANSLATED_IP] [-a ACTION]
                      [-t0 T0]
                      command

Functions for logical switches

positional arguments:
  command               
        create_router: create a new logical switch
        create_router_port: create a new router port on an existing router
        create_static_route: creates a new static route
        create_nat_rule: create a NAT rule on a given router


optional arguments:
  -h, --help            show this help message and exit
  -t ROUTER_TYPE, --router_type ROUTER_TYPE
                        Type of router, TIER0 or TIER1
  -n NAME, --name NAME  display name for created routing component
  -ec EDGE_CLUSTER, --edge_cluster EDGE_CLUSTER
                        Name of the edge cluster to attach to
  -rpt ROUTER_PORT_TYPE, --router_port_type ROUTER_PORT_TYPE
                        The type of router port to create. (uplink, downlink, loopback)
  -ls LOGICAL_SWITCH, --logical_switch LOGICAL_SWITCH
                        Name of the logical switch to attach to
  -lr LOGICAL_ROUTER, --logical_router LOGICAL_ROUTER
                        Name of the logical router to create router port on
  -ip IP_ADDRESS, --ip_address IP_ADDRESS
                        IP Address of the router port
  -mask MASK, --mask MASK
                        Mask of the IP address for the router port
  -network NETWORK, --network NETWORK
                        Network for a static route
  -next_hop NEXT_HOP, --next_hop NEXT_HOP
                        Next hop of a static route
  -oip ORIGINAL_IP, --original_ip ORIGINAL_IP
                        Original IP for NAT entry (source IP for SNAT, destination IP for DNAT)
  -tip TRANSLATED_IP, --translated_ip TRANSLATED_IP
                        Translated IP for NAT Rule
  -a ACTION, --action ACTION
                        NAT Action (SNAT or DNAT)
  -t0 T0, --t0 T0       Tier-0 Router to connect Tier-1 router to during creation
```

### Pools
```
usage: cli.py pool [-h] [-c CIDR] [-n NAME] [-s START] [-e END] command

Functions for ip pools

positional arguments:
  command               
        create_ip_block: create a new ip block
        create_ip_pool: create a new ip pool


optional arguments:
  -h, --help            show this help message and exit
  -c CIDR, --cidr CIDR  CIDR for the ip block
  -n NAME, --name NAME  display name of the ip block
  -s START, --start START
                        Starting IP address for a range
  -e END, --end END     Ending IP address for a range
```
