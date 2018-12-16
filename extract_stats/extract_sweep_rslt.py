#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np

def drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, rot):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "drain_sweep_s":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "rot-" + str(rot):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.endswith("_" + str(num_fault) + ".txt"):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                token = dir4.split('-')
                                                idx = float(token[1])
                                                index = int(idx * 50) - 1
                                                file = dir4 + "/stats.txt"
                                                filepath = os.path.join(root4, file)
                                                packet_latency = subprocess.check_output(
                                                    "grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
                                                        .format(filepath), shell=True)
                                                throuput = subprocess.check_output(
                                                    "grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
                                                        .format(filepath), shell=True)
                                                try:
                                                    float(packet_latency)
                                                    # lat_matrix[index].append(float(packet_latency))
                                                    pkt_lat[index] += float(packet_latency)
                                                    thrpt[index] += int(throuput)
                                                    cntr_[index] += 1
                                                except ValueError:
                                                    print("Not a float")

def drainSweep_f(path, num_fault, cntr_, pkt_lat, thrpt, freq):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "drain_sweep_f":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "freq-" + str(freq):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "shuffle":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.endswith("_" + str(num_fault) + ".txt"):
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            token = dir5.split('-')
                                                            idx = float(token[1])
                                                            index = int(idx * 50) - 1
                                                            file = dir5 + "/stats.txt"
                                                            filepath = os.path.join(root5, file)
                                                            packet_latency = subprocess.check_output(
                                                                "grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
                                                                    .format(filepath), shell=True)
                                                            throuput = subprocess.check_output(
                                                                "grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
                                                                    .format(filepath), shell=True)
                                                            try:
                                                                float(packet_latency)
                                                                # lat_matrix[index].append(float(packet_latency))
                                                                pkt_lat[index] += float(packet_latency)
                                                                thrpt[index] += int(throuput)
                                                                cntr_[index] += 1
                                                            except ValueError:
                                                                print("Not a float")


def usage():
    pass
    script_name = basename(sys.argv[0])
    print("Usage:")
    print("  " + script_name + " <fault_num>")


if len(sys.argv) != 3:
    usage()
    sys.exit()

num_fault = int(sys.argv[1])
sweep_option = sys.argv[2]

print("fault_num: {0:d}".format(num_fault))

path = os.getcwd()
# print(path)

# path = path + "/drain_isca2019_rslt/11-30-2018/"
path = path + "/drain_isca2019_rslt/12-03-2018/"
# path = path + "/drain_isca2019_rslt/"

if(sweep_option == "s"):
    print("hello--s")
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 1)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    print("average pkt-latency s-1:")
    for lat_ in avg_pkt_lat:
        print lat_

    # print("low load avg. pkt-latency for rot-1: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-1: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 2)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    print("average pkt-latency s-2:")
    for lat_ in avg_pkt_lat:
        print lat_

    # print("low load avg. pkt-latency for rot-2: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-2: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 3)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-3: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-3: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 4)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    print("average pkt-latency s-4:")
    for lat_ in avg_pkt_lat:
        print lat_

    # print("low load avg. pkt-latency for rot-4: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-4: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 5)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-5: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-5: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 6)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-6: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-6: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 7)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    print("average pkt-latency s-7:")
    for lat_ in avg_pkt_lat:
        print lat_

    # print("low load avg. pkt-latency for rot-7: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-7: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 8)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("average pkt-latency s-8:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("low load avg. pkt-latency for rot-8: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-8: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 9)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-9: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-9: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 10)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-10: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-10: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 11)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-11: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-11: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 12)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-12: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-12: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 13)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-13: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-13: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 14)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("low load avg. pkt-latency for rot-14: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-14: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 15)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    print("average pkt-latency s-15:")
    for lat_ in avg_pkt_lat:
        print lat_

    # print("low load avg. pkt-latency for rot-15: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-15: {0:f}".format(norm_sat_thrpt))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_s(path, num_fault, cntr_, pkt_lat, thrpt, 16)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break
    sat_thrpt = avg_thrpt[itr]
    norm_sat_thrpt = float(sat_thrpt) / 6400000

    # print("average pkt-latency s-16:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("low load avg. pkt-latency for rot-16: {0:f}".format(avg_pkt_lat[0]))
    # print("sat normalized throughput for rot-16: {0:f}".format(norm_sat_thrpt))
elif (sweep_option == "f"):
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_f(path, num_fault, cntr_, pkt_lat, thrpt, 5)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            print(avg_pkt_lat[itr]),
            print("\t {0:f}".format(avg_thrpt[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            # print("itr: {0:d}".format(itr))
            print("saturation throughput for freq-5: {0:1.2f}".format((itr + 1) * 0.02))
            break

    sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    norm_sat_thrpt = max(avg_thrpt) / 6400000
    # print("average pkt-latency f-5:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("max average throughput for freq-5: {0:f}".format(norm_sat_thrpt))
    # print("low-load latency for freq-5: {0:f}".format(avg_pkt_lat[0]))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_f(path, num_fault, cntr_, pkt_lat, thrpt, 50)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            print("saturation throughput for freq-50: {0:1.2f}".format((itr + 1) * 0.02))
            break

    sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    norm_sat_thrpt = max(avg_thrpt) / 6400000
    # print("average pkt-latency f-50:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("max average throughput for freq-50: {0:f}".format(norm_sat_thrpt))
    # print("low-load latency for freq-50: {0:f}".format(avg_pkt_lat[0]))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_f(path, num_fault, cntr_, pkt_lat, thrpt, 500)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            print("saturation throughput for freq-500: {0:1.2f}".format((itr + 1) * 0.02))
            break

    sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    norm_sat_thrpt = max(avg_thrpt) / 6400000
    # print("average pkt-latency f-50:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("max average throughput for freq-500: {0:f}".format(norm_sat_thrpt))
    # print("low-load latency for freq-500: {0:f}".format(avg_pkt_lat[0]))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_f(path, num_fault, cntr_, pkt_lat, thrpt, 5000)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            print("saturation throughput for freq-5000: {0:1.2f}".format((itr + 1) * 0.02))
            break

    sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    norm_sat_thrpt = max(avg_thrpt) / 6400000
    # print("average pkt-latency f-50:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("max average throughput for freq-5000: {0:f}".format(norm_sat_thrpt))
    # print("low-load latency for freq-5000: {0:f}".format(avg_pkt_lat[0]))
    ###########################################################################################################
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    drainSweep_f(path, num_fault, cntr_, pkt_lat, thrpt, 50000)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))


    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            print("saturation throughput for freq-50000: {0:1.2f}".format((itr + 1) * 0.02))
            break

    sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    norm_sat_thrpt = max(avg_thrpt) / 6400000
    # print("average pkt-latency f-50:")
    # for lat_ in avg_pkt_lat:
    #     print lat_

    # print("max average throughput for freq-50000: {0:f}".format(norm_sat_thrpt))
    # print("low-load latency for freq-50000: {0:f}".format(avg_pkt_lat[0]))
    ###########################################################################################################
else:
    print("unidentified option")
    sys.exit()