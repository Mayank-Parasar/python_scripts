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
vc_ = int(sys.argv[1])
print vc_
print script_name

call(["ls", "-ltr"])
pkt_lat = 0
injection_rate = 0.02
# output_dir = "./vc_-"+
# os.system("ls -ltr")
while(pkt_lat < 100.00 and injection_rate < 1.0 ):
    os.system("./build/Garnet_standalone/gem5.opt -d ./vc-%d/inj-%1.2f/ configs/example/garnet_synth_traffic.py --topology=Mesh_XY --num-cpus=64 --num-dirs=64 --mesh-rows=8 --network=garnet2.0 --router-latency=1  --sim-cycles=10000  --inj-vnet=0 --vcs-per-vnet=%d --injectionrate=%1.2f --synthetic=uniform_random --routing-algorithm=0"%(vc_, injection_rate, vc_, injection_rate))
    packet_latency = subprocess.check_output("grep -nri average_flit_latency ./vc-%d/inj-%1.2f/ | sed 's/.*system.ruby.network.average_flit_latency\s*//'"%(vc_, injection_rate), shell=True)
    pkt_lat = float(packet_latency)
    # print ("Packet Latency: %f"%((float)packet_latency))
    print ("Packet Latency: %f" %(pkt_lat))
    injection_rate+=0.02
    print ("injection_rate: %1.2f" %(injection_rate))
# print ("Hello world")
