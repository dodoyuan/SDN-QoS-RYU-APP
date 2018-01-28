# Common Setting for Networ awareness module.
from collections import defaultdict

DISCOVERY_PERIOD = 15  # For discovering topology.

MONITOR_PERIOD = 3  # For monitoring traffic

DELAY_DETECTING_PERIOD = 2  # For detecting link delay.

TOSHOW = True  # For showing information in terminal

MAX_CAPACITY = 100  # Max capacity of link

path_number = 3

def get_link_capacity(dpid, port, return_matrix_flag):
    link_capacity = defaultdict(lambda: defaultdict(lambda: 10))
    # link_capacity[4][1] = 100
    # link_capacity[4][2] = 100
    # link_capacity[4][3] = 100
    # link_capacity[4][4] = 100
    # link_capacity[1][1] = 100
    # link_capacity[1][2] = 100
    # link_capacity[1][3] = 100
    # link_capacity[1][4] = 100
    if return_matrix_flag:
        return link_capacity
    else:
        return link_capacity[dpid][port]

k_paths = 2

WEIGHT = 'bw'

# predefined requirement band-with of each source IP
require_band = {"10.0.0.1": 2, "10.0.0.2": 2, "10.0.0.3": 2, "10.0.0.4": 2}

# predefined priority of each source IP
priority_weight = {"10.0.0.1": 16, "10.0.0.2": 8, "10.0.0.3": 4}
