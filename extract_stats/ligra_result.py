#!/usr/bin/python

import os
import sys
import xlsxwriter as excelwriter
from os.path import basename
import re
import subprocess
import numpy as np
import plot_thrpt
import math
from shlex import split


###### Function definition #######
def extract_stats_escapeVC(path, benchmark_, num_fault, vc_, cntr_, stat_, stats="None"):
    path = path + "/ligra_benchmark_result/irregular_up_dn/03-19-2019/escapeVC_UP_DN/"
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == benchmark_.lower():
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.endswith("_" + str(num_fault) + ".txt"):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "vc-" + str(vc_):
                                        path4 = os.path.join(root3, dir3)
                                        file_path = path4 + "/stats.txt"
                                        # print file_path
                                        with open(file_path, "r") as file:
                                            for line in file:
                                                line = line.rstrip()
                                                if stats == "pkt_latency":
                                                    if "system.ruby.network.average_packet_latency" in line:
                                                        lineOut = line.split()
                                                        stat_[0] += float(lineOut[1])
                                                        cntr_[0] += 1
                                                        # print "stat_", stat_
                                                        # print "cntr_", cntr_
                                                if stats == "sim_ticks":
                                                    if "sim_ticks" in line:
                                                        lineOut = line.split()
                                                        stat_[0] += int(lineOut[1])
                                                        cntr_[0] += 1


###################
def extract_stats_drain(path, benchmark_, num_fault, vc_, period_, cntr_, stat_, stats="None"):
    # path = path + "/ligra_benchmark_result/DRAIN/03-19-2019/"
    path = path + "/ligra_benchmark_result/DRAIN/vnet-0/03-21-2019/"
    dirs = os.listdir(path)
    for dir in dirs:
        if dir == benchmark_:
            path1 = os.path.join(path, dir)
            dirs1 = os.listdir(path1)
            for dir1 in dirs1:
                if dir1.lower() == "drain-" + str(period_):
                    path2 = os.path.join(path1, dir1)
                    dirs2 = os.listdir(path2)
                    for dir2 in dirs2:
                        if dir2.endswith("_" + str(num_fault) + ".txt"):
                            path3 = os.path.join(path2, dir2)
                            dirs3 = os.listdir(path3)
                            for dir3 in dirs3:
                                if dir3.lower() == "vc-" + str(vc_):
                                    path4 = os.path.join(path3, dir3)
                                    file_path = path4 + "/stats.txt"
                                    # print file_path
                                    with open(file_path, "r") as file:
                                        for line in file:
                                            line = line.rstrip()
                                            if stats == "pkt_latency":
                                                if "system.ruby.network.average_packet_latency" in line:
                                                    lineOut = line.split()
                                                    stat_[0] += float(lineOut[1])
                                                    cntr_[0] += 1
                                                    # print "stat_", stat_
                                                    # print "cntr_", cntr_
                                            if stats == "sim_ticks":
                                                if "sim_ticks" in line:
                                                    lineOut = line.split()
                                                    stat_[0] += int(lineOut[1])
                                                    cntr_[0] += 1


###### Parsing command-line option ######
benchmark_ = sys.argv[1]
vc_ = int(sys.argv[2])
num_fault = int(sys.argv[3])

option = sys.argv[4]
path = os.getcwd()

if option.lower() == "escapevc-all_vc":

    if benchmark_.lower() == "all":
        # benchmark = [ "bc", "bellmanford", "bfs", "bfs-bitvector", "bfscc", "cf", "components",
        #               "components-shortcut"]
        # for root, dirs, fnames in os.walk(path + "/ligra_benchmark_result/irregular_up_dn/03-19-2019/escapeVC_UP_DN/"):
        dirs = os.listdir(path + "/ligra_benchmark_result/irregular_up_dn/03-19-2019/escapeVC_UP_DN/")
        print dirs
        for benchmark in dirs:
            print benchmark,
            for vc_ in [1, 2, 4, 8]:
                cntr_ = [0]
                stat_ = [0]
                extract_stats_escapeVC(path, benchmark, num_fault, vc_, cntr_, stat_, "sim_ticks")
                print float(stat_[0]) / cntr_[0],
            print " "
if option.lower() == "drain_evc_all_vc":
    if benchmark_.lower() == "all":
        workbook = excelwriter.Workbook('demo.xlxs')
        benchmarks = os.listdir(path + "/ligra_benchmark_result/DRAIN/03-19-2019/")
        for benchmark in benchmarks:
            print benchmark,
            cntr_ = [0]
            stat_ = [0]
            extract_stats_escapeVC(path, benchmark, num_fault, vc_, cntr_, stat_, "sim_ticks")
            print float(stat_[0]) / cntr_[0],
            ##################################
            cntr_ = [0]
            stat_ = [0]
            extract_stats_drain(path, benchmark, num_fault, vc_, 1024, cntr_, stat_, "sim_ticks")
            print float(stat_[0]) / cntr_[0],
            ##################################
            cntr_ = [0]
            stat_ = [0]
            extract_stats_drain(path, benchmark, num_fault, vc_, 65536, cntr_, stat_, "sim_ticks")
            print float(stat_[0]) / cntr_[0]
            ##################################
if option.lower() == "drain_lat":
    if benchmark_.lower() == "all":
        benchmarks = ['BC', 'BFS', 'BFS-Bitvector', 'BFSCC', 'Components', 'Components-Shortcut', 'KCore', 'MIS',
                      'PageRank', 'PageRankDelta', 'Radii', 'Triangle', 'BellmanFord', 'CF']
        for benchmark in benchmarks:
            print benchmark,
            cntr_ = [0]
            stat_ = [0]
            extract_stats_drain(path, benchmark, num_fault, vc_, 65536, cntr_, stat_, "sim_ticks")
            print float(stat_[0]) / cntr_[0]
