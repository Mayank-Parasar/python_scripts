#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np


# this function returns 1 list per configuration
def spinSTAT(path, traffic_, num_vc_, num_fault, cntr_, pkt_lat, thrpt, total_spins, lat_matrix):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "spin":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "thresh-4096":
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    # put vc here
                                    if dir3.lower() == "vc-"+str(num_vc_):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == traffic_:
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            if dir5.endswith("_" + str(num_fault) + ".txt"):
                                                                path6 = os.path.join(root5, dir5)
                                                                for root6, dirs6, fnames6 in os.walk(path6):
                                                                    for dir6 in dirs6:
                                                                        token = dir6.split('-')
                                                                        idx = float(token[1])
                                                                        index = int(idx * 50) - 1
                                                                        # print(index)
                                                                        file = dir6 + "/stats.txt"
                                                                        # print(os.path.join(root6, file))
                                                                        filepath = os.path.join(root6, file)
                                                                        packet_latency = subprocess.check_output(
                                                                            "grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
                                                                                .format(filepath), shell=True)
                                                                        # print(packet_latency)
                                                                        throuput = subprocess.check_output(
                                                                            "grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
                                                                                .format(filepath), shell=True)
                                                                        num_spin = subprocess.check_output(
                                                                            "grep -nri total_spins {0:s} | sed 's/.*total_spins\s*//'"
                                                                                .format(filepath), shell=True)
                                                                        # print(throuput)
                                                                        try:
                                                                            float(packet_latency)
                                                                            lat_matrix[index].append(
                                                                                float(packet_latency))
                                                                            pkt_lat[index] += float(packet_latency)
                                                                            thrpt[index] += int(throuput)
                                                                            total_spins[index] += int(num_spin)
                                                                            cntr_[index] += 1
                                                                        except ValueError:
                                                                            print("Not a float")


def usage():
    pass
    script_name = basename(sys.argv[0])
    print("Usage:")
    print("  " + script_name + " <traffic-pattern> <num-vc> <num-fault>")


if len(sys.argv) != 4:
    usage()
    sys.exit()

traffic_pattern = sys.argv[1]
if (traffic_pattern != "uniform_random" and
        traffic_pattern != "bit_complement" and
        traffic_pattern != "bit_reverse" and
        traffic_pattern != "bit_rotation" and
        traffic_pattern != "transpose" and
        traffic_pattern != "shuffle"):
    print("Unrecognized traffic-pattern: " + traffic_pattern)
    pass
    usage()
    sys.exit()

num_vc = int(sys.argv[2])
num_fault = int(sys.argv[3])

print("num_vc: {0:d}".format(num_vc))
print("num_fault: {0:d}".format(num_fault))

path = os.getcwd()
print(path)
path = path + "/drain_isca2019_rslt/11-27-2018/"

spin_cntr_ = [0] * 21
spin_pkt_lat = [0] * 21
spin_avg_pkt_lat = []  # make it empty
spin_thrpt = [0] * 21
spin_avg_thrpt = []
spin_lat_matrix = [[] for i in range(21)]
spin_total_spins = [0] * 21
spin_avg_total_spins = []
# SPIN-vc-1
#################################################################################################
spinSTAT(path, traffic_pattern, num_vc, num_fault, spin_cntr_, spin_pkt_lat, spin_thrpt, spin_total_spins,
         spin_lat_matrix)
# print("spin-256")
for itr in range(len(spin_cntr_)):
    if spin_cntr_[itr] > 0:
        spin_avg_pkt_lat.append(float(spin_pkt_lat[itr] / spin_cntr_[itr]))
        spin_avg_thrpt.append((float(spin_thrpt[itr]) / spin_cntr_[itr]))
        spin_avg_total_spins.append((float(spin_total_spins[itr])) / spin_cntr_[itr])
        # print(
        #     "pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
        #     .format(spin_cntr_[itr], spin_pkt_lat[itr], spin_thrpt[itr], np.var(spin_lat_matrix[itr]),
        #             spin_avg_pkt_lat[itr], spin_avg_thrpt[itr]))
for itr in spin_avg_total_spins:
    print(itr)

print("mean number of spins: {0:f}".format(np.mean(spin_avg_total_spins)))
