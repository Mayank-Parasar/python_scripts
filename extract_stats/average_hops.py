#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np

def extract_hops(path, traffic_, freq, rot, num_fault, cntr, total_hops):
    for root, dirs, fnames in os.walk(path):
        for dir in dirs:
            if dir.lower() == "drain_escapevc":
                path2 = os.path.join(root, dir)
                for root2, dirs2, fnames2 in os.walk(path2):
                    for dir2 in dirs2:
                        if dir2.lower() == "freq-" + str(freq):
                            path3 = os.path.join(root2, dir2)
                            for root3, dirs3, fnames3 in os.walk(path3):
                                for dir3 in dirs3:
                                    if dir3.lower() == "rot-" + str(rot):
                                        path4 = os.path.join(root3, dir3)
                                        for root4, dirs4, fnames4 in os.walk(path4):
                                            for dir4 in dirs4:
                                                if dir4.lower() == "vc-4":
                                                    path5 = os.path.join(root4, dir4)
                                                    for root5, dirs5, fnames5 in os.walk(path5):
                                                        for dir5 in dirs5:
                                                            if dir5.lower() == traffic_:
                                                                path6 = os.path.join(root5, dir5)
                                                                for root6, dirs6, fnames6 in os.walk(path6):
                                                                    for dir6 in dirs6:
                                                                        if dir6.endswith("_" + str(num_fault) + ".txt"):
                                                                            path7 = os.path.join(root6, dir6)
                                                                            for root7, dirs7, fnames7 in os.walk(path7):
                                                                                for dir7 in dirs7:
                                                                                    token = dir7.split('-')
                                                                                    idx = float(token[1])
                                                                                    index = int(idx * 50) - 1
                                                                                    # print(index)
                                                                                    file = dir7 + "/stats.txt"
                                                                                    # print(os.path.join(root7, file))
                                                                                    filepath = os.path.join(root7, file)
                                                                                    average_hops = subprocess.check_output(
                                                                                        "grep -nri misroute_per_pkt {0:s} | sed 's/.*system.ruby.network.misroute_per_pkt\s*//'"
                                                                                            .format(filepath),
                                                                                        shell=True)
                                                                                    try:
                                                                                        total_hops[index] += float(average_hops)
                                                                                        cntr[index] +=1
                                                                                    except ValueError:
                                                                                        pass


traffic_pattern = sys.argv[1]
if (traffic_pattern != "uniform_random" and
        traffic_pattern != "bit_complement" and
        traffic_pattern != "bit_reverse" and
        traffic_pattern != "bit_rotation" and
        traffic_pattern != "transpose" and
        traffic_pattern != "shuffle"):
    print("Unrecognized traffic-pattern: " + traffic_pattern)
    sys.exit()

num_fault = int(sys.argv[2])
freq = int(sys.argv[3])
rot = int(sys.argv[4])

path = os.getcwd()
path = path + "/drain_isca2019_rslt/11-27-2018/"
# path = path + "/drain_isca2019_rslt/12-05-2018/DRAIN_sweep_s"

cntr = [0] * 21
total_hops = [0] * 21
avg_hops = []

extract_hops(path, traffic_pattern, freq, rot, num_fault, cntr, total_hops)
for itr in range(len(cntr)):
    if cntr[itr] > 0:
        avg_hops.append(float(total_hops[itr])/ cntr[itr])


# for hops in avg_hops:
#     print(hops)

print("mean: {0:f}".format(np.mean(avg_hops)))