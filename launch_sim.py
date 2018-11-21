import os
import glob
import sys
from os.path import basename
from subprocess import call
import subprocess
path=os.getcwd()
print path
# os.chdir(path + "/../gem5_up_down/gem5/")
# print path
script_name = basename(sys.argv[0])
print script_name

call(["ls", "-ltr"])
packet_latency = 0
injection_rate = 0.02
# os.system("ls -ltr")
# while(packet_latency < 100 ):
os.system("./build/Garnet_standalone/gem5.opt configs/example/garnet_synth_traffic.py --topology=Mesh_XY --num-cpus=64 --num-dirs=64 --mesh-rows=8 --network=garnet2.0 --router-latency=1  --sim-cycles=10000  --inj-vnet=0 --vcs-per-vnet=4 --injectionrate=%f --synthetic=uniform_random --routing-algorithm=0"%(injection_rate))
packet_latency = subprocess.check_output("grep average_flit_latency m5out/stats.txt | sed 's/system.ruby.network.average_flit_latency\s*//'", shell=True)
# print ("Packet Latency: %f"%((float)packet_latency))
print ("Packet Latency: %s" %(packet_latency))
print ("Hello world")
