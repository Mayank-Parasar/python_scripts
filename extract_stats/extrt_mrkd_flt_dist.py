#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
import plot_thrpt
import math
import statistics
# import try_stackedBarPlot
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


def extract_topology_avg_lat_eVC(path, traffic_pattern, eVC_, cntr_, num_fault, vc_, ni_pol):
    if ni_pol == "fcfs":
        path = path + "/irregular_up_dn/03-03-2019/64c/"
    elif ni_pol == "rr":
        path = path + "/irregular_up_dn/02-20-2019/64c/"
    else:
        assert (0)
    next_file = 0
    # print path
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
                                                            print file_path
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
                                                                        if "system.ruby.network.average_marked_pkt_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            eVC_[index] += float(avg_pkt_lat)
                                                                            cntr_[index] += 1
                                                                    elif option.lower() == "saturation-throughput":
                                                                        if "system.ruby.network.average_packet_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            # print avg_pkt_lat
                                                                            if avg_pkt_lat > 100.0:
                                                                                eVC_.append(idx)
                                                                                # print eVC_,
                                                                                # print " "
                                                                                # print file_path,
                                                                                # print " "
                                                                                next_file = 1
                                                                                continue

def extract_avg_lat_eVC(path, traffic_pattern, eVC_, eVC_min_, cntr_,
                        num_fault, vc_, ni_pol, listoflist):
    next_file = 0
    if ni_pol == "fcfs":
        path = path + "/irregular_up_dn/03-03-2019/64c/"
    else:
        print "other option is not implemented"
        assert(0)
    list_idx_ = 0
    tmp_list = [0] * 20
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "vc-" + str(vc_):
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == traffic_pattern:
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.endswith("_" + str(num_fault) + ".txt"):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                file_path = path4 + "/" + dir4 + "/stats.txt"
                                                # print file_path
                                                ijr_ = dir4.split('-')
                                                idx = float(ijr_[1])
                                                index = int(np.round(idx * 50.0 - 1.0))
                                                if index == 0:
                                                    next_file = 0
                                                    if tmp_list[0] > 0.0:
                                                        listoflist.append(tmp_list)
                                                        tmp_list = [0] * 20
                                                with open(file_path, "r") as file:
                                                    # print file_path
                                                    for line in file:
                                                        if next_file == 1:
                                                            continue
                                                        line = line.rstrip()
                                                        if option.lower() == "evc_avg_latency" \
                                                                or option.lower() == "avg_lat":
                                                            if "system.ruby.network.average_marked_pkt_latency " in line:
                                                                lineOut = line.split()
                                                                avg_pkt_lat = float(lineOut[1])
                                                                eVC_[index] += float(avg_pkt_lat)
                                                                tmp_list[index] = (float(avg_pkt_lat))
                                                                cntr_[index] += 1
                                                                if eVC_min_[index] == 0:
                                                                	eVC_min_[index] = float(avg_pkt_lat)
                                                                if eVC_min_[index] > float(avg_pkt_lat):
                                                                	eVC_min_[index] = float(avg_pkt_lat)
                                                                # print tmp_list
                                                        elif option.lower() == "evc-sat-thrpt":
                                                            if "system.ruby.network.average_packet_latency " in line:
                                                                lineOut = line.split()
                                                                avg_pkt_lat = float(lineOut[1])
                                                                if avg_pkt_lat > 100.0:
                                                                    drain_.append(idx)
                                                                    # print drain_,
                                                                    # print " "
                                                                    # print file_path,
                                                                    # print " "
                                                                    next_file = 1
                                                                    continue
# noinspection Duplicates
def extract_topology_avg_lat_drain(path, traffic_pattern, drain_, drain_min_, cntr_,
                                   num_fault, vc_, freq, rot, stat_type = "none"):
    next_file = 0
    prev_index = 0
    if option.lower() == "sweep" \
        or option.lower() == "sweep-sat-thrpt" \
        or option.lower() == "rot-sweep" \
        or option.lower() == "period-rot-sweep" \
		or option.lower() == "num-drain-sweep" \
		or option.lower() == "avg-fwd-prg" \
		or option.lower() == "avg-mis-route" \
		or option.lower() == "avg-bubble-movement" \
        or option == "stackedPlot" \
		or option.lower() == "avg_lat" \
		or option.lower() == "average_latency" \
        or option.lower() == "low_load" \
        or option.lower() == "sat_thrpt":
        path = path + "/drain_micro2019_rslt/03-04-2019/DRAIN/simType-2/sweep/64c/DRAIN_escapeVC/uTurnCrossbar-1/"
    else:
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
                                                                        if prev_index > index:
                                                                            # print "index ", index,
                                                                            # print "prev_index", prev_index
                                                                            if option.lower() == "sat_thrpt":
                                                                                # print file_path
                                                                                # print os.listdir(path6)
                                                                                drain_.append(prev_index)
                                                                        if index == 0:
                                                                            # print file_path
                                                                            next_file = 0
                                                                        prev_index = index
                                                                        with open(file_path, "r") as file:
                                                                            # print file_path
                                                                            for line in file:
                                                                                if next_file == 1:
                                                                                    continue
                                                                                line = line.rstrip()
                                                                                if option.lower() == "avg_latency" \
                                                                                    or option.lower() == "sweep" \
                                                                                    or option.lower() == "rot-sweep" \
                                                                                    or option.lower() == "period-rot-sweep" \
                                                                                    or option.lower() == "avg_lat":
                                                                                    if "system.ruby.network.average_marked_flt_latency " in line:
                                                                                        lineOut = line.split()
                                                                                        avg_pkt_lat = float(lineOut[1])
                                                                                        drain_[index] += float(
                                                                                            avg_pkt_lat)
                                                                                        cntr_[index] += 1
                                                                                        if drain_min_[index] == 0:
                                                                                        	drain_min_[index] = float(avg_pkt_lat)
                                                                                        if drain_min_[index] > float(avg_pkt_lat):
                                                                                        	drain_min_[index] = float(avg_pkt_lat)
                                                                                elif option.lower() == "saturation-throughput" \
                                                                                        or option.lower() == "sweep-sat-thrpt" :
                                                                                    if "system.ruby.network.average_packet_latency " in line:
                                                                                        lineOut = line.split()
                                                                                        avg_pkt_lat = float(lineOut[1])
                                                                                        if avg_pkt_lat > 100.0:
                                                                                            drain_.append(idx)
                                                                                            next_file = 1
                                                                                            continue
                                                                                elif option.lower() == "num-drain-sweep":
                                                                                    if "system.ruby.network.total_DRAIN_spins " in line:
                                                                                        lineOut = line.split()
                                                                                        total_spin = int(lineOut[1])
                                                                                        drain_[index] += int(total_spin)
                                                                                        cntr_[index] += 1
                                                                                elif option.lower() == "avg-fwd-prg" \
                                                                                        or stat_type == "pkt_route":
                                                                                    if "system.ruby.network.flit_forward_progress_per_drain " in line:
                                                                                        lineOut = line.split()
                                                                                        fwd_prog = float(lineOut[1])
                                                                                        # NaN check
                                                                                        if math.isnan(fwd_prog):
                                                                                            drain_[index] += float(0.0)
                                                                                            cntr_[index] += 1
                                                                                        else:
                                                                                            drain_[index] += float(fwd_prog)
                                                                                            cntr_[index] += 1
                                                                                elif option.lower() == "avg-mis-route" \
                                                                                        or stat_type == "pkt_misroute":
                                                                                    if "system.ruby.network.flit_misroute_per_drain " in line:
                                                                                        lineOut = line.split()
                                                                                        avg_misroute = float(lineOut[1])
                                                                                        # NaN check
                                                                                        if math.isnan(avg_misroute):
                                                                                            drain_[index] += float(0.0)
                                                                                            cntr_[index] += 1
                                                                                        else:
                                                                                            drain_[index] += float(
                                                                                                avg_misroute)
                                                                                            cntr_[index] += 1
                                                                                elif option.lower() == "avg-bubble-movement" \
                                                                                        or stat_type == "bubble_movement":
                                                                                    if "system.ruby.network.bubble_movement_per_drain " in line:
                                                                                        lineOut = line.split()
                                                                                        bubble_movement = float(
                                                                                                            lineOut[1])
                                                                                        # NaN check
                                                                                        if math.isnan(bubble_movement):
                                                                                            drain_[index] += float(0.0)
                                                                                            cntr_[index] += 1
                                                                                        else:
                                                                                            drain_[index] += float(
                                                                                                bubble_movement)
                                                                                            cntr_[index] += 1
                                                                                elif option.lower() == "low_load":
                                                                                    if "system.ruby.network.average_packet_latency " in line:
                                                                                        lineOut = line.split()
                                                                                        avg_pkt_lat = float(lineOut[1])
                                                                                        if index == 0:
                                                                                            drain_[0] += avg_pkt_lat
                                                                                            cntr_[0] += 1

def extract_topology_avg_lat_spin(path, traffic_pattern, spin_, spin_min_, cntr_,
                                  num_fault, vc_, thresh):
    next_file = 0
    if option.lower() == "spin_avg_lat" \
    	or option.lower() == "avg_lat" \
    	or option.lower() == "average_latency":
        path = path + "/drain_micro2019_rslt/SPIN/simType-2/03-10-2019/"
    else:
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
                                                            # print file_path
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
                                                                    # No need to pass 'option' to this API as it is global
                                                                    if option.lower() == "avg_latency":
                                                                        if "system.ruby.network.average_packet_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            spin_[index] += float(avg_pkt_lat)
                                                                            cntr_[index] += 1
                                                                    elif option.lower() == "spin_avg_lat" \
                                                                            or option.lower() == "avg_lat":
                                                                        if "system.ruby.network.average_marked_flt_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            spin_[index] += float(avg_pkt_lat)
                                                                            cntr_[index] += 1
                                                                            if spin_min_[index] == 0:
                                                                            	spin_min_[index] = float(avg_pkt_lat)
                                                                            if spin_min_[index] > float(avg_pkt_lat):
                                                                            	spin_min_[index] = float(avg_pkt_lat)
                                                                    elif option.lower() == "saturation-throughput":
                                                                        if "system.ruby.network.average_packet_latency " in line:
                                                                            lineOut = line.split()
                                                                            avg_pkt_lat = float(lineOut[1])
                                                                            if avg_pkt_lat > 100.0:
                                                                                spin_.append(idx)
                                                                                # print spin_,
                                                                                # print " "
                                                                                # print file_path,
                                                                                # print " "
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
thresh = int(sys.argv[7]) # used for SPIN

marked_flit = int(sys.argv[5])  # FIXME
### lambda function ###
float_formatter = lambda x: "%.2f" % x
### ### ###
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
############################
elif (option.lower() == "spin_avg_lat"):
    #### thresh-16 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin16 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 16)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin16.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin16:
        print lat_,
    print " "
    #### thresh-64 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin64 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 64)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin64.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin64:
        print lat_,
    print " "
    #### thresh-128 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin128 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 128)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin128.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin128:
        print lat_,
    print " "
    #### thresh-1024 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin1024 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 1024)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin1024.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin1024:
        print lat_,
    print " "
    #### thresh-4096 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin4096 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 4096)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin4096.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin4096:
        print lat_,
    print " "
    #### thresh-65536 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    avg_flt_lat_spin65536 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, cntr_,
                                  num_fault, vc_, 65536)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin65536.append(float(flt_lat_spin[itr] / cntr_[itr]))
    for lat_ in avg_flt_lat_spin65536:
        print lat_,
    print " "
    # plotting Graph here
    # plot_thrpt.plot1_line_graph(avg_flt_lat_spin128, vc_, traffic_pattern, num_fault)
    plot_thrpt.plot6_line_graph_sweep("spin-16", avg_flt_lat_spin16, "spin-64", avg_flt_lat_spin64,
                                      "spin-128", avg_flt_lat_spin128, "spin-1024", avg_flt_lat_spin1024,
                                      "spin-4096", avg_flt_lat_spin4096, "spin-65536", avg_flt_lat_spin65536,
                                      vc_, traffic_pattern, num_fault)
############################
elif option.lower() == "avg_latency" \
	or option.lower() == "avg_lat":
    if option.lower() == "avg_latency":
        flit_lat_eVC_rr = [0] * 25
        cntr_ = [0] * 25  # to average out the sum for given injection rate
        extract_topology_avg_lat_eVC(path, traffic_pattern, flit_lat_eVC_rr, cntr_, num_fault, vc_, "rr")
        for itr in range(len(cntr_)):
            if cntr_[itr] > 0:
                avg_pkt_lat_eVC_rr.append(float(flit_lat_eVC_rr[itr] / cntr_[itr]))
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
    elif option.lower() == "avg_lat":
        #### average latency for escapeVC ####
        cntr_ = [0] * 25  # to average out the sum for given injection rate
        flt_lat_eVC = [0] * 25  # flit latancy
        flt_lat_min_eVC = [0] * 25 # minimum flit latency
        listoflist_0 = []
        avg_pkt_lat_eVC_fcfs = []
        extract_avg_lat_eVC(path, traffic_pattern, flt_lat_eVC, flt_lat_min_eVC,
        					cntr_, num_fault, vc_, "fcfs", listoflist_0)
        for itr in range(len(cntr_)):
            if cntr_[itr] > 0:
                avg_pkt_lat_eVC_fcfs.append(float(flt_lat_eVC[itr] / cntr_[itr]))
        for lat_ in avg_pkt_lat_eVC_fcfs:
            print lat_,
    else:
        assert(0)
    ##############################################
    print " "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flit_lat_min_drain128 = [0] * 25  # minimum flit latency for DRAIN
    avg_flt_lat_drain128 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flit_lat_min_drain128,
    							 cntr_, num_fault, vc_, 128, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain128.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain128
    print "length of avg_flt_lat_drain128: ", len(avg_flt_lat_drain128)

    ################################################
    print" "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flit_lat_min_drain4096 = [0] * 25  # minimum flit latency for DRAIN
    avg_flt_lat_drain4096 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flit_lat_min_drain4096,
    								cntr_, num_fault, vc_, 4096, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain4096.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain4096
    print "length of avg_flt_lat_drain4096: ", len(avg_flt_lat_drain4096)

    ################################################
    print " "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    flit_lat_min_spin128 = [0] * 25 # minimum flit latency for SPIN
    avg_flt_lat_spin128 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, flit_lat_min_spin128,
    								cntr_, num_fault, vc_, 128)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin128.append(float(flt_lat_spin[itr] / cntr_[itr]))

    print avg_flt_lat_spin128
    print "length of avg_flt_lat_spin128: ", len(avg_flt_lat_spin128)
    ################################################
    print " "
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_spin = [0] * 25  # flit latency for SPIN
    flit_lat_min_spin4096 = [0] * 25 # minimum flit latency for SPIN
    avg_flt_lat_spin4096 = []  # empty list
    extract_topology_avg_lat_spin(path, traffic_pattern, flt_lat_spin, flit_lat_min_spin4096,
    								cntr_, num_fault, vc_, 4096)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_spin4096.append(float(flt_lat_spin[itr] / cntr_[itr]))


    print avg_flt_lat_spin4096
    print "length of avg_flt_lat_spin4096: ", len(avg_flt_lat_spin4096)


    if option.lower() == "avg_latency":
        max_len = max(len(avg_pkt_lat_eVC_rr), len(avg_flt_lat_drain1024),
                      len(avg_flt_lat_drain128),
                      len(avg_flt_lat_spin128), len(avg_pkt_lat_eVC_fcfs),
                      len(avg_flt_lat_spin1024))
    elif option.lower() == "avg_lat":
        max_len = max(len(avg_pkt_lat_eVC_fcfs), len(avg_flt_lat_drain4096),
                      len(avg_flt_lat_drain128),
                      len(avg_flt_lat_spin128), len(avg_flt_lat_spin4096))
    print " "
    print "Max length: ", max_len
    print " "
                ########### Code for Length Normalization ###########
    if option.lower() == "avg_latency":
        if len(avg_pkt_lat_eVC_rr) < max_len:
            avg_pkt_lat_eVC_rr.extend([9999] * (max_len - len(avg_pkt_lat_eVC_rr)))
        if len(avg_pkt_lat_eVC_fcfs) < max_len:
            avg_pkt_lat_eVC_fcfs.extend([9999] * (max_len - len(avg_pkt_lat_eVC_fcfs)))
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

        # injr = np.linspace(0.02, 0.38, 19)
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
    elif option.lower() == "avg_lat":
        print "flt_lat_min_eVC: ", np.trim_zeros(flt_lat_min_eVC)
        print "flit_lat_min_drain128: ", np.trim_zeros(flit_lat_min_drain128)
        print "flit_lat_min_drain4096: ", np.trim_zeros(flit_lat_min_drain4096)
        print "flit_lat_min_spin128: ", np.trim_zeros(flit_lat_min_spin128)
        print "flit_lat_min_spin4096: ", np.trim_zeros(flit_lat_min_spin4096)
        # plot_thrpt.plot5_line_graph( "escapeVC(fcfs)", avg_pkt_lat_eVC_fcfs,
        #                             "spin-128", avg_flt_lat_spin128,
        #                             "spin-4096", avg_flt_lat_spin4096,
        #                             "drain-128", avg_flt_lat_drain128,
        #                             "drain-4096", avg_flt_lat_drain4096,
        #                             vc_, traffic_pattern, num_fault)
        plot_thrpt.plot5_line_graph("escapeVC(fcfs)", np.trim_zeros(flt_lat_min_eVC),
                                    "spin-128", np.trim_zeros(flit_lat_min_spin128),
                                    "spin-4096", np.trim_zeros(flit_lat_min_spin4096),
                                    "drain-128", np.trim_zeros(flit_lat_min_drain128),
                                    "drain-4096", np.trim_zeros(flit_lat_min_drain4096),
                                    vc_, traffic_pattern, num_fault)
  #######################################################
elif (option.lower() == "saturation-throughput"):
    sat_thrpt_eVC_rr = []
    extract_topology_avg_lat_eVC(path, traffic_pattern, sat_thrpt_eVC_rr, cntr_,
                                 num_fault, vc_, "rr")
    sat_thrpt_eVC_fcfs = []
    extract_topology_avg_lat_eVC(path, traffic_pattern, sat_thrpt_eVC_fcfs, cntr_,
                                 num_fault, vc_, "fcfs")
    sat_thrpt_drain128 = []
    min_lat_drain128 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain128, min_lat_drain128,
                                   cntr_, num_fault, vc_, 128, rot)
    sat_thrpt_drain1024 = []
    min_lat_drain1024 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain1024, min_lat_drain1024,
                                   cntr_, num_fault, vc_, freq, rot)

    sat_thrpt_spin128 = []
    min_lat_spin128 = []
    extract_topology_avg_lat_spin(path, traffic_pattern, sat_thrpt_spin128, min_lat_spin128,
                                  cntr_, num_fault, vc_, 128)
    sat_thrpt_spin1024 = []
    min_lat_spin1024 = []
    extract_topology_avg_lat_spin(path, traffic_pattern, sat_thrpt_spin1024, min_lat_spin1024,
                                  cntr_, num_fault, vc_, 1024)

    sat_variance = [] # empty list to plot saturation
                      # variance

    print "sat_thrpt_eVC_rr: "
    print sat_thrpt_eVC_rr
    print "variance: ", np.var(sat_thrpt_eVC_rr)
    sat_variance.append(np.var(sat_thrpt_eVC_rr))

    print "sat_thrpt_eVC_fcfs: "
    print sat_thrpt_eVC_fcfs
    print "variance: ", np.var(sat_thrpt_eVC_fcfs)
    sat_variance.append(np.var(sat_thrpt_eVC_fcfs))

    print "sat_thrpt_drain128: "
    print sat_thrpt_drain128
    print "variance: ", np.var(sat_thrpt_drain128)
    sat_variance.append(np.var(sat_thrpt_drain128))

    print "sat_thrpt_drain1024: "
    print sat_thrpt_drain1024
    print "variance: ", np.var(sat_thrpt_drain1024)
    sat_variance.append(np.var(sat_thrpt_drain1024))

    print "sat_thrpt_spin128: "
    print sat_thrpt_spin128
    print "variance: ", np.var(sat_thrpt_spin128)
    sat_variance.append(np.var(sat_thrpt_spin128))

    print "sat_thrpt_spin1024: "
    print sat_thrpt_spin1024
    print "variance: ", np.var(sat_thrpt_spin1024)
    sat_variance.append(np.var(sat_thrpt_spin1024))


    max_len = max(len(sat_thrpt_eVC_rr), len(sat_thrpt_eVC_fcfs),
                  len(sat_thrpt_drain128),
                  len(sat_thrpt_spin128), len(sat_thrpt_drain1024),
                  len(sat_thrpt_spin1024))
    limit_tmp = [] # create am empty list
    limit_tmp.append(np.max(sat_thrpt_eVC_rr))
    limit_tmp.append(np.max(sat_thrpt_eVC_fcfs))
    limit_tmp.append(np.max(sat_thrpt_drain128))
    limit_tmp.append(np.max(sat_thrpt_spin128))
    limit_tmp.append(np.max(sat_thrpt_drain1024))
    limit_tmp.append(np.max(sat_thrpt_spin1024))

    limit = np.max(limit_tmp)
    print "limit: ", limit

    ########### Code for Length Normalization ###########
    if len(sat_thrpt_eVC_rr) < max_len:
        sat_thrpt_eVC_rr.extend([9999] * (max_len - len(sat_thrpt_eVC_rr)))
    if len(sat_thrpt_eVC_fcfs) < max_len:
        sat_thrpt_eVC_fcfs.extend([9999] * (max_len - len(sat_thrpt_eVC_fcfs)))
    if len(sat_thrpt_spin128) < max_len:
        sat_thrpt_spin128.extend([9999] * (max_len - len(sat_thrpt_spin128)))
    if len(sat_thrpt_spin1024) < max_len:
        sat_thrpt_spin1024.extend([9999] * (max_len - len(sat_thrpt_spin1024)))
    if len(sat_thrpt_drain128) < max_len:
        sat_thrpt_drain128.extend([9999] * (max_len - len(sat_thrpt_drain128)))
    if len(sat_thrpt_drain1024) < max_len:
        sat_thrpt_drain1024.extend([9999] * (max_len - len(sat_thrpt_drain1024)))

    sat_thrpt_eVC_rr_ = np.array(sat_thrpt_eVC_rr)
    sat_thrpt_eVC_fcfs_ = np.array(sat_thrpt_eVC_fcfs)
    sat_thrpt_spin128_ = np.array(sat_thrpt_spin128)
    sat_thrpt_spin1024_ = np.array(sat_thrpt_spin1024)
    sat_thrpt_drain128_ = np.array(sat_thrpt_drain128)
    sat_thrpt_drain1024_ = np.array(sat_thrpt_drain1024)

    plot_thrpt.plot6_scatter_graph(sat_thrpt_eVC_rr_, sat_thrpt_eVC_fcfs_,
                                sat_thrpt_spin128_, sat_thrpt_spin1024_,
                                sat_thrpt_drain128_, sat_thrpt_drain1024_,
                                vc_, traffic_pattern, num_fault, limit)

    sat_variance_ = np.array(sat_variance)
    print sat_variance_
    plot_thrpt.plot6_bar_graph(sat_variance_, vc_, traffic_pattern, num_fault)
    #################################################################
elif (option.lower() == "sweep"):
     ### Period-16 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain16 = [0] * 25 # minimum flit latency for DRAIN
    avg_flt_lat_drain16 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain16,
                                   cntr_, num_fault, vc_, 16, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain16.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain16
    print "length of avg_flt_lat_drain16: ", len(avg_flt_lat_drain16)

    # for ii_ in range(len(avg_flt_lat_drain16)):
    #     if ii_ < (len(avg_flt_lat_drain16) - 1):
    #         if avg_flt_lat_drain16[ii_] > (avg_flt_lat_drain16[ii_ + 1] + 10):
    #             break
    # print ii_
    #
    # avg_flt_lat_drain16[(ii_ + 1):] = [101] * (len(avg_flt_lat_drain16) - ii_)
    # print avg_flt_lat_drain16

    ### Period-64 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain64 = [0] * 25 # minimum flit latency for DRAIN
    avg_flt_lat_drain64 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain64,
                                   cntr_, num_fault, vc_, 64, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain64.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain64
    print "length of avg_flt_lat_drain64: ", len(avg_flt_lat_drain64)

    # for ii_ in range(len(avg_flt_lat_drain64)):
    #     if ii_ < (len(avg_flt_lat_drain64) - 1):
    #         if avg_flt_lat_drain64[ii_] > (avg_flt_lat_drain64[ii_ + 1] + 10):
    #             break
    # print ii_
    #
    # avg_flt_lat_drain64[(ii_ + 1):] = [101] * (len(avg_flt_lat_drain64) - ii_)
    # print avg_flt_lat_drain64

    ### Period-128 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain128 = [0] * 25 # minimum flit latency for DRAIN
    avg_flt_lat_drain128 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain128,
                                   cntr_, num_fault, vc_, 128, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain128.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain128
    print "length of avg_flt_lat_drain128: ", len(avg_flt_lat_drain128)

    # for ii_ in range(len(avg_flt_lat_drain128)):
    #     if ii_ < (len(avg_flt_lat_drain128) - 1):
    #         if avg_flt_lat_drain128[ii_] > (avg_flt_lat_drain128[ii_ + 1] + 10):
    #             break
    # print ii_
    #
    # avg_flt_lat_drain128[(ii_ + 1):] = [101] * (len(avg_flt_lat_drain128) - ii_)
    # print avg_flt_lat_drain128

    ### Period-1024 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain1024 = [0] * 25 # minimum flit latency for DRAIN
    avg_flt_lat_drain1024 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain1024,
                                   cntr_, num_fault, vc_, 1024, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain1024.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain1024
    print "length of avg_flt_lat_drain1024: ", len(avg_flt_lat_drain1024)

    # for ii_ in range(len(avg_flt_lat_drain1024)):
    #     if ii_ < (len(avg_flt_lat_drain1024) - 1):
    #         if avg_flt_lat_drain1024[ii_] > (avg_flt_lat_drain1024[ii_ + 1] + 10):
    #             break
    # print ii_
    #
    # avg_flt_lat_drain1024[(ii_ + 1):] = [101] * (len(avg_flt_lat_drain1024) - ii_)
    # print avg_flt_lat_drain1024

    ### Period-4096 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain4096 = [0] * 25 # minimum flit latency for DRAIN
    avg_flt_lat_drain4096 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain4096,
                                   cntr_, num_fault, vc_, 4096, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain4096.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain4096
    print "length of avg_flt_lat_drain4096: ", len(avg_flt_lat_drain4096)

    # for ii_ in range(len(avg_flt_lat_drain4096)):
    #     if ii_ < (len(avg_flt_lat_drain4096) - 1):
    #         if avg_flt_lat_drain4096[ii_] > (avg_flt_lat_drain4096[ii_ + 1] + 10):
    #             break
    # print ii_
    #
    # avg_flt_lat_drain4096[(ii_ + 1):] = [101] * (len(avg_flt_lat_drain4096) - ii_)
    # print avg_flt_lat_drain4096

    ### Period-16384 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain16384 = [0] * 25  # minimum flit latency for DRAIN
    avg_flt_lat_drain16384 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain16384,
                                cntr_, num_fault, vc_, 16384, rot)

    for itr in range(len(cntr_)):
     if cntr_[itr] > 0:
         avg_flt_lat_drain16384.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain16384
    print "length of avg_flt_lat_drain16384: ", len(avg_flt_lat_drain16384)

    ### Period-32768 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain32768 = [0] * 25  # minimum flit latency for DRAIN
    avg_flt_lat_drain32768 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain32768,
                                cntr_, num_fault, vc_, 32768, rot)

    for itr in range(len(cntr_)):
     if cntr_[itr] > 0:
         avg_flt_lat_drain32768.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain32768
    print "length of avg_flt_lat_drain32768: ", len(avg_flt_lat_drain32768)

    ### Period-65536 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain65536 = [0] * 25 # minimum flit latency for DRAIN
    avg_flt_lat_drain65536 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, flt_lat_min_drain65536,
                                   cntr_, num_fault, vc_, 65536, rot)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain65536.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain65536
    print "length of avg_flt_lat_drain65536: ", len(avg_flt_lat_drain65536)

    # for ii_ in range(len(avg_flt_lat_drain65536)):
    #     if ii_ < (len(avg_flt_lat_drain65536) - 1):
    #         if avg_flt_lat_drain65536[ii_] > (avg_flt_lat_drain65536[ii_ + 1] + 10):
    #             break
    # print ii_
    #
    # avg_flt_lat_drain65536[(ii_ + 1):] = [101] * (len(avg_flt_lat_drain65536) - ii_)
    # print avg_flt_lat_drain65536

    max_len = max(len(avg_flt_lat_drain16), len(avg_flt_lat_drain64),
                  len(avg_flt_lat_drain128),
                  len(avg_flt_lat_drain1024), len(avg_flt_lat_drain4096),
                  len(avg_flt_lat_drain65536))
    print " "
    print "Max length: ", max_len
    print " "

    ########### Code for Length Normalization ###########
    if len(avg_flt_lat_drain16) < max_len:
        avg_flt_lat_drain16.extend([9999] * (max_len - len(avg_flt_lat_drain16)))
    if len(avg_flt_lat_drain64) < max_len:
        avg_flt_lat_drain64.extend([9999] * (max_len - len(avg_flt_lat_drain64)))
    if len(avg_flt_lat_drain128) < max_len:
        avg_flt_lat_drain128.extend([9999] * (max_len - len(avg_flt_lat_drain128)))
    if len(avg_flt_lat_drain1024) < max_len:
        avg_flt_lat_drain1024.extend([9999] * (max_len - len(avg_flt_lat_drain1024)))
    if len(avg_flt_lat_drain4096) < max_len:
        avg_flt_lat_drain4096.extend([9999] * (max_len - len(avg_flt_lat_drain4096)))
    if len(avg_flt_lat_drain65536) < max_len:
        avg_flt_lat_drain65536.extend([9999] * (max_len - len(avg_flt_lat_drain65536)))


    injr = np.linspace(0.02, (max_len*0.02), max_len)
    avg_flt_lat_drain16_ = np.array(avg_flt_lat_drain16)
    avg_flt_lat_drain64_ = np.array(avg_flt_lat_drain64)
    avg_flt_lat_drain128_ = np.array(avg_flt_lat_drain128)
    avg_flt_lat_drain1024_ = np.array(avg_flt_lat_drain1024)
    avg_flt_lat_drain4096_ = np.array(avg_flt_lat_drain4096)
    avg_flt_lat_drain65536_ = np.array(avg_flt_lat_drain65536)


    # plot_thrpt.plot6_line_graph_sweep( "DRAIN-16", avg_flt_lat_drain16_, "DRAIN-64", avg_flt_lat_drain64_,
    #                             "DRAIN-128" ,avg_flt_lat_drain128_, "DRAIN-1024", avg_flt_lat_drain1024_,
    #                             "DRAIN-4096", avg_flt_lat_drain4096_, "DRAIN-65536", avg_flt_lat_drain65536_,
    #                             vc_, traffic_pattern, num_fault, rot)

    # plot_thrpt.plot6_line_graph_sweep("DRAIN-16", np.trim_zeros(flt_lat_min_drain16),
    #                                   "DRAIN-64", np.trim_zeros(flt_lat_min_drain64),
    #                                     "DRAIN-128", np.trim_zeros(flt_lat_min_drain128),
    #                                     "DRAIN-1024", np.trim_zeros(flt_lat_min_drain1024),
    #                                     "DRAIN-4096", np.trim_zeros(flt_lat_min_drain4096),
    #                                     "DRAIN-65536", np.trim_zeros(flt_lat_min_drain65536),
    #                                     vc_, traffic_pattern, num_fault, rot)
    plot_thrpt.plot7_line_graph_sweep("DRAIN-16", np.trim_zeros(flt_lat_min_drain16),
                                    "DRAIN-64", np.trim_zeros(flt_lat_min_drain64),
                                    "DRAIN-128", np.trim_zeros(flt_lat_min_drain128),
                                    "DRAIN-1024", np.trim_zeros(flt_lat_min_drain1024),
                                    "DRAIN-4096", np.trim_zeros(flt_lat_min_drain4096),
                                    "DRAIN-16384", np.trim_zeros(flt_lat_min_drain16384),
                                    "DRAIN-32768", np.trim_zeros(flt_lat_min_drain32768),
                                    vc_, traffic_pattern, num_fault, rot)
    #################################################################
elif (option == "stackedPlot"):
	##############
    print "num_fault: ", num_fault
    ring_size = int(224 - 2*(num_fault))
    print "DRAIN ring size: ", ring_size

    cntr_ = [0] * 25  # to average out the sum for given injection rate
    pkt_misroute_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain1024 = [0] * 25  # flit latancy for DRAIN
    avg_pkt_misroute = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, pkt_misroute_drain, flt_lat_min_drain1024,
                                        cntr_, num_fault, vc_, freq, rot, "pkt_misroute")
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_misroute.append(float(pkt_misroute_drain[itr] / cntr_[itr]))

    print avg_pkt_misroute
    avg_pkt_misroute[:] = [x * 100 / ring_size for x in avg_pkt_misroute]
    print avg_pkt_misroute
    print "length of avg_pkt_misroute: ", len(avg_pkt_misroute)
    ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    pkt_route_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain1024 = [0] * 25  # flit latancy for DRAIN
    avg_pkt_route = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, pkt_route_drain, flt_lat_min_drain1024,
                                        cntr_, num_fault, vc_, freq, rot, "pkt_route")
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_route.append(float(pkt_route_drain[itr] / cntr_[itr]))

    print avg_pkt_route
    avg_pkt_route[:] = [x * 100 / ring_size for x in avg_pkt_route]
    print avg_pkt_route
    print "length of avg_pkt_route: ", len(avg_pkt_route)
    ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    bubble_movement_drain = [0] * 25  # flit latancy for DRAIN
    flt_lat_min_drain1024 = [0] * 25  # flit latancy for DRAIN
    avg_bubble_movement = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, bubble_movement_drain, flt_lat_min_drain1024,
                                        cntr_, num_fault, vc_, freq, rot, "bubble_movement")
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_bubble_movement.append(float(bubble_movement_drain[itr] / cntr_[itr]))

    print avg_bubble_movement
    avg_bubble_movement[:] = [x * 100 / ring_size for x in avg_bubble_movement]
    print avg_bubble_movement
    print "length of avg_bubble_movement: ", len(avg_bubble_movement)
    plot_thrpt.stackedBarPlot(avg_bubble_movement, avg_pkt_route, avg_pkt_misroute,
                              vc_, traffic_pattern, num_fault, rot, freq )
    ##################################################################
elif option.lower() == "period-rot-sweep" \
	or option.lower() == "num-drain-sweep" \
	or option.lower() == "avg-fwd-prg" \
	or option.lower() == "avg-mis-route" \
	or option.lower() == "avg-bubble-movement":
    ### Period-16 ###
    ### Rot-1 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain16_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 16, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain16_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain16_1
    print "length of avg_flt_lat_drain16_1: ", len(avg_flt_lat_drain16_1)

    ### Rot-4 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain16_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 16, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain16_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain16_4
    print "length of avg_flt_lat_drain16_4: ", len(avg_flt_lat_drain16_4)

    ### Rot-8 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain16_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 16, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain16_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain16_8
    print "length of avg_flt_lat_drain16_8: ", len(avg_flt_lat_drain16_8)
    ##################################################################################################
    ### Period-64 ###
    ### Rot-1 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain64_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 64, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain64_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain64_1
    print "length of avg_flt_lat_drain64_1: ", len(avg_flt_lat_drain64_1)

    ### Rot-4 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain64_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 64, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain64_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain64_4
    print "length of avg_flt_lat_drain64_4: ", len(avg_flt_lat_drain64_4)

    ### Rot-8 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain64_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 64, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain64_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain64_8
    print "length of avg_flt_lat_drain64_8: ", len(avg_flt_lat_drain64_8)
    ##################################################################################################
    ### Period-128 ###
    ### Rot-1 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain128_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 128, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain128_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain128_1
    print "length of avg_flt_lat_drain128_1: ", len(avg_flt_lat_drain128_1)

    ### Rot-4 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain128_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 128, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain128_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain128_4
    print "length of avg_flt_lat_drain128_4: ", len(avg_flt_lat_drain128_4)

    ### Rot-8 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain128_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 128, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain128_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain128_8
    print "length of avg_flt_lat_drain128_8: ", len(avg_flt_lat_drain128_8)

    ##################################################################################################
    ### Period-1024 ###
    ### Rot-1 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain1024_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 1024, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain1024_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain1024_1
    print "length of avg_flt_lat_drain1024_1: ", len(avg_flt_lat_drain1024_1)

    ### Rot-4 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain1024_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 1024, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain1024_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain1024_4
    print "length of avg_flt_lat_drain1024_4: ", len(avg_flt_lat_drain1024_4)

    ### Rot-8 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain1024_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 1024, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain1024_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain1024_8
    print "length of avg_flt_lat_drain1024_8: ", len(avg_flt_lat_drain1024_8)
    ##################################################################################################
    ### Period-4096 ###
    ### Rot-1 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain4096_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 4096, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain4096_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain4096_1
    print "length of avg_flt_lat_drain4096_1: ", len(avg_flt_lat_drain4096_1)

    ### Rot-4 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain4096_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 4096, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain4096_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain4096_4
    print "length of avg_flt_lat_drain4096_4: ", len(avg_flt_lat_drain4096_4)

    ### Rot-8 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain4096_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 4096, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain4096_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain4096_8
    print "length of avg_flt_lat_drain4096_8: ", len(avg_flt_lat_drain4096_8)
    ##################################################################################################
    ### Period-65536 ###
    ### Rot-1 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain65536_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 65536, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain65536_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain65536_1
    print "length of avg_flt_lat_drain65536_1: ", len(avg_flt_lat_drain65536_1)

    ### Rot-4 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain65536_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 65536, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain65536_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain65536_4
    print "length of avg_flt_lat_drain65536_4: ", len(avg_flt_lat_drain65536_4)

    ### Rot-8 ###
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drain65536_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, 65536, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drain65536_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drain65536_8
    print "length of avg_flt_lat_drain65536_8: ", len(avg_flt_lat_drain65536_8)

    max_len = max(len(avg_flt_lat_drain16_1), len(avg_flt_lat_drain16_4), len(avg_flt_lat_drain16_8),
                len(avg_flt_lat_drain64_1), len(avg_flt_lat_drain64_4), len(avg_flt_lat_drain64_8),
                len(avg_flt_lat_drain128_1), len(avg_flt_lat_drain128_4), len(avg_flt_lat_drain128_8),
                len(avg_flt_lat_drain1024_1), len(avg_flt_lat_drain1024_4), len(avg_flt_lat_drain1024_8),
                len(avg_flt_lat_drain4096_1), len(avg_flt_lat_drain4096_4), len(avg_flt_lat_drain4096_8),
                len(avg_flt_lat_drain65536_1), len(avg_flt_lat_drain65536_4), len(avg_flt_lat_drain65536_8)
                )
    print " "
    print "Max length: ", max_len
    print " "

    ########### Code for Length Normalization ###########
    # if len(avg_flt_lat_drain16_1) < max_len:
    #     avg_flt_lat_drain16_1.extend([9999] * (max_len - len(avg_flt_lat_drain16_1)))
    # if len(avg_flt_lat_drain16_4) < max_len:
    #     avg_flt_lat_drain16_4.extend([9999] * (max_len - len(avg_flt_lat_drain16_4)))
    # if len(avg_flt_lat_drain16_8) < max_len:
    #     avg_flt_lat_drain16_8.extend([9999] * (max_len - len(avg_flt_lat_drain16_8)))
    #
    # if len(avg_flt_lat_drain64_1) < max_len:
    #     avg_flt_lat_drain64_1.extend([9999] * (max_len - len(avg_flt_lat_drain64_1)))
    # if len(avg_flt_lat_drain64_4) < max_len:
    #     avg_flt_lat_drain64_4.extend([9999] * (max_len - len(avg_flt_lat_drain64_4)))
    # if len(avg_flt_lat_drain64_8) < max_len:
    #     avg_flt_lat_drain64_8.extend([9999] * (max_len - len(avg_flt_lat_drain64_8)))
    #
    # if len(avg_flt_lat_drain128_1) < max_len:
    #     avg_flt_lat_drain128_1.extend([9999] * (max_len - len(avg_flt_lat_drain128_1)))
    # if len(avg_flt_lat_drain128_4) < max_len:
    #     avg_flt_lat_drain128_4.extend([9999] * (max_len - len(avg_flt_lat_drain128_4)))
    # if len(avg_flt_lat_drain128_8) < max_len:
    #     avg_flt_lat_drain128_8.extend([9999] * (max_len - len(avg_flt_lat_drain128_8)))
    #
    # if len(avg_flt_lat_drain1024_1) < max_len:
    #     avg_flt_lat_drain1024_1.extend([9999] * (max_len - len(avg_flt_lat_drain1024_1)))
    # if len(avg_flt_lat_drain1024_4) < max_len:
    #     avg_flt_lat_drain1024_4.extend([9999] * (max_len - len(avg_flt_lat_drain1024_4)))
    # if len(avg_flt_lat_drain1024_8) < max_len:
    #     avg_flt_lat_drain1024_8.extend([9999] * (max_len - len(avg_flt_lat_drain1024_8)))
    #
    # if len(avg_flt_lat_drain4096_1) < max_len:
    #     avg_flt_lat_drain4096_1.extend([9999] * (max_len - len(avg_flt_lat_drain4096_1)))
    # if len(avg_flt_lat_drain4096_4) < max_len:
    #     avg_flt_lat_drain4096_4.extend([9999] * (max_len - len(avg_flt_lat_drain4096_4)))
    # if len(avg_flt_lat_drain4096_8) < max_len:
    #     avg_flt_lat_drain4096_8.extend([9999] * (max_len - len(avg_flt_lat_drain4096_8)))
    #
    # if len(avg_flt_lat_drain65536_1) < max_len:
    #     avg_flt_lat_drain65536_1.extend([9999] * (max_len - len(avg_flt_lat_drain65536_1)))
    # if len(avg_flt_lat_drain65536_4) < max_len:
    #     avg_flt_lat_drain65536_4.extend([9999] * (max_len - len(avg_flt_lat_drain65536_4)))
    # if len(avg_flt_lat_drain65536_8) < max_len:
    #     avg_flt_lat_drain65536_8.extend([9999] * (max_len - len(avg_flt_lat_drain65536_8)))

    injr = np.linspace(0.02, (max_len*0.02), max_len)
    print "length of avg_flt_lat_drain16_1: ", len(avg_flt_lat_drain16_1)
    print "length of avg_flt_lat_drain16_4: ", len(avg_flt_lat_drain16_4)
    print "length of avg_flt_lat_drain16_8: ", len(avg_flt_lat_drain16_8)

    print "length of avg_flt_lat_drain64_1: ", len(avg_flt_lat_drain64_1)
    print "length of avg_flt_lat_drain64_4: ", len(avg_flt_lat_drain64_4)
    print "length of avg_flt_lat_drain64_8: ", len(avg_flt_lat_drain64_8)

    print "length of avg_flt_lat_drain128_1: ", len(avg_flt_lat_drain128_1)
    print "length of avg_flt_lat_drain128_4: ", len(avg_flt_lat_drain128_4)
    print "length of avg_flt_lat_drain128_8: ", len(avg_flt_lat_drain128_8)

    print "length of avg_flt_lat_drain1024_1: ", len(avg_flt_lat_drain1024_1)
    print "length of avg_flt_lat_drain1024_4: ", len(avg_flt_lat_drain1024_4)
    print "length of avg_flt_lat_drain1024_8: ", len(avg_flt_lat_drain1024_8)

    print "length of avg_flt_lat_drain4096_1: ", len(avg_flt_lat_drain4096_1)
    print "length of avg_flt_lat_drain4096_4: ", len(avg_flt_lat_drain4096_4)
    print "length of avg_flt_lat_drain4096_8: ", len(avg_flt_lat_drain4096_8)

    print "length of avg_flt_lat_drain65536_1: ", len(avg_flt_lat_drain65536_1)
    print "length of avg_flt_lat_drain65536_4: ", len(avg_flt_lat_drain65536_4)
    print "length of avg_flt_lat_drain65536_8: ", len(avg_flt_lat_drain65536_8)

    print "length of injr: ", len(injr)


    plot_thrpt.plot18_line_graph_sweep(injr,
        avg_flt_lat_drain16_1, "drain16_1", avg_flt_lat_drain16_4, "drain16_4", avg_flt_lat_drain16_8, "drain16_8",
        avg_flt_lat_drain64_1, "drain64_1", avg_flt_lat_drain64_4, "drain64_4", avg_flt_lat_drain64_8, "drain64_8",
        avg_flt_lat_drain128_1, "drain128_1", avg_flt_lat_drain128_4, "drain128_4", avg_flt_lat_drain128_8, "drain128_8",
        avg_flt_lat_drain1024_1, "drain1024_1", avg_flt_lat_drain1024_4, "drain1024_4", avg_flt_lat_drain1024_8, "drain1024_8",
        avg_flt_lat_drain4096_1, "drain4096_1", avg_flt_lat_drain4096_4, "drain4096_4", avg_flt_lat_drain4096_8, "drain4096_8",
        avg_flt_lat_drain65536_1, "drain65536_1", avg_flt_lat_drain65536_4, "drain65536_4", avg_flt_lat_drain65536_8, "drain65536_8",
        vc_, traffic_pattern, num_fault, rot)

#################################################################################################
elif (option.lower() == "rot-sweep"):
	#### Rot-1 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN

    avg_flt_lat_drainFreq_1 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, freq, 1)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drainFreq_1.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drainFreq_1
    print "length of avg_flt_lat_drainFreq_1: ", len(avg_flt_lat_drainFreq_1)
    for ii_ in range(len(avg_flt_lat_drainFreq_1)):
        if ii_ < (len(avg_flt_lat_drainFreq_1) - 1):
            if avg_flt_lat_drainFreq_1[ii_] > (avg_flt_lat_drainFreq_1[ii_ + 1] + 10):
                break
    print ii_

    avg_flt_lat_drainFreq_1[(ii_ + 1):] = [101] * (len(avg_flt_lat_drainFreq_1) - ii_)
    print avg_flt_lat_drainFreq_1
	#### Rot-4 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drainFreq_4 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, freq, 4)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drainFreq_4.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drainFreq_4
    print "length of avg_flt_lat_drainFreq_4: ", len(avg_flt_lat_drainFreq_4)
    for ii_ in range(len(avg_flt_lat_drainFreq_4)):
        if ii_ < (len(avg_flt_lat_drainFreq_4) - 1):
            if avg_flt_lat_drainFreq_4[ii_] > (avg_flt_lat_drainFreq_4[ii_ + 1] + 10):
                break
    print ii_

    avg_flt_lat_drainFreq_4[(ii_ + 1):] = [101] * (len(avg_flt_lat_drainFreq_4) - ii_)
    print avg_flt_lat_drainFreq_4
	#### Rot-8 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat_drain = [0] * 25  # flit latancy for DRAIN
    avg_flt_lat_drainFreq_8 = []  # empty list
    extract_topology_avg_lat_drain(path, traffic_pattern, flt_lat_drain, cntr_, num_fault, vc_, freq, 8)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_flt_lat_drainFreq_8.append(float(flt_lat_drain[itr] / cntr_[itr]))

    print avg_flt_lat_drainFreq_8
    print "length of avg_flt_lat_drainFreq_8: ", len(avg_flt_lat_drainFreq_8)
    for ii_ in range(len(avg_flt_lat_drainFreq_8)):
        if ii_ < (len(avg_flt_lat_drainFreq_8) - 1):
            if avg_flt_lat_drainFreq_8[ii_] > (avg_flt_lat_drainFreq_8[ii_ + 1] + 10):
                break
    print ii_

    avg_flt_lat_drainFreq_8[(ii_ + 1):] = [101] * (len(avg_flt_lat_drainFreq_8) - ii_)
    print avg_flt_lat_drainFreq_8

    max_len = max(len(avg_flt_lat_drainFreq_1), len(avg_flt_lat_drainFreq_4),
    			len(avg_flt_lat_drainFreq_8))
    print " "
    print "Max length: ", max_len
    print " "
    ########### Code for Length Normalization ###########
    if len(avg_flt_lat_drainFreq_1) < max_len:
    	avg_flt_lat_drainFreq_1.extend([9999] * (max_len - len(avg_flt_lat_drainFreq_1)))
    if len(avg_flt_lat_drainFreq_4) < max_len:
    	avg_flt_lat_drainFreq_4.extend([9999] * (max_len - len(avg_flt_lat_drainFreq_4)))
    if len(avg_flt_lat_drainFreq_8) < max_len:
    	avg_flt_lat_drainFreq_8.extend([9999] * (max_len - len(avg_flt_lat_drainFreq_8)))

    injr = np.linspace(0.02, (max_len*0.02), max_len)
    avg_flt_lat_drainFreq_1_ = np.array(avg_flt_lat_drainFreq_1)
    avg_flt_lat_drainFreq_4_ = np.array(avg_flt_lat_drainFreq_4)
    avg_flt_lat_drainFreq_8_ = np.array(avg_flt_lat_drainFreq_8)

    plot_thrpt.plot3_line_graph_sweep(injr, avg_flt_lat_drainFreq_1_, avg_flt_lat_drainFreq_4_,
    					avg_flt_lat_drainFreq_8_, vc_, traffic_pattern, num_fault, rot, freq)

elif option.lower() == "sweep-sat-thrpt":

    sat_thrpt_drain16 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain16, cntr_,
                                   num_fault, vc_, 16, rot)
    print sat_thrpt_drain16,
    print " "
    sat_thrpt_drain64 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain64, cntr_,
                                   num_fault, vc_, 64, rot)
    print sat_thrpt_drain64,
    print " "
    sat_thrpt_drain128 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain128, cntr_,
                                   num_fault, vc_, 128, rot)
    print sat_thrpt_drain128,
    print " "
    sat_thrpt_drain1024 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain1024, cntr_,
                                   num_fault, vc_, 1024, rot)
    print sat_thrpt_drain1024,
    print " "
    sat_thrpt_drain4096 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain4096, cntr_,
                                   num_fault, vc_, 4096, rot)
    print sat_thrpt_drain4096,
    print " "
    sat_thrpt_drain65536 = []
    extract_topology_avg_lat_drain(path, traffic_pattern, sat_thrpt_drain65536, cntr_,
                                   num_fault, vc_, 65536, rot)
    print sat_thrpt_drain65536,
    print " "
    sat_variance = [] # empty list to plot saturation
                      # variance
    sat_variance.append(np.var(sat_thrpt_drain16))
    sat_variance.append(np.var(sat_thrpt_drain64))
    sat_variance.append(np.var(sat_thrpt_drain128))
    sat_variance.append(np.var(sat_thrpt_drain1024))
    sat_variance.append(np.var(sat_thrpt_drain4096))
    sat_variance.append(np.var(sat_thrpt_drain65536))

    sat_variance_ = np.array(sat_variance)
    print sat_variance_
    plot_thrpt.plot6_bar_sweep_graph(sat_variance_, vc_, traffic_pattern, num_fault, rot)
    #################################################################
elif option == "eVC_avg_latency":
    np.set_printoptions(formatter={'float_kind': float_formatter})

    #### average latency Fault-0 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat = [0] * 25  # flit latancy
    listoflist_0 = []
    avg_pkt_lat_eVC_fcfs_0 = []
    extract_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, 0, vc_, "fcfs", listoflist_0)
    print np.var(listoflist_0, 0)
    print " "
    var_f0_ = np.var(listoflist_0, 0)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_fcfs_0.append(float(flt_lat[itr] / cntr_[itr]))
    for lat_ in avg_pkt_lat_eVC_fcfs_0:
        print lat_,

    #### average latency Fault-1 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat = [0] * 25  # flit latancy
    avg_pkt_lat_eVC_fcfs_1 = []
    listoflist_1 = []
    extract_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, 1, vc_, "fcfs", listoflist_1)
    print np.var(listoflist_1, 0)
    print " "
    var_f1_ = np.var(listoflist_1, 0)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_fcfs_1.append(float(flt_lat[itr] / cntr_[itr]))

    for lat_ in avg_pkt_lat_eVC_fcfs_1:
        print lat_,


    #### average latency Fault-4 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat = [0] * 25  # flit latancy
    avg_pkt_lat_eVC_fcfs_4 = []
    listoflist_4 = []
    extract_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, 4, vc_, "fcfs", listoflist_4)
    print np.var(listoflist_4, 0)
    print " "
    var_f4_ = np.var(listoflist_4, 0)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_fcfs_4.append(float(flt_lat[itr] / cntr_[itr]))
    for lat_ in avg_pkt_lat_eVC_fcfs_4:
        print lat_,



    #### average latency Fault-8 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat = [0] * 25  # flit latancy
    avg_pkt_lat_eVC_fcfs_8 = []
    listoflist_8 = []
    extract_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, 8, vc_, "fcfs", listoflist_8)
    # print "cntr_", cntr_

    # for itr in listoflist_8:
    #     print itr
    # print " "

    print np.var(listoflist_8, 0)
    print " "
    var_f8_ = np.var(listoflist_8, 0)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_fcfs_8.append(float(flt_lat[itr] / cntr_[itr]))
    # for lat_ in avg_pkt_lat_eVC_fcfs_8:
    #     print lat_,

    #### average latency Fault-12 ####
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    flt_lat = [0] * 25  # flit latancy
    avg_pkt_lat_eVC_fcfs_12 = []
    listoflist_12 = []
    extract_avg_lat_eVC(path, traffic_pattern, flt_lat, cntr_, 12, vc_, "fcfs", listoflist_12)
    print np.var(listoflist_12, 0)
    print " "
    var_f12_ = np.var(listoflist_12, 0)

    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat_eVC_fcfs_12.append(float(flt_lat[itr] / cntr_[itr]))


    max_len = max(len(avg_pkt_lat_eVC_fcfs_0), len(avg_pkt_lat_eVC_fcfs_1),
                len(avg_pkt_lat_eVC_fcfs_4), len(avg_pkt_lat_eVC_fcfs_8),
                len(avg_pkt_lat_eVC_fcfs_12))

    injr = np.linspace(0.02, (max_len * 0.02), max_len)
    ######## trim the list to meet injr length ##########
    var_f0_ = var_f0_[0:max_len]
    var_f1_ = var_f1_[0:max_len]
    var_f4_ = var_f4_[0:max_len]
    var_f8_ = var_f8_[0:max_len]
    var_f12_ = var_f12_[0:max_len]


    ########### Code for Length Normalization ###########
    if len(avg_pkt_lat_eVC_fcfs_0) < max_len:
        avg_pkt_lat_eVC_fcfs_0.extend([9999] * (max_len - len(avg_pkt_lat_eVC_fcfs_0)))
    if len(avg_pkt_lat_eVC_fcfs_1) < max_len:
        avg_pkt_lat_eVC_fcfs_1.extend([9999] * (max_len - len(avg_pkt_lat_eVC_fcfs_1)))
    if len(avg_pkt_lat_eVC_fcfs_4) < max_len:
        avg_pkt_lat_eVC_fcfs_4.extend([9999] * (max_len - len(avg_pkt_lat_eVC_fcfs_4)))
    if len(avg_pkt_lat_eVC_fcfs_8) < max_len:
        avg_pkt_lat_eVC_fcfs_8.extend([9999] * (max_len - len(avg_pkt_lat_eVC_fcfs_8)))
    if len(avg_pkt_lat_eVC_fcfs_12) < max_len:
        avg_pkt_lat_eVC_fcfs_12.extend([9999] * (max_len - len(avg_pkt_lat_eVC_fcfs_12)))

    ######### PLOT- Graph #########
    # plot_thrpt.plot5_line_graph_eVC(injr, avg_pkt_lat_eVC_fcfs_0, "fault-0",
    #                                 avg_pkt_lat_eVC_fcfs_1, "fault-1", avg_pkt_lat_eVC_fcfs_4, "fault-4",
    #                                 avg_pkt_lat_eVC_fcfs_8, "fault-8", avg_pkt_lat_eVC_fcfs_12, "fault-12",
    #                                 vc_, traffic_pattern)
    plot_thrpt.plot5_line_graph_eVC(injr, var_f0_, "var-fault-0", var_f1_, "var-fault-1",
                                    var_f4_, "var-fault-4", var_f8_, "var-fault-8", var_f12_,
                                    "var-fault-12", vc_, traffic_pattern)
    #####################################################################

elif (option.lower() == "tail-latency"):
    extract_flt_tail_lat(path, traffic_pattern, flt_tail_latency, inj_, num_fault, vc_, marked_flit)
    for x, y in zip(inj_, flt_tail_latency):
        print x, y
elif (option.lower() == "marked_histogram"):
    extract_lat_hist(path, traffic_pattern, flt_lat_hist, inj_, num_fault, vc_, marked_flit)

elif (option.lower() == "average_hops"):
    pass
elif option.lower() == "swap":
    pass
elif option.lower() == "low_load":
    cntr_ = [0]
    stat_=[0]
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 16, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 64, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 128, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 1024, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 4096, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 16384, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 32768, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
    ##################
    cntr_ = [0]
    stat_=[0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 65536, rot, "low_load")
    print float(stat_[0]) / cntr_[0],
elif option.lower() == "sat_thrpt":
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 16, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 64, rot, "low_load")
    # print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 128, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 1024, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 4096, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 16384, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 32768, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
    ###################
    cntr_ = [0]
    stat_ = []
    dummy = [0]
    extract_topology_avg_lat_drain(path, traffic_pattern, stat_, dummy, cntr_,
                                   num_fault, vc_, 65536, rot, "low_load")
    print (statistics.mean(stat_) * float(0.02) + 0.02),
else:
    print option
    print("wrong option!")
