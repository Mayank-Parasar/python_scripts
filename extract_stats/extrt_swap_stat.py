#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
import plot_thrpt
import math
# import try_stackedBarPlot
from shlex import split


def extract_swap_pkt_latency(path, traffic_pattern, swap_, vc_, whenToSwap,
                             avg_pkt_latency, stat_type="none"):
    path = path + "/swapChannel_micro2019_rslt/03-23-2019/64c/"
    # print path
    # for root, dirs, fnames in os.walk(path):
    dirs = os.listdir(path)
    print dirs
    for dir in dirs:
        if dir.endswith(str(swap_)):
            path2 = os.path.join(path, dir)
            for root2, dirs2, fnames2 in os.walk(path2):
                for dir2 in dirs2:
                    if dir2.lower() == traffic_pattern:
                        path3 = os.path.join(root2, dir2)
                        for root3, dirs3, fnames3 in os.walk(path3):
                            for dir3 in dirs3:
                                if dir3 == "whenToSwap-"+str(whenToSwap):
                                    path4 = os.path.join(root3, dir3)
                                    for root4, dirs4, fnames4 in os.walk(path4):
                                        for dir4 in dirs4:
                                            if dir4.lower() == "vc-"+str(vc_):
                                                path5 = os.path.join(root4, dir4)
                                                for root5, dirs5, fnames5 in os.walk(path5):
                                                    for dir5 in dirs5:
                                                        file_path = path5 + "/" + dir5 + "/stats.txt"
                                                        # print file_path
                                                        ijr_ = dir5.split('-')
                                                        idx = float(ijr_[1])
                                                        index = int(np.round(idx * 50.0 - 1.0))
                                                        with open(file_path, "r") as file:
                                                            for line in file:
                                                                line = line.rstrip()
                                                                if stat_type.lower() == "pkt_lat":
                                                                    if "system.ruby.network.average_packet_latency " \
                                                                            in line:
                                                                        lineOut = line.split()
                                                                        avg_pkt_lat = float(lineOut[1])
                                                                        avg_pkt_latency[index] += float(avg_pkt_lat)
                                                                elif stat_type.lower() == "num_swaps":
                                                                    if "system.ruby.network.total_swaps " \
                                                                            in line:
                                                                        lineOut = line.split()
                                                                        avg_pkt_lat = float(lineOut[1])
                                                                        avg_pkt_latency[index] += float(avg_pkt_lat)


traffic_pattern = sys.argv[1]
if (traffic_pattern != "uniform_random" and
    traffic_pattern != "bit_complement" and
    traffic_pattern != "bit_reverse" and
    traffic_pattern != "bit_rotation" and
    traffic_pattern != "transpose" and
    traffic_pattern != "shuffle"):
    print("Unrecognized traffic-pattern: " + traffic_pattern)
    sys.exit()

swap_=str(sys.argv[2])
vc_ = int(sys.argv[3])
whenToSwap = int(sys.argv[4])


print os.getcwd()
path = os.getcwd()

# call to the function
disable_avg_pkt_latency = [0] * 25 # empty list
extract_swap_pkt_latency(path, traffic_pattern, "disable", vc_,
                         whenToSwap, disable_avg_pkt_latency, "pkt_lat")
print disable_avg_pkt_latency
    ##########
enable_avg_pkt_latency = [0] * 25 # empty list
extract_swap_pkt_latency(path, traffic_pattern, "enable", vc_,
                         whenToSwap, enable_avg_pkt_latency, "pkt_lat")
print enable_avg_pkt_latency

plot_thrpt.plot2_line_graph(np.trim_zeros(disable_avg_pkt_latency), "disable-Swap",
                            np.trim_zeros(enable_avg_pkt_latency), "enable-Swap",
                            whenToSwap, vc_, traffic_pattern)