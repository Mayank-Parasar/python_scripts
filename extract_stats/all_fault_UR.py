#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np

def extract_custom_escapeVC_thrpt(path, num_fault, cntr_, pkt_lat, thrpt):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.endswith("_" + str(num_fault) + ".txt"):
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "escape_vc_up_dn_":
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "bit_rotation":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "vc-4":
                                                    path5 = os.path.join(root4, dir4)
                                                    for root6, dirs6, fnames6 in os.walk(path5):
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
                                                            # print(throuput)
                                                            try:
                                                                float(packet_latency)
                                                                pkt_lat[index] += float(packet_latency)
                                                                thrpt[index] += int(throuput)
                                                                cntr_[index] += 1
                                                            except ValueError:
                                                                pass

def extract_upDn_thrpt(path, num_fault, cntr_, pkt_lat, thrpt, latency_matrix):
    indx = (-1)
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "up_dn":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.endswith("_" + str(num_fault) + ".txt"):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "escape_vc_up_dn_":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "uniform_random":
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:

                                                                indx = indx + 1
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
                                                                        # print(throuput)
                                                                        try:
                                                                            float(packet_latency)
                                                                            pkt_lat[index] += float(packet_latency)
                                                                            latency_matrix[indx].append(
                                                                                float(packet_latency))
                                                                            thrpt[index] += int(throuput)
                                                                            cntr_[index] += 1
                                                                        except ValueError:
                                                                            pass
                                                                            # print("Not a float")

def extract_escapeVC_thrpt(path, num_fault, cntr_, pkt_lat, thrpt, latency_matrix):
    indx = (-1)
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "up_dn":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "escape_vc_up_dn_":
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "vc-2":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "uniform_random":
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            if dir5.endswith("_" + str(num_fault) + ".txt"):
                                                                indx = indx + 1
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
                                                                        # print(throuput)
                                                                        try:
                                                                            float(packet_latency)
                                                                            pkt_lat[index] += float(packet_latency)
                                                                            latency_matrix[indx].append(
                                                                                float(packet_latency))
                                                                            thrpt[index] += int(throuput)
                                                                            cntr_[index] += 1
                                                                        except ValueError:
                                                                            pass
                                                                            # print("Not a float")

def extract_ideal_thrpt(path, num_fault, cntr_, pkt_lat, thrpt):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "up_dn":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "ideal":
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "vc-128":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "uniform_random":
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
                                                                        # print(throuput)
                                                                        try:
                                                                            float(packet_latency)
                                                                            pkt_lat[index] += float(packet_latency)
                                                                            thrpt[index] += int(throuput)
                                                                            cntr_[index] += 1
                                                                        except ValueError:
                                                                            pass
                                                                            # print("Not a float")


def extract_spin_thrpt(path, num_fault, cntr_, pkt_lat, thrpt, thresh, latency_matrix):
    indx = (-1)
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "spin":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "thresh-"+str(thresh):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    # put vc here
                                    if dir3.lower() == "vc-1":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "uniform_random":
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            if dir5.endswith("_" + str(num_fault) + ".txt"):
                                                                indx = indx + 1
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
                                                                        # print(throuput)
                                                                        try:
                                                                            float(packet_latency)
                                                                            pkt_lat[index] += float(packet_latency)
                                                                            latency_matrix[indx].append(
                                                                                float(packet_latency))
                                                                            thrpt[index] += int(throuput)
                                                                            cntr_[index] += 1
                                                                        except ValueError:
                                                                            pass
                                                                            # print("Not a float")


def extract_drain_thrpt(path, num_fault, cntr_, pkt_lat, thrpt, freq, rot, latency_matrix):
    indx = (-1)
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "freq-"+str(freq):
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "rot-"+str(rot):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "vc-1":
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "uniform_random":
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            if dir5.endswith("_" + str(num_fault) + ".txt"):
                                                                # here is the parsing of new topology folder with
                                                                # given number of fault. inc the index of sat_matrix
                                                                indx = indx + 1
                                                                # thrpt_mat[idx]
                                                                path6 = os.path.join(root5, dir5)
                                                                for root6, dirs6, fnames6 in os.walk(path6):
                                                                    for dir6 in dirs6:
                                                                        token = dir6.split('-')
                                                                        idx = float(token[1])
                                                                        index = int(idx * 50) - 1
                                                                        file = dir6 + "/stats.txt"
                                                                        filepath = os.path.join(root6, file)
                                                                        packet_latency = subprocess.check_output(
                                                                            "grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
                                                                                .format(filepath), shell=True)
                                                                        # print(packet_latency)
                                                                        throuput = subprocess.check_output(
                                                                            "grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
                                                                                .format(filepath), shell=True)
                                                                        # print(throuput)
                                                                        try:
                                                                            float(packet_latency)
                                                                            pkt_lat[index] += float(packet_latency)
                                                                            latency_matrix[indx].append(float(packet_latency))
                                                                            thrpt[index] += int(throuput)

                                                                            cntr_[index] += 1
                                                                        except ValueError:
                                                                            print("Not a float")


def usage():
    pass
    script_name = basename(sys.argv[0])
    print("Usage:")
    print("  " + script_name + " <fault_num>")


# if len(sys.argv) != 2:
#     usage()
#     sys.exit()

routing_ = sys.argv[1]
num_flt = int(sys.argv[2])
freq = int(sys.argv[3])
step = int(sys.argv[4])

# print("fault_num: {0:d}".format(num_fault))

path = os.getcwd()
# print(path)

# path = path + "/drain_isca2019_rslt/12-04-2018/"
path = path + "/drain_isca2019_rslt/12-07-2018/"
# path = path + "/drain_isca2019_rslt/11-27-2018/"
# path = path + "/irregular_up_dn/12-04-2018/"

if(routing_.lower() == "drain"):
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    lat_matrix = [[] for i in range(21)]
    extract_drain_thrpt(path+"DRAIN/", num_flt, cntr_, pkt_lat, thrpt, freq, step, lat_matrix)
    lat_var = []
    # printing out the throughput matrix here.. for computing varaince
    strt = 0
    while len(lat_matrix[strt]) > 0:
        for k in range(len(lat_matrix[strt])):
            # print(lat_matrix[strt][k]),
            # populate the vector for latency_variance
            if lat_matrix[strt][k] > (2 * lat_matrix[strt][0]):
                lat_var.append((k+1)*0.02)
        strt = strt + 1
        # print(" ")

    # print latency variance vector
    # for it in lat_var:
    #     print(it),

    # print(" ")
    # print("std. dev of throughput for fault-{1:d}-drain_{2:d}_{3:d} is: {0:f}".format(np.std(lat_var, ddof=1), num_flt, freq,
    #                                                                                   step))
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))
            print(avg_pkt_lat[itr]),

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (2*avg_pkt_lat[0]):
            break

    # sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    # norm_sat_thrpt = max(avg_thrpt) / 6400000
    norm_sat_thrpt = (itr+1)*0.02

    # max_avg_thrpt = max(avg_thrpt)
    # norm_avg_thrpt = float(max_avg_thrpt) / 6400000
    print(" normalized sat throughput for fault-{1:d}-drain_{2:d}_{3:d}: {0:f}".format(norm_sat_thrpt, num_flt, freq,
                                                                                      step))
    # print("max normalized throughput for fault-{1:d}-drain_{2:d}_{3:d}: {0:f}".format(norm_avg_thrpt, num_flt, freq,
    #                                                                                   step))
    # print("low load latency for fault-{1:d}-drain_{2:d}_{3:d}: {0:f}".format(avg_pkt_lat[0], num_flt, freq, step))
    ###########################################################################################################
elif(routing_.lower() == "spin"):
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    lat_matrix = [[] for i in range(21)]
    extract_spin_thrpt(path, num_flt, cntr_, pkt_lat, thrpt, freq, lat_matrix)
    lat_var = []
    # printing out the throughput matrix here.. for computing varaince
    strt = 0
    # while len(lat_matrix[strt]) > 0:
    #     for k in range(len(lat_matrix[strt])):
    #         # print(lat_matrix[strt][k]),
    #         # populate the vector for latency_variance
    #         if lat_matrix[strt][k] > (2 * lat_matrix[strt][0]):
    #             lat_var.append((k+1)*0.02)
    #     strt = strt + 1
        # print(" ")

    # print latency variance vector
    # for it in lat_var:
    #     print(it),
    #
    # print(" ")
    # print("std. dev of throughput for fault-{1:d}-spin_{2:d} is: {0:f}".format(np.std(lat_var, ddof=1), num_flt, freq,
    #                                                                                   ))
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (2*avg_pkt_lat[0]):
            break

    # sat_thrpt = avg_thrpt[itr]
    # # norm_sat_thrpt = float(sat_thrpt) / 6400000
    # norm_sat_thrpt = max(avg_thrpt) / 6400000
    norm_sat_thrpt = (itr + 1) * 0.02

    print("sat normalized throughput for fault-{1:d}-spin_{2:d}: {0:f}".format(norm_sat_thrpt, num_flt, freq))
    # print("low load latency for fault-{1:d}-spin_{2:d}: {0:f}".format(avg_pkt_lat[0], num_flt, freq))
elif(routing_.lower() == "up_dn"):
    cntr_ = [0] * 21
    pkt_lat = [0] * 21
    avg_pkt_lat = []  # make it empty
    thrpt = [0] * 21
    avg_thrpt = []
    lat_matrix = [[] for i in range(21)]
    # extract_custom_escapeVC_thrpt(path, num_flt, cntr_, pkt_lat, thrpt)
    extract_upDn_thrpt(path, num_flt, cntr_, pkt_lat, thrpt, lat_matrix)
    # extract_escapeVC_thrpt(path, num_flt, cntr_, pkt_lat, thrpt, lat_matrix)
    # extract_ideal_thrpt(path, num_flt, cntr_, pk t_lat, thrpt)
    lat_var = []
    # printing out the throughput matrix here.. for computing varaince
    strt = 0
    while len(lat_matrix[strt]) > 0:
        for k in range(len(lat_matrix[strt])):
            # print(lat_matrix[strt][k]),
            # populate the vector for latency_variance
            if lat_matrix[strt][k] > (2 * lat_matrix[strt][0]):
                lat_var.append((k+1)*0.02)
        strt = strt + 1
        # print(" ")

    # print latency variance vector
    for it in lat_var:
        print(it),

    print(" ")
    print("std. dev of throughput for fault-{1:d}-upDn-escapeVC_ is: {0:f}".format(np.std(lat_var, ddof=1), num_flt
                                                                                      ))


    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(pkt_lat[itr] / cntr_[itr]))
            avg_thrpt.append((float(thrpt[itr]) / cntr_[itr]))

    # for itr in range(len(avg_pkt_lat)):
    #     print(avg_pkt_lat[itr]),
    #     print(avg_thrpt[itr])

    for itr in range(len(avg_pkt_lat)):
        if avg_pkt_lat[itr] > (3*avg_pkt_lat[0]):
            break

    sat_thrpt = avg_thrpt[itr]
    # norm_sat_thrpt = float(sat_thrpt) / 6400000
    norm_sat_thrpt = max(avg_thrpt) / 6400000

    print("sat normalized throughput for fault-{1:d}-EscapeVC-up_dn: {0:f}".format(norm_sat_thrpt, num_flt))
    # print("low load latency for fault-{1:d}-IDEAL: {0:f}".format(avg_pkt_lat[0], num_flt))

else:
    print("unidentified option")
    sys.exit()