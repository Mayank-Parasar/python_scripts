from pylab import *
import matplotlib.pyplot as plt
import numpy as np


def plot2_line_graph(injr_, sim1_thrpt_, sim2_thrpt_, vc_, traffic_, title_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    fig, ax = subplots()
    # ax.axis('tight')
    ax.plot(injr_, sim1_thrpt_, label="sim-type-1", linewidth=2.00, ls='-', marker='o', markersize=4,
            markerfacecolor="blue")
    ax.plot(injr_, sim2_thrpt_, label="sim-type-2", linewidth=2.00, ls='-', marker='o', markersize=4,
            markerfacecolor="red")
    ax.set_ylim(ymin=0.02)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("packets received/cycle/node")
    ax.legend(loc=4)
    stri=traffic_+" ( VC-"+str(vc_)+" )"

    # x0, xmax = plt.xlim()
    # y0, ymax = plt.ylim()
    # print xmax
    # print ymax
    # ax.text(0.15, 0.030, stri, fontsize=20, color="black")
    # ax.text(xmax / 4, ymax / 2, stri, fontsize=20, color="black")
    # ax.set_title(stri)
    ax.set_title(title_)
    # file_name="irregular_fig/"+traffic_+"_VC-"+str(vc_)+".png"
    file_name="irregular_fig/"+title_+".png"
    fig.savefig(file_name)
    # fig.show()

# def plot1_line_thrpt_graph(injr, thrpt_)

# injr=np.linspace(0.02,0.98,49)
# print injr,
#
# sim1_thrpt=[0.020027969,0.039979063,0.059961719,0.079906563,0.099942344,0.119785313,0.139718594,0.159763906,0.179700625,0.198283281,0.214879688,0.225436563,0.202057656,0.190400313,0.183236563,0.175121094,0.170248438,0.165706563,0.16440625,0.163147656,0.161875,0.160588906,0.15933375,0.158091094,0.156932813,0.156039219,0.155406875,0.154797969,0.154092031,0.15359,0.153587969,0.153586875,0.153585625,0.153585469,0.153583906,0.153585469,0.153586094,0.153585625,0.153585313,0.153585469,0.153585469,0.153585938,0.153585156,0.153585156,0.153585,0.153584531,0.15358375,0.153585469,0.153584688]
# sim2_thrpt=[0.020013321,0.039833274,0.059939389,0.079699056,0.099821121,0.119906377,0.139683533,0.159227555,0.178164196,0.195190506,0.205835858,0.213281463,0.192165785,0.178225163,0.167740204,0.164768533,0.158952187,0.154427753,0.152528309,0.152097732,0.150486372,0.148979786,0.148908796,0.146975825,0.146631006,0.145146307,0.145146307,0.144235207,0.143638536,0.143112292,0.143112292,0.143112292,0.14326976,0.14326976,0.14326976,0.14326976,0.143112292,0.143112292,0.143033687,0.143020595,0.143112292,0.143112292,0.143112292,0.143112292,0.143112292,0.143112292,0.143112292,0.143112292,0.143112292]
# # call to plotting API:
# plot2_line_graph(injr, sim1_thrpt, sim2_thrpt, 8, "bit_complement")