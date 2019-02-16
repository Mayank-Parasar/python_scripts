#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
# import plot_thrpt
from shlex import split

def extract_flt_dist(path, traffic_pattern, flt_dist, num_fault, vc_):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.endswith("_"+ str(num_fault)+".txt"):
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
                                                file_path = path4+"/"+dir4+"/stats.txt"
                                                # print file_path
                                                with open(file_path , "r") as file:
                                                    for line in file:
                                                        line = line.rstrip()    # it removes '\n'
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
            if dir.endswith("_"+ str(num_fault)+".txt"):
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
                                                if dir5.lower() == "marked_pkt-"+str(marked_flit):
                                                    path4 = os.path.join(root5, dir5)
                                                    for root4, dirs4, fnames4 in os.walk(path4):
                                                        for dir4 in dirs4:
                                                            file_path = path4+"/"+dir4+"/stats.txt"
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

def extract_topology_avg_lat(path, traffic_pattern, flt_latency, cntr_, num_fault, vc_):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.endswith("_"+ str(num_fault)+".txt"):
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
                                            for dir4 in dirs4:
                                                if dir4.lower() == "vc-" + str(vc_):
                                                    path5 = os.path.join(root4, dir4)
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

def extract_flt_tail_lat(path, traffic_pattern, flt_tail_latency, inj_, num_fault, vc_, marked_flit):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.endswith("_"+str(num_fault)+".txt"):
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
                                                if dir4.lower() == "marked_pkt-"+str(marked_flit):
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            file_path = path5+"/"+dir5+"/stats.txt"
                                                            ijr_ = dir5.split('-')
                                                            ijr1_ = ijr_[1]
                                                            inj_.append(ijr1_)
                                                            with open (file_path, "r") as file:
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

marked_flit = int(sys.argv[5])

path = os.getcwd()
# print path
path = path + "/irregular_up_dn/02-14-2019/64c/"
# print path
flt_dist = [] # define the empty list.
flt_latency = []
flt_lat_hist = []
flt_tail_latency = []
inj_ = []
cntr_ = [0] * 25 # to average out the sum for given injection rate
flt_lat = [0] * 25
avg_pkt_lat = []
############################
if (option.lower() == "distribution"):
    extract_flt_dist(path, traffic_pattern, flt_dist, num_fault, vc_)
elif (option.lower() == "marked_latency"):
    extract_flt_avg_lat(path, traffic_pattern, flt_latency, inj_, num_fault, vc_, marked_flit)
    for x,y in zip(inj_, flt_latency):
        print x, y

elif (option.lower() == "avg_latency"):
    extract_topology_avg_lat(path, traffic_pattern, flt_lat, cntr_, num_fault, vc_)
    for itr in range(len(cntr_)):
        if cntr_[itr] > 0:
            avg_pkt_lat.append(float(flt_lat[itr] / cntr_[itr]))
    for lat_ in avg_pkt_lat:
        print lat_,

elif (option.lower() == "tail-latency"):
    extract_flt_tail_lat(path, traffic_pattern, flt_tail_latency, inj_, num_fault, vc_, marked_flit)
    for x,y in zip(inj_, flt_tail_latency):
        print x, y
elif (option.lower() == "marked_histogram"):
    extract_lat_hist(path, traffic_pattern, flt_lat_hist, inj_, num_fault, vc_, marked_flit)

elif (option.lower() == "average_hops"):
    pass
else:
    print("wrong option!")
