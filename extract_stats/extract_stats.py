#!/usr/bin/python

import os
import sys
from os.path import basename
import re
import subprocess
import numpy as np
# from statistics import variance

def findfiles(path, regex):
	regObj = re.compile(regex)
	res = []
	for root, dirs, fnames in os.walk(path):
		for fname in fnames:
			if regObj.match(fname):
				res.append(os.path.join(root, fname))
	return res

def idealSTAT(path, traffic_, num_fault, cntr_, pkt_lat, thrpt, lat_matrix):
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
																		index = int(idx*50) - 1
																		file = dir6+"/stats.txt"
																		filepath = os.path.join(root6, file)
																		packet_latency = subprocess.check_output(
																		"grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
																		.format(filepath), shell=True)
																		print(packet_latency)
																		throuput = subprocess.check_output(
																			"grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
																			.format(filepath), shell=True)
																		print(throuput)
																		try:
																			float(packet_latency)
																			lat_matrix[index].append(float(packet_latency))
																			pkt_lat[index] += float(packet_latency)
																			thrpt[index] += int(throuput)
																			cntr_[index] += 1
																		except ValueError:
																			print("Not a float")



def updnSTAT(path, folder_, traffic_, num_fault, cntr_, pkt_lat, thrpt, lat_matrix):
	for root, dirs, fnames in os.walk(path):
		for dir in dirs:
			if dir.lower() == "up_dn":
				path2 = os.path.join(root, dir)
				for root2, dirs2, fnames2 in os.walk(path2):
					for dir2 in dirs2:
						if dir2.lower() == folder_:
							path3 = os.path.join(root2, dir2)
							for root3, dirs3, fnames3 in os.walk(path3):
								for dir3 in dirs3:
									if dir3.lower() == "vc-4":
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
																		index = int(idx*50) - 1
																		file = dir6+"/stats.txt"
																		filepath = os.path.join(root6, file)
																		packet_latency = subprocess.check_output(
																		"grep -nri average_packet_latency {0:s} | sed 's/.*system.ruby.network.average_packet_latency\s*//'"
																		.format(filepath), shell=True)
																		print(packet_latency)
																		throuput = subprocess.check_output(
																			"grep -nri packets_received::total {0:s} | sed 's/.*system.ruby.network.packets_received::total\s*//'"
																			.format(filepath), shell=True)
																		print(throuput)
																		try:
																			float(packet_latency)
																			lat_matrix[index].append(float(packet_latency))
																			pkt_lat[index] += float(packet_latency)
																			thrpt[index] += int(throuput)
																			cntr_[index] += 1
																		except ValueError:
																			print("Not a float")

# this function returns 1 list per configuration
def spinSTAT(path, traffic_, num_vc, num_fault, cntr_, pkt_lat, thrpt, lat_matrix):
	for root, dirs, fnames in os.walk(path):
		for dir in dirs:
			if dir.lower() == "spin":
				path2 = os.path.join(root,dir)
				for root2, dirs2, fnames2 in os.walk(path2):
					for dir2 in dirs2:
						if dir2.lower() == "thresh-256":
							path3 = os.path.join(root2,dir2)
							for root3, dirs3, fnames3 in os.walk(path3):
								for dir3 in dirs3:
									# put vc here
									if dir3.lower() == "vc-4":
										path4 = os.path.join(root3,dir3)
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
																		index = int(idx*50) - 1
																		# print(index)
																		file = dir6+"/stats.txt"
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
																			lat_matrix[index].append(float(packet_latency))
																			pkt_lat[index] += float(packet_latency)
																			thrpt[index] += int(throuput)
																			cntr_[index] += 1
																		except ValueError:
																			print("Not a float")


def drainSTAT(path, traffic_, freq, rot, num_vc, num_fault, cntr_, pkt_lat, thrpt, lat_matrix):
	for root, dirs, fnames in os.walk(path):
		for dir in dirs:
			if dir.lower() == "drain":
				path2 = os.path.join(root, dir)
				for root2, dirs2, fnames2 in os.walk(path2):
					for dir2 in dirs2:
						if dir2.lower() == "freq-"+str(freq):
							path3 = os.path.join(root2,dir2)
							for root3, dirs3, fnames3 in os.walk(path3):
								for dir3 in dirs3:
									if dir3.lower() == "rot-"+str(rot):
										path4 = os.path.join(root3,dir3)
										for root4, dirs4, fnames4 in os.walk(path4):
											for dir4 in dirs4:
												if dir4.lower() == "vc-"+str(num_vc):
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
																					index = int(idx*50) - 1
																					# print(index)
																					file = dir7+"/stats.txt"
																					# print(os.path.join(root7, file))
																					filepath = os.path.join(root7, file)
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
																						lat_matrix[index].append(float(packet_latency))
																						pkt_lat[index] += float(packet_latency)
																						thrpt[index] += int(throuput)
																						cntr_[index] += 1
																					except ValueError:
																						print("Not a float")
																					# lat_matrix[index].append(float(packet_latency))
																					# pkt_lat[index] += float(packet_latency)
																					# thrpt[index] += int(throuput)
																					# cntr_[index] += 1





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
 	traffic_pattern != "shuffle") :
	print("Unrecognized traffic-pattern: " + traffic_pattern)
	pass
	usage()
	sys.exit()

num_vc = sys.argv[2]
num_fault = sys.argv[3]

path = os.getcwd()
print(path)

path = path + "/drain_isca2019_rslt/11-27-2018/"
folder = os.listdir(path)
print(folder)

up_dn_cntr_ = [0] * 21
up_dn_pkt_lat = [0] * 21
up_dn_avg_pkt_lat = [] #make it empty
up_dn_thrpt = [0] * 21
up_dn_avg_thrpt = []
up_dn_lat_matrix = [[] for i in range(21)]
#################################################################################################
folder_name = "up_dn_"
updnSTAT(path, folder_name, traffic_pattern, num_fault, up_dn_cntr_, up_dn_pkt_lat, up_dn_thrpt, up_dn_lat_matrix)
print("up-dn")
for itr in range(len(up_dn_cntr_)):
	if up_dn_cntr_[itr] > 0:
		up_dn_avg_pkt_lat.append(float(up_dn_pkt_lat[itr]/up_dn_cntr_[itr]))
		up_dn_avg_thrpt.append((float(up_dn_thrpt[itr]) / up_dn_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(up_dn_cntr_[itr], up_dn_pkt_lat[itr], up_dn_thrpt[itr], np.var(up_dn_lat_matrix[itr]), up_dn_avg_pkt_lat[itr], up_dn_avg_thrpt[itr]))
#################################################################################################

spin_256_cntr_ = [0] * 21
spin_256_pkt_lat = [0] * 21
spin_256_avg_pkt_lat = [] #make it empty
spin_256_thrpt = [0] * 21
spin_256_avg_thrpt = []
spin_256_lat_matrix = [[] for i in range(21)]
# var_mat_lat[0].append(1)
# get the path for the traffic pattern folder
# from here
# SPIN-vc-1
#################################################################################################
spinSTAT(path, traffic_pattern, num_vc, num_fault, spin_256_cntr_, spin_256_pkt_lat, spin_256_thrpt, spin_256_lat_matrix)
print("spin-256")
for itr in range(len(spin_256_cntr_)):
	if spin_256_cntr_[itr] > 0:
		spin_256_avg_pkt_lat.append(float(spin_256_pkt_lat[itr]/spin_256_cntr_[itr]))
		spin_256_avg_thrpt.append((float(spin_256_thrpt[itr]) / spin_256_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(spin_256_cntr_[itr], spin_256_pkt_lat[itr], spin_256_thrpt[itr], np.var(spin_256_lat_matrix[itr]), spin_256_avg_pkt_lat[itr], spin_256_avg_thrpt[itr]))
#################################################################################################

drain_100_1_cntr_ = [0] * 21
drain_100_1_pkt_lat = [0] * 21
drain_100_1_avg_pkt_lat = [] #make it empty
drain_100_1_thrpt = [0] * 21
drain_100_1_avg_thrpt = []
drain_100_1_lat_matrix = [[] for i in range(21)] #TODO: is this correct?
#################################################################################################
drainSTAT(path, traffic_pattern, 100, 1, num_vc, num_fault, drain_100_1_cntr_, drain_100_1_pkt_lat, drain_100_1_thrpt, drain_100_1_lat_matrix)
print("drain_f-100_s-1")
for itr in range(len(drain_100_1_cntr_)):
	if drain_100_1_cntr_[itr] > 0:
		drain_100_1_avg_pkt_lat.append(float(drain_100_1_pkt_lat[itr]/drain_100_1_cntr_[itr]))
		drain_100_1_avg_thrpt.append((float(drain_100_1_thrpt[itr]) / drain_100_1_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(drain_100_1_cntr_[itr], drain_100_1_pkt_lat[itr], drain_100_1_thrpt[itr], np.var(drain_100_1_lat_matrix[itr]), drain_100_1_avg_pkt_lat[itr], drain_100_1_avg_thrpt[itr]))
#################################################################################################

drain_100_8_cntr_ = [0] * 21
drain_100_8_pkt_lat = [0] * 21
drain_100_8_avg_pkt_lat = [] #make it empty
drain_100_8_thrpt = [0] * 21
drain_100_8_avg_thrpt = []
drain_100_8_lat_matrix = [[] for i in range(21)] #TODO: is this correct?
#################################################################################################
drainSTAT(path, traffic_pattern, 100, 8, num_vc, num_fault, drain_100_8_cntr_, drain_100_8_pkt_lat, drain_100_8_thrpt, drain_100_8_lat_matrix)
print("drain_f-100_s-8")
for itr in range(len(drain_100_8_cntr_)):
	if drain_100_8_cntr_[itr] > 0:
		drain_100_8_avg_pkt_lat.append(float(drain_100_8_pkt_lat[itr]/drain_100_8_cntr_[itr]))
		drain_100_8_avg_thrpt.append((float(drain_100_8_thrpt[itr]) / drain_100_8_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(drain_100_8_cntr_[itr], drain_100_8_pkt_lat[itr], drain_100_8_thrpt[itr], np.var(drain_100_8_lat_matrix[itr]), drain_100_8_avg_pkt_lat[itr], drain_100_8_avg_thrpt[itr]))
#################################################################################################

drain_1000_1_cntr_ = [0] * 21
drain_1000_1_pkt_lat = [0] * 21
drain_1000_1_avg_pkt_lat = [] #make it empty
drain_1000_1_thrpt = [0] * 21
drain_1000_1_avg_thrpt = []
drain_1000_1_lat_matrix = [[] for i in range(21)] #TODO: is this correct?
#################################################################################################
drainSTAT(path, traffic_pattern, 1000, 1, num_vc, num_fault, drain_1000_1_cntr_, drain_1000_1_pkt_lat, drain_1000_1_thrpt, drain_1000_1_lat_matrix)
print("drain_f-1000_s-1")
for itr in range(len(drain_1000_1_cntr_)):
	if drain_1000_1_cntr_[itr] > 0:
		drain_1000_1_avg_pkt_lat.append(float(drain_1000_1_pkt_lat[itr]/drain_1000_1_cntr_[itr]))
		drain_1000_1_avg_thrpt.append((float(drain_1000_1_thrpt[itr]) / drain_1000_1_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(drain_1000_1_cntr_[itr], drain_1000_1_pkt_lat[itr], drain_1000_1_thrpt[itr], np.var(drain_1000_1_lat_matrix[itr]), drain_1000_1_avg_pkt_lat[itr], drain_1000_1_avg_thrpt[itr]))
#################################################################################################

drain_1000_8_cntr_ = [0] * 21
drain_1000_8_pkt_lat = [0] * 21
drain_1000_8_avg_pkt_lat = [] #make it empty
drain_1000_8_thrpt = [0] * 21
drain_1000_8_avg_thrpt = []
drain_1000_8_lat_matrix = [[] for i in range(21)] #TODO: is this correct?
#################################################################################################
drainSTAT(path, traffic_pattern, 1000, 8, num_vc, num_fault, drain_1000_8_cntr_, drain_1000_8_pkt_lat, drain_1000_8_thrpt, drain_1000_8_lat_matrix)
print("drain_f-1000_s-8")
for itr in range(len(drain_1000_8_cntr_)):
	if drain_1000_8_cntr_[itr] > 0:
		drain_1000_8_avg_pkt_lat.append(float(drain_1000_8_pkt_lat[itr]/drain_1000_8_cntr_[itr]))
		drain_1000_8_avg_thrpt.append((float(drain_1000_8_thrpt[itr]) / drain_1000_8_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(drain_1000_8_cntr_[itr], drain_1000_8_pkt_lat[itr], drain_1000_8_thrpt[itr], np.var(drain_1000_8_lat_matrix[itr]), drain_1000_8_avg_pkt_lat[itr], drain_1000_8_avg_thrpt[itr]))
#################################################################################################

drain_5000_1_cntr_ = [0] * 21
drain_5000_1_pkt_lat = [0] * 21
drain_5000_1_avg_pkt_lat = [] #make it empty
drain_5000_1_thrpt = [0] * 21
drain_5000_1_avg_thrpt = []
drain_5000_1_lat_matrix = [[] for i in range(21)] #TODO: is this correct?
#################################################################################################
drainSTAT(path, traffic_pattern, 5000, 1, num_vc, num_fault, drain_5000_1_cntr_, drain_5000_1_pkt_lat, drain_5000_1_thrpt, drain_5000_1_lat_matrix)
print("drain_f-5000_s-1")
for itr in range(len(drain_5000_1_cntr_)):
	if drain_5000_1_cntr_[itr] > 0:
		drain_5000_1_avg_pkt_lat.append(float(drain_5000_1_pkt_lat[itr]/drain_5000_1_cntr_[itr]))
		drain_5000_1_avg_thrpt.append((float(drain_5000_1_thrpt[itr]) / drain_5000_1_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(drain_5000_1_cntr_[itr], drain_5000_1_pkt_lat[itr], drain_5000_1_thrpt[itr], np.var(drain_5000_1_lat_matrix[itr]), drain_5000_1_avg_pkt_lat[itr], drain_5000_1_avg_thrpt[itr]))
#################################################################################################

drain_5000_8_cntr_ = [0] * 21
drain_5000_8_pkt_lat = [0] * 21
drain_5000_8_avg_pkt_lat = [] #make it empty
drain_5000_8_thrpt = [0] * 21
drain_5000_8_avg_thrpt = []
drain_5000_8_lat_matrix = [[] for i in range(21)] #TODO: is this correct?
#################################################################################################
drainSTAT(path, traffic_pattern, 5000, 8, num_vc, num_fault, drain_5000_8_cntr_, drain_5000_8_pkt_lat, drain_5000_8_thrpt, drain_5000_8_lat_matrix)
print("drain_f-5000_s-8")
for itr in range(len(drain_5000_8_cntr_)):
	if drain_5000_8_cntr_[itr] > 0:
		drain_5000_8_avg_pkt_lat.append(float(drain_5000_8_pkt_lat[itr]/drain_5000_8_cntr_[itr]))
		drain_5000_8_avg_thrpt.append((float(drain_5000_8_thrpt[itr]) / drain_5000_8_cntr_[itr]))
		print("pkt_lat_cntr: {0:d} \t pkt_lat: {1:f} \t thrpt: {2:d} \t average_pkt_latency: {4:f} \t average_thrput: {5:f} \t latency_variance: {3:f}"
			  .format(drain_5000_8_cntr_[itr], drain_5000_8_pkt_lat[itr], drain_5000_8_thrpt[itr], np.var(drain_5000_8_lat_matrix[itr]), drain_5000_8_avg_pkt_lat[itr], drain_5000_8_avg_thrpt[itr]))
#################################################################################################

# print(*a, sep = ", ")
print("~~~~DONE~~~~~")
print("spin-256"),
for itr in spin_256_avg_pkt_lat:
	print itr,
print("")
print("drain_f-100_s-1"),
for itr in drain_100_1_avg_pkt_lat:
	print itr,
print("")
print("drain_f-100_s-8"),
for itr in drain_100_8_avg_pkt_lat:
	print itr,
print("")
print("drain_f-1000_s-1"),
for itr in drain_1000_1_avg_pkt_lat:
	print itr,
print("")
print("drain_f-1000_s-8"),
for itr in drain_1000_8_avg_pkt_lat:
	print itr,
print("")
print("drain_f-5000_s-1"),
for itr in drain_5000_1_avg_pkt_lat:
	print itr,
print("")
print("drain_f-5000_s-8"),
for itr in drain_5000_8_avg_pkt_lat:
	print itr,
print("")
print("~~~~AVG-THROUGH-PUT~~~~~")
print("spin-256"),
for itr in spin_256_avg_thrpt:
	print itr,
print("")
print("drain_f-100_s-1"),
for itr in drain_100_1_avg_thrpt:
	print itr,
print("")
print("drain_f-100_s-8"),
for itr in drain_100_8_avg_thrpt:
	print itr,
print("")
print("drain_f-1000_s-1"),
for itr in drain_1000_1_avg_thrpt:
	print itr,
print("")
print("drain_f-1000_s-8"),
for itr in drain_1000_8_avg_thrpt:
	print itr,
print("")
print("drain_f-5000_s-1"),
for itr in drain_5000_1_avg_thrpt:
	print itr,
print("")
print("drain_f-5000_s-8"),
for itr in drain_5000_8_avg_thrpt:
	print itr,