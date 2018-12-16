#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np

def extract_pkt_lat(path, traffic_, vc, pkt_per_vc, pkt_lat):
    for root, dirs, fnames, in os.walk(path):
        for dir in dirs:
            if dir.lower() == traffic_:
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "vc-"+str(vc):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "pkt-per-vc-"+str(pkt_per_vc):
                                        path4 = os.path.join(root3, dir3)
                                        for root7, dirs7, fnames7 in os.walk(path4):
                                            for dir7 in dirs7:
                                                token = dir7.split('-')
                                                idx = float(token[1])
                                                index = int(idx * 50) - 1
                                                file = dir7 + "/stats.txt"
                                                filepath = os.path.join(root7, file)
                                                packet_latency = subprocess.check_output(
                                                    "grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
                                                        .format(filepath),
                                                    shell=True)
                                                try:
                                                    pkt_lat[index] += float(packet_latency)
                                                except ValueError:
                                                    pass




traffic_pattern = sys.argv[1]
if (traffic_pattern != "uniform_random" and
        traffic_pattern != "bit_complement" and
        traffic_pattern != "bit_reverse" and
        traffic_pattern != "bit_rotation" and
        traffic_pattern != "transpose" and
        traffic_pattern != "shuffle"):
    print("Unrecognized traffic-pattern: " + traffic_pattern)
    sys.exit()

vc_=sys.argv[2]

path = os.getcwd()
path = path + "/gem5_vc_deep_rslt/12-10-2018/64c/XY/"

pkt_lat_1 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 1, pkt_lat_1)

pkt_lat_2 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 2, pkt_lat_2)

pkt_lat_3 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 3, pkt_lat_3)

pkt_lat_4 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 4, pkt_lat_4)

pkt_lat_5 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 5, pkt_lat_5)

pkt_lat_6 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 6, pkt_lat_6)

pkt_lat_7 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 7, pkt_lat_7)

pkt_lat_8 = [0] * 25
extract_pkt_lat(path, traffic_pattern, vc_, 8, pkt_lat_8)
#################################### Printing out Stats #########################################
#1
for itr in pkt_lat_1:
    if itr != 0:
        print itr,
print ""
#2
for itr in pkt_lat_2:
    if itr != 0:
        print itr,
print ""
#3
for itr in pkt_lat_3:
    if itr != 0:
        print itr,
print ""
#4
for itr in pkt_lat_4:
    if itr != 0:
        print itr,
print ""
#5
for itr in pkt_lat_5:
    if itr != 0:
        print itr,
print ""
#6
for itr in pkt_lat_6:
    if itr != 0:
        print itr,
print ""
#7
for itr in pkt_lat_7:
    if itr != 0:
        print itr,
print ""
#8
for itr in pkt_lat_8:
    if itr != 0:
        print itr,