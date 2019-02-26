#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
import plot_thrpt
from shlex import split


def extract_flt_dist(path, traffic_pattern, flt_dist, num_fault, vc_):
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
                                    if dir3.lower() == "vc-" + str(vc_):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                file_path = path4 + "/" + dir4 + "/stats.txt"
                                                # print file_path
                                                with open(file_path, "r") as file:
                                                    for line in file:
                                                        line = line.rstrip()  # it removes '\n'
                                                        if "system.ruby.network.marked_flit_distribution " in line:
                                                            lineOut = line.split()
                                                            flt_dist = lineOut[3::4]
                                                            print dir4,
                                                            for percentage in flt_dist:
                                                                print percentage,
                                                            print " "


# API for logging latency histogram
def extract_lat_hist(path, traffic_pattern, flt_lat_hist, inj_, num_fault, vc_, marked_flit):
    pass
    # store bucket-size in a variable


def extract_flt_avg_lat(path, traffic_pattern, flt_latency, inj_, num_fault, vc_, marked_flit):
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
                                    if dir3.lower() == "vc-" + str(vc_):
                                        path4 = os.path.join(root3, dir3)
                                        for root5, dirs5, fnames5 in os.walk(path4):
                                            for dir5 in dirs5:
                                                if dir5.lower() == "marked_pkt-" + str(marked_flit):
                                                    path4 = os.path.join(root5, dir5)
                                                    for root4, dirs4, fnames4 in os.walk(path4):
                                                        for dir4 in dirs4:
                                                            file_path = path4 + "/" + dir4 + "/stats.txt"
                                                            ijr_ = dir4.split('-')
                                                            ijr1_ = ijr_[1]
                                                            inj_.append(ijr1_)
                                                            with open(file_path, "r") as file:
                                                                for line in file:
                                                                    line = line.rstrip()
                                                                    if "system.ruby.network.average_packet_latency " in line:
                                                                        lineOut = line.split()
                                                                        flt_lat = float(lineOut[1])
                                                                        flt_latency.append(flt_lat)


def extract_topology_avg_lat_eVC(path, traffic_pattern, flt_latency, cntr_, num_fault, vc_, ni_pol):
    if ni_pol == "fcfs":
        path = path + "/irregular_up_dn/02-19-2019/64c/"
    elif ni_pol == "rr":
        path = path + "/irregular_up_dn/02-20-2019/64c/"
    else:
        assert (0);
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
                                    if dir3.lower() == traffic_pattern:
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            dirs4[:] = [dir4 for dir4 in dirs4 if dir4 not in ['vnet-2']]
                                            for dir4 in dirs4:
                                                if dir4.lower() == "vc-" + str(vc_):
                                                    path5 = os.path.join(root4, dir4)
                                                    # print path5
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            file_path = path5 + "/" + dir5 + "/stats.txt"
                                                            ijr_ = dir5.split('-')
                                                            idx = float(ijr_[1])
                                                            index = int(np.round(idx * 50.0 - 1.0))
                                                            with open(file_path, "r") as file:
                                                                for line in file:
                                                                    line = line.rstrip()
                                                                    if "system.ruby.network.average_packet_latency " in line:
                                                                        lineOut = line.split()
                                                                        avg_pkt_lat = float(lineOut[1])
                                                                        flt_latency[index] += float(avg_pkt_lat)
                                                                        cntr_[index] += 1


# noinspection Duplicates
def extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat, cntr_, num_fault, vc_, freq, rot):
    path = path + "/drain_micro2019_rslt/02-15-2019/DRAIN/64c/DRAIN_escapeVC/uTurnCrossbar-1/"
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "freq-" + str(freq):
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "rot-" + str(rot):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "vc-" + str(vc_):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == traffic_pattern:
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            if dir5.endswith("_" + str(num_fault) + ".txt"):
                                                                path6 = os.path.join(root5, dir5)
                                                                # print path6
                                                                for root6, dirs6, fnames6 in os.walk(path6):
                                                                    for dir6 in dirs6:
                                                                        file_path = path6 + "/" + dir6 + "/stats.txt"
                                                                        # print file_path
                                                                        ijr_ = dir6.split('-')
                                                                        idx = float(ijr_[1])
                                                                        index = int(np.round(idx * 50.0 - 1.0))
                                                                        with open(file_path, "r") as file:
                                                                            # print file_path
                                                                            for line in file:
                                                                                line = line.rstrip()
                                                                                if option.lower() == "avg_latency":
                                                                                    if "system.ruby.network.average_packet_latency " in line:
                                                                                        lineOut = line.split()
                                                                                        avg_pkt_lat = float(lineOut[1])
                                                                                        flt_lat[index] += float(
                                                                                            avg_pkt_lat)
                                                                                        cntr_[index] += 1
                                                                                elif option.lower() == "saturation-throughput":
                                                                                    pass



def extract_topology_avg_lat_spin(path, traffic_pattern, spin_, cntr_,
                                  num_fault, vc_, thresh, option):
    next_file = 0
    path = path + "/drain_micro2019_rslt/SPIN/02-19-2019/"
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == traffic_pattern:
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.endswith("_" + str(num_fault) + ".txt"):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "thresh-" + str(thresh):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "vc-" + str(vc_):
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            file_path = path5 + "/" + dir5 + "/stats.txt"
                                                            ijr_ = dir5.split('-')
                                                            idx = float(ijr_[1])
                                                            index = int(np.round(idx * 50.0 - 1.0))
                                                            if index == 0:
                                                                next_file = 0
                                                            with open(file_path, "r") as file:
                                                                for line in file:
                                                                    if next_file == 1:
                                                                        continue
                                                                    line = line.rstrip()
                                                                    if option.lower() == "avg_latency":
                                                                        if "system.ruby.network.average_packet_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            spin_[index] += float(avg_pkt_lat)
                                                                            cntr_[index] += 1
                                                                    elif option.lower() == "saturation-throughput":
                                                                        if "system.ruby.network.average_packet_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            if avg_pkt_lat > 100.0:
                                                                                spin_.append(idx)
                                                                                print spin_,
                                                                                print " "
                                                                                print file_path,
                                                                                print " "
                                                                                next_file = 1
                                                                                continue


def extract_flt_tail_lat(path, traffic_pattern, flt_tail_latency, inj_, num_fault, vc_, marked_flit):
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
                                    if dir3.lower() == "vc-" + str(vc_):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "marked_pkt-" + str(marked_flit):
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            file_path = path5 + "/" + dir5 + "/stats.txt"
                                                            ijr_ = dir5.split('-')
                                                            ijr1_ = ijr_[1]
                                                            inj_.append(ijr1_)
                                                            with open(file_path, "r") as file:
                                                                for line in file:
                                                                    line = line.rstrip()
                                                                    if "system.ruby.network.max_marked_flit_latency " in line:
                                                                        lineOut = line.split()
                                                                        tail_lat = float(lineOut[1])
                                                                        flt_tail_latency.append(tail_lat)


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
num_fault = int(sys.argv[3])

option = sys.argv[4]

freq = int(sys.argv[5])
rot = int(sys.argv[6])
thresh = int(sys.argv[7])

marked_flit = int(sys.argv[5])  # FIXME

path = os.getcwd()
# print path

# print path
flt_dist = []  # define the empty list.
flt_latency = []
flt_lat_hist = []
flt_tail_latency = []
inj_ = []
cntr_ = [0] * 25  # to average out the sum for given injection rate
flt_lat = [0] * 25
avg_pkt_lat_eVC_rr = []
avg_pkt_lat_eVC_fcfs = []
############################
if (option.lower() == "distribution"):
    extract_flt_dist(path, traffic_pattern, flt_dist, num_fault, vc_)
elif (option.lower() == "marked_latency"):
    extract_flt_avg_lat(path, traffic_pattern, flt_latency, inj_, num_fault, vc_, marked_flit)
    for x, y in zip(inj_, flt_latency):
        print x, y

elif (option.lower() == "avg_latency"):
    extract_topology_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, num_fault, vc_, "rr")
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_rr.append(float(flt_lat[itr] / cntr_[itr]))
    for lat_ in avg_pkt_lat_eVC_rr:
        print lat_,
    ###############################################
    print " "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat = [0] * 25  # flit latancy for DRAIN
    extract_topology_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, num_fault, vc_, "fcfs")
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_fcfs.append(float(flt_lat[itr] / cntr_[itr]))
    for lat_ in avg_pkt_lat_eVC_fcfs:
        print lat_,
    ###############################################
    print" "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain1024 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, freq, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain1024.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain1024
    for ii_ in range(len(avg_flt_lat_drain1024)):
        if avg_flt_lat_drain1024[ii_] < avg_flt_lat_drain1024[ii_ - 1]:
            break
    avg_flt_lat_drain1024[ii_:] = [101] * (len(avg_flt_lat_drain1024) - ii_)
    print avg_flt_lat_drain1024

    ################################################
    print" "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain128 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 128, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain128.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain128
    for ii_ in range(len(avg_flt_lat_drain128)):
        if avg_flt_lat_drain128[ii_] < avg_flt_lat_drain128[ii_ - 1]:
            break
    avg_flt_lat_drain128[ii_:] = [101] * (len(avg_flt_lat_drain128) - ii_)
    print avg_flt_lat_drain128

    ################################################
    print " "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin128 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, thresh, option.lower())
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin128.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin128:
        print lat_,
    ################################################
    print " "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin1024 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 1024, option.lower())
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin1024.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin1024:
        print lat_,

    print " "
    print "old length of avg_flt_lat_drain_: ", len(avg_flt_lat_drain1024)

    max_len = max(len(avg_pkt_lat_eVC_rr), len(avg_flt_lat_drain1024),
                  len(avg_flt_lat_drain128),
                  len(avg_flt_lat_spin128), len(avg_pkt_lat_eVC_fcfs),
                  len(avg_flt_lat_spin1024))
    print " "
    print "Max length: ", max_len
    print " "
                    ########### Code for Length Normalization ###########
    if len(avg_pkt_lat_eVC_rr) < max_len:
        avg_pkt_lat_eVC_rr.extend([9999] * (max_len - len(avg_pkt_lat_eVC_rr)))
    if len(avg_pkt_lat_eVC_fcfs) < max_len:
        avg_pkt_lat_eVC_fcfs.extend([9999] * (max_len - len(avg_pkt_lat_eVC_rr)))
    if len(avg_flt_lat_spin128) < max_len:
        avg_flt_lat_spin128.extend([9999] * (max_len - len(avg_flt_lat_spin128)))
    if len(avg_flt_lat_spin1024) < max_len:
        avg_flt_lat_spin1024.extend([9999] * (max_len - len(avg_flt_lat_spin1024)))
    if len(avg_flt_lat_drain128) < max_len:
        avg_flt_lat_drain128.extend([9999] * (max_len - len(avg_flt_lat_drain128)))
    if len(avg_flt_lat_drain1024) < max_len:
        avg_flt_lat_drain1024.extend([9999] * (max_len - len(avg_flt_lat_drain1024)))

    print avg_flt_lat_drain1024,
    print " "
    print "new length of avg_flt_lat_drain_: ", len(avg_flt_lat_drain1024)
    print " "

    injr = np.linspace(0.02, 0.38, 19)
    avg_pkt_lat_eVC_rr_ = np.array(avg_pkt_lat_eVC_rr)
    avg_pkt_lat_eVC_fcfs_ = np.array(avg_pkt_lat_eVC_fcfs)
    avg_flt_lat_spin128_ = np.array(avg_flt_lat_spin128)
    avg_flt_lat_spin1024_ = np.array(avg_flt_lat_spin1024)
    avg_flt_lat_drain128_ = np.array(avg_flt_lat_drain128)
    avg_flt_lat_drain1024_ = np.array(avg_flt_lat_drain1024)

    # NOTE: Cautious about order of parameter you ae passing to plot function
    # and what label you are using for those parameters in the plot legend
    ################ PLOT-FUNCTION ######################
    # plot_thrpt.plot5_line_graph(injr, avg_pkt_lat_eVC_rr_, avg_pkt_lat_eVC_fcfs_,
    #                             avg_flt_lat_spin128_, avg_flt_lat_spin1024_,
    #                             avg_flt_lat_drain1024_,
    #                             vc_, traffic_pattern, num_fault)
    plot_thrpt.plot6_line_graph(injr, avg_pkt_lat_eVC_rr_, avg_pkt_lat_eVC_fcfs_,
                                avg_flt_lat_spin128_, avg_flt_lat_spin1024_,
                                avg_flt_lat_drain128_, avg_flt_lat_drain1024_,
                                vc_, traffic_pattern, num_fault)
elif (option.lower() == "saturation-throughput"):
    sat_thrpt = []
    extract_topology_avg_lat_spin(path, traffic_pattern, sat_thrpt, cntr_,
                                  num_fault, vc_, thresh, option.lower())
elif (option.lower() == "tail-latency"):
    extract_flt_tail_lat(path, traffic_pattern, flt_tail_latency, inj_, num_fault, vc_, marked_flit)
    for x, y in zip(inj_, flt_tail_latency):
        print x, y
elif (option.lower() == "marked_histogram"):
    extract_lat_hist(path, traffic_pattern, flt_lat_hist, inj_, num_fault, vc_, marked_flit)

elif (option.lower() == "average_hops"):
    pass
else:
    print("wrong option!")
