#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
import plot_thrpt

def extract_pkt_received(path, traffic_, pkt_rvd, pkt_lat, vc, inj):
    path = path + "sim-type-1/"
    for root, dirs, fnames, in os.walk(path):
        for dir in dirs:
            if dir.lower() == traffic_:
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "vc-" + str(vc):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "pkt-per-vc-1":
                                        path4 = os.path.join(root3, dir3)
                                        for root5, dirs5, fnames5 in os.walk(path4):
                                            for dir5 in dirs5:
                                                token = dir5.split('-')
                                                idx = float(token[1])
                                                # print idx
                                                inj.append(idx)
                                                # important
                                                index = int(np.round(idx * 50.0 - 1.0))
                                                # print index
                                                file = dir5 + "/stats.txt"
                                                filepath = os.path.join(root5, file)
                                                packet_rvd = subprocess.check_output(
                                                    "grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
                                                        .format(filepath),
                                                    shell=True)
                                                pkt_lat_ = subprocess.check_output(
                                                    "grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
                                                        .format(filepath),
                                                    shell=True)
                                                try:
                                                    pkt_rvd[index] = int(packet_rvd)
                                                    pkt_lat[index] = float(pkt_lat_)
                                                except ValueError:
                                                    pass

def extract_sim_tick(path, traffic_, sim_ticks, pkt_lat, vc):
    path = path + "sim-type-2/"
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == traffic_:
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "vc-" + str(vc):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "pkt-per-vc-1":
                                        path4 = os.path.join(root3, dir3)
                                        for root5, dirs5, fnames5 in os.walk(path4):
                                            for dir5 in dirs5:
                                                token = dir5.split('-')
                                                idx = float(token[1])
                                                # important
                                                index = int(np.round(idx * 50.0 - 1.0))
                                                file = dir5 + "/stats.txt"
                                                filepath = os.path.join(root5, file)
                                                ticks = subprocess.check_output(
                                                    "grep -nri sim_ticks {0:s} | sed 's/.*sim_ticks\s*//' | sed 's/#.*\s*//'"
                                                        .format(filepath),
                                                    shell=True)
                                                pkt_lat_ = subprocess.check_output(
                                                    "grep -nri average_marked_pkt_latency {0:s} | sed 's/.*system.ruby.network.average_marked_pkt_latency\s*//'"
                                                        .format(filepath),
                                                    shell=True)
                                                try:
                                                    sim_ticks[index] += int(ticks)
                                                    pkt_lat[index] += float(pkt_lat_)
                                                except ValueError:
                                                    pass
# sim_type = int(sys.argv[1])
traffic_pattern = sys.argv[1]
if (traffic_pattern != "uniform_random" and
        traffic_pattern != "bit_complement" and
        traffic_pattern != "bit_reverse" and
        traffic_pattern != "bit_rotation" and
        traffic_pattern != "transpose" and
        traffic_pattern != "shuffle"):
    print("Unrecognized traffic-pattern: " + traffic_pattern)
    sys.exit()

vc_ = int(sys.argv[2])

path = os.getcwd()
path = path + "/gem5_vc_deep_rslt/12-20-2018/64c/XY/"

injr=np.linspace(0.02,0.98,49)

pkt_received = [0] * 50
sim_cycles = [0] * 50
pkt_lat_1 = [0] * 50
pkt_lat_2 = [0] * 50
thrpt_1 = []
thrpt_2 = []
inj_ = []

extract_pkt_received(path, traffic_pattern, pkt_received, pkt_lat_1, vc_, inj_)
for itr in pkt_received:
    if itr != 0:
        thrpt_1.append(float(itr) / (64 * 100000))

# z = zip(inj_, thrpt_1)
#
# for itr in z:
#     print itr

print np.count_nonzero(pkt_received)

extract_sim_tick(path, traffic_pattern, sim_cycles, pkt_lat_2, vc_)
for itr in sim_cycles:
    if itr != 0:
        thrpt_2.append(float(100000) / (64 * (itr - 1000)))

# for thr_ in thrpt_1:
#     print thr_,
#
# print" "
#
# for thr_ in thrpt_2:
#     print thr_,
#
# print" "

plot_thrpt.plot2_line_graph(injr, thrpt_1, thrpt_2, vc_, traffic_pattern)

# for itr in sim_cycles:
#     if itr != 0:
#         print itr,
# print np.count_nonzero(thrpt_1)
# for itr in pkt_lat_1:
#     if itr != 0:
#         print itr,
#
# print" "
#
# for itr in pkt_lat_2:
#     if itr != 0:
#         print itr,