#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
# import plot_thrpt


def extract_sim_ticks(path, traffic_, num_fault, sim_ticks, pkt_lat, vc, cntr,
                      net_lat, que_lat, max_lat, max_net_lat, max_que_lat):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.endswith("_" + str(num_fault) + ".txt"):
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "vc-" + str(vc):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    token = dir3.split('-')
                                    idx = float(token[1])
                                    # important
                                    index = int(np.round(idx * 50.0 - 1.0))
                                    file = dir3 + "/stats.txt"
                                    filepath = os.path.join(root3, file)
                                    ticks = subprocess.check_output(
                                        "grep -nri sim_ticks {0:s} | sed 's/.*sim_ticks\s*//' | sed 's/#.*\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    # print ticks
                                    pkt_lat_ = subprocess.check_output(
                                        "grep -nri average_marked_pkt_latency {0:s} | sed 's/.*system.ruby.network.average_marked_pkt_latency\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    net_lat_ = subprocess.check_output(
                                        "grep -nri marked_flit_network_latency_histogram::mean {0:s} | sed 's/.*system.ruby.network.marked_flit_network_latency_histogram::mean\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    que_lat_ = subprocess.check_output(
                                        "grep -nri marked_flit_queueing_latency_histogram::mean {0:s} | sed 's/.*system.ruby.network.marked_flit_queueing_latency_histogram::mean\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    max_lat_ = subprocess.check_output(
                                        "grep -nri max_flit_latency {0:s} | sed 's/.*system.ruby.network.max_flit_latency\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    max_net_lat_ = subprocess.check_output(
                                        "grep -nri max_flit_network_latency {0:s} | sed 's/.*system.ruby.network.max_flit_network_latency\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    max_que_lat_ = subprocess.check_output(
                                        "grep -nri max_flit_queueing_latency {0:s} | sed 's/.*system.ruby.network.max_flit_queueing_latency\s*//'"
                                            .format(filepath),
                                        shell=True)
                                    # print
                                    try:
                                        sim_ticks[index] += int(ticks)
                                        pkt_lat[index] += float(pkt_lat_)
                                        net_lat[index] += float(net_lat_)
                                        que_lat[index] += float(que_lat_)
                                        max_lat[index] += float(max_lat_)
                                        max_net_lat[index] += float(max_net_lat_)
                                        max_que_lat[index] += float(max_que_lat_)
                                        cntr[index] += 1
                                        # if index reaches maximum then insert the
                                        # command to cplot here
                                    except ValueError:
                                        pass


num_fault = int(sys.argv[1])
traffic_pattern = sys.argv[2]
if (traffic_pattern != "uniform_random" and
        traffic_pattern != "bit_complement" and
        traffic_pattern != "bit_reverse" and
        traffic_pattern != "bit_rotation" and
        traffic_pattern != "transpose" and
        traffic_pattern != "shuffle"):
    print("Unrecognized traffic-pattern: " + traffic_pattern)
    sys.exit()

vc_ = int(sys.argv[3])

path = os.getcwd()
path = path + "/irregular_up_dn/01-24-2019/64c/"

injr = np.linspace(0.02, 0.24, 12)

# pkt_received = [0] * 12
cntr_ = [0] * 15
sim_cycles = [0] * 15
pkt_lat = [0] * 15
net_lat = [0] * 15
que_lat = [0] * 15
max_lat = [0] * 15
max_net_lat = [0] * 15
max_que_lat = [0] * 15

# pkt_lat_2 = [0] * 50
avg_thrpt = []
avg_pkt_lat = []
avg_net_lat = []
avg_que_lat = []
avg_max_lat = []
avg_max_net_lat = []
avg_max_que_lat = []

# thrpt_2 = []
inj_ = []

extract_sim_ticks(path, traffic_pattern, num_fault, sim_cycles,
                  pkt_lat, vc_, cntr_, net_lat, que_lat, max_lat,
                  max_net_lat, max_que_lat)

for itr in range(len(cntr_)):
    if cntr_[itr] > 0:
        # print "cntr_["+str(itr)+"]: "+str(cntr_[itr])
        avg_thrpt.append(float(100000) / (64.0 * ((sim_cycles[itr]/cntr_[itr]) - 1000.0)))
        avg_pkt_lat.append(pkt_lat[itr]/cntr_[itr])
        avg_net_lat.append(net_lat[itr]/cntr_[itr])
        avg_que_lat.append(que_lat[itr]/cntr_[itr])
        avg_max_lat.append(max_lat[itr]/cntr_[itr])
        avg_max_net_lat.append(max_net_lat[itr]/cntr_[itr])
        avg_max_que_lat.append(max_que_lat[itr]/cntr_[itr])

# for thrpt in avg_thrpt:
#     print thrpt,
#
# print (" ")

# for pkt_lat_ in avg_pkt_lat:
#     print pkt_lat_,
#
# print (" ")

# for net_lat_ in avg_net_lat:
#     print net_lat_,
#
# print(" ")

# for que_lat_ in avg_que_lat:
#     print que_lat_,
#
# print(" ")

# for max_net_lat_ in avg_max_net_lat:
#     print max_net_lat_,
#
# print(" ")

for max_que_lat_ in avg_max_que_lat:
    print max_que_lat_,

print(" ")

# for max_lat_ in avg_max_lat:
#     print max_lat_,
#
# print(" ")
# for now just get the numbers and draw it out in excel..
# in

#put here the command to plot the average of all the value extracted.