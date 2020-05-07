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
from shlex import split



def extract_stat_drain(path, traffic_pattern, drain_, cntr_,
                                   num_fault, vc_, freq, rot, stat_type = "none"):
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
                                                                        ijr_ = dir6.split('-')
                                                                        idx = float(ijr_[1])
                                                                        index = int(np.round(idx * 50.0 - 1.0))
                                                                        with open(file_path, "r") as file:
                                                                            # print file_path
                                                                            for line in file:
                                                                                line = line.rstrip()
                                                                                if stat_type == "success_uturn":
                                                                                    if "sim_ticks " in line:
                                                                                        lineOut = line.split()
                                                                                        sim_ticks = int(lineOut[1])
                                                                                    if "system.ruby.network.total_successful_uturns " in line:
                                                                                        lineOut = line.split()
                                                                                        success_uturn = int(lineOut[1])
                                                                                        print "sucess_uturn: ", success_uturn
                                                                                        print "sim_ticks: ", sim_ticks
                                                                                        drain_[index] += float(
                                                                                            success_uturn)/sim_ticks
                                                                                        print "drain_: ", drain_
                                                                                        cntr_[index] += 1








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
path = os.getcwd()
# thresh = int(sys.argv[7]) # used for SPIN

if option.lower() == "success_uturn":
    path = path + \
           "/drain_hpca2019_rslt/04-23-2019/DRAIN/simType-2/64c/DRAIN_escapeVC/uTurnCrossbar-1/"
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_0 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, 0, vc_, freq,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_0.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_0:
        print success_uturn

    ############
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_1 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, 1, vc_, freq,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_1.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_1:
        print success_uturn

    ############
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_4 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, 4, vc_, freq,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_4.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_4:
        print success_uturn

    ############
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_8 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, 8, vc_, freq,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_8.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_8:
        print success_uturn

    ############
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_12 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, 12, vc_, freq,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_12.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_12:
        print success_uturn

    plot_thrpt.plot5_line_graph("fault-0", drain_stat_0, "fault-1", drain_stat_1,
                                "fault-4", drain_stat_4, "fault-8", drain_stat_8,
                                "fault-12", drain_stat_12, vc_, "uniform_random", 1, freq)
    #######################################################################################
elif option.lower() == "success_uturn_per_fault":
    path = path + \
           "/drain_hpca2019_rslt/04-23-2019/DRAIN/simType-2/64c/DRAIN_escapeVC/uTurnCrossbar-1/"

    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_0 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, num_fault, vc_, 1024,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_0.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_0:
        print success_uturn

    ############
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_1 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, num_fault, vc_, 4096,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_1.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_1:
        print success_uturn

    ############
    cntr_ = [0] * 25  # to average out the sum for given injection rate
    drain_ = [0] * 25 # this will contain the required stat
    drain_stat_4 = []
    extract_stat_drain(path, traffic_pattern, drain_, cntr_, num_fault, vc_, 16384,
                       rot, "success_uturn")
    # do the stat processing here (for example taking average)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            drain_stat_4.append(float(drain_[itr] / cntr_[itr]))

    for success_uturn in drain_stat_4:
        print success_uturn
    #########################
    plot_thrpt.plot3_line_graph("period-1024", drain_stat_0, "period-4096", drain_stat_1,
                                "period-16384", drain_stat_4, vc_, "uniform_random", num_fault, 1)