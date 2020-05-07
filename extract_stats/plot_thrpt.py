import matplotlib as mpl

mpl.use('Agg')

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


### lambda function ###
float_formatter = lambda x: "%.2f" % x
### ### ### ###

def plot2_line_graph(y_val1_, label_1, y_val2_, label_2, whenToSwap,
                     vc_, traffic_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    fig, ax = subplots()
    # ax.axis('tight')
    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_,
            label=label_1, linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="blue", color="orange")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_,
            label=label_2, linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="red", color="green")
    ax.set_ylim(ymin=0.02)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("packets received/cycle/node")
    ax.legend(loc=0)
    # stri = traffic_ + " ( VC-" + str(vc_) + " )"

    ax.set_ylim(ymin=min(min(y_val1_), min(y_val2_)) - 2)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.0)

    ax.set_title(traffic_+" VC-"+str(vc_)+" SwapPeriod-"+str(whenToSwap))
    stri = traffic_+"_VC-"+str(vc_)+"_SwapPeriod"+str(whenToSwap)
    # file_name="irregular_fig/"+traffic_+"_VC-"+str(vc_)+".png"
    # file_name = stri + ".png"
    file_name = "swap_plots/" + stri + ".png"
    fig.savefig(file_name)
    # fig.show()

def plot3_line_graph(label1_, y_val1_, label2_, y_val2_, label3_, y_val3_,
                     vc_, traffic_, fault_, rot_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_, label=str(label1_), linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="blue", color="blue")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_, label=str(label2_), linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="red", color="red")
    ax.plot(np.linspace(0.02, (len(y_val3_) * 0.02), len(y_val3_)), y_val3_, label=str(label3_), linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="red", color="black")
    # ax.set_ylim(ymin = min(min(y_val1_), min(y_val2_), min(y_val3_)) - 2)
    # ax.set_ylim(ymax = 100)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("total U-turns/cycle")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "periodSweep-" + str(traffic_) + "VC-" + str(vc_) + \
           "fault-" + str(fault_) + "rot-" + str(rot_)
    ax.set_title(stri)
    # fig.savefig("simType1_sweep_plots_04_03_2019/" + str(stri) + ".png")
    fig.savefig("plots_23_april_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()

def plot5_line_graph_eVC(injr, y_val1_, label_1,  y_val2_, label_2, y_val3_, label_3,
                         y_val4_, label_4, y_val5_, label_5, vc_, traffic_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(injr, y_val1_, label=str(label_1), linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="blue", color="blue")
    ax.plot(injr, y_val2_, label=str(label_2), linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="red", color="red")
    ax.plot(injr, y_val3_, label=str(label_3), linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="red", color="black")
    ax.plot(injr, y_val4_, label=str(label_4), linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="orange", color="green")
    ax.plot(injr, y_val5_, label=str(label_5), linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="black", color="purple")
    ax.set_ylim(ymin=min(min(y_val1_), min(y_val2_), min(y_val3_),
                    min(y_val4_), min(y_val5_)))
    ax.set_ylim(ymax=max(max(y_val1_), max(y_val2_), max(y_val3_), max(y_val4_), max(y_val5_)))
    ax.set_ylim(ymin=min(min(y_val1_), min(y_val2_), min(y_val3_), min(y_val4_), min(y_val5_)))
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("variance across topologies for latency")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "variance_eVC-" + str(traffic_) + "VC-" + str(vc_)
    ax.set_title(stri)
    fig.savefig("eVC_plots_05_03_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()


def plot5_line_graph(label1_, y_val1_, label2_, y_val2_,
                     label3_, y_val3_, label4_, y_val4_,
                     label5_, y_val5_, vc_, traffic_, rot, period):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_, label=label1_,
            linewidth=3.00, ls='-', markersize=4, markerfacecolor="blue", color="blue")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_, label=label2_,
            linewidth=3.00, ls='-', markersize=4, markerfacecolor="red", color="red")
    ax.plot(np.linspace(0.02, (len(y_val3_) * 0.02), len(y_val3_)), y_val3_, label=label3_,
            linewidth=3.00, ls='-', marker='*', markersize=4, markerfacecolor="red", color="black")
    ax.plot(np.linspace(0.02, (len(y_val4_) * 0.02), len(y_val4_)), y_val4_, label=label4_,
            linewidth=3.00, ls='-', marker='*', markersize=4, markerfacecolor="orange", color="green")
    ax.plot(np.linspace(0.02, (len(y_val5_) * 0.02), len(y_val5_)), y_val5_, label=label5_,
            linewidth=3.00, ls='-', marker='o', markersize=4, markerfacecolor="black", color="purple")
    # ax.set_ylim(ymin=10)
    # ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("total U-turns/cycle")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "Traffic-" + str(traffic_) + "VC-" + str(vc_) + "rot-" + str(rot) + "period-" + str(period)
    ax.set_title(stri)
    fig.savefig("plots_23_april_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()


def plot6_line_graph(injr, y_val1_, y_val2_, y_val3_, y_val4_, y_val5_,
                     y_val6_, vc_, traffic_, fault_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(injr, y_val1_, label="escapeVC(rr)", linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="blue", color="blue")
    ax.plot(injr, y_val2_, label="escapeVC(fcfs)", linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="red", color="red")
    ax.plot(injr, y_val3_, label="SPIN-128", linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="red", color="black")
    ax.plot(injr, y_val4_, label="SPIN-1024", linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="orange", color="green")
    ax.plot(injr, y_val5_, label="DRAIN-128", linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="black", color="purple")
    ax.plot(injr, y_val6_, label="DRAIN-1024", linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="black", color="gray")
    ax.set_ylim(ymin=0.02)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("total U-turns/cycle")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    # fig.savefig("plots_25_02_2019/" + str(stri) + ".png")
    fig.savefig(str(stri) + ".png")
    # fig.show()

def plot6_line_graph_sweep(label1_, y_val1_, label2_, y_val2_,
                           label3_, y_val3_, label4_, y_val4_,
                           label5_, y_val5_, label6_, y_val6_,
                           vc_, traffic_, fault_, rot_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_, label=label1_, linewidth=3.00,
            markersize=4, markerfacecolor="blue", color="blue")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_, label=label2_, linewidth=3.00,
            markersize=4, markerfacecolor="red", color="red")
    ax.plot(np.linspace(0.02, (len(y_val3_) * 0.02), len(y_val3_)), y_val3_, label=label3_, linewidth=3.00,
            marker='*', markersize=4, markerfacecolor="red", color="black")
    ax.plot(np.linspace(0.02, (len(y_val4_) * 0.02), len(y_val4_)), y_val4_, label=label4_, linewidth=3.00,
            marker='*', markersize=4, markerfacecolor="orange", color="green")
    ax.plot(np.linspace(0.02, (len(y_val5_) * 0.02), len(y_val5_)), y_val5_, label=label5_, linewidth=3.00,
            marker='o', markersize=4, markerfacecolor="black", color="purple")
    ax.plot(np.linspace(0.02, (len(y_val6_) * 0.02), len(y_val6_)), y_val6_, label=label6_, linewidth=3.00,
            marker='s', markersize=4, markerfacecolor="black", color="gray")
    ax.set_ylim(ymin=10)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("average packet latency")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "sweepTraffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_) + "rot-" + str(rot_)
    # stri = "sweepTraffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    # fig.savefig("spin_simType2_sweep_plots_10_03_2019/" + str(stri) + ".png")
    fig.savefig(str(stri) + ".png")
    # fig.show()


def plot7_line_graph_sweep(label1_, y_val1_, label2_, y_val2_,
                           label3_, y_val3_, label4_, y_val4_,
                           label5_, y_val5_, label6_, y_val6_,
                           label7_, y_val7_,
                           vc_, traffic_, fault_, rot_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_, label=label1_, linewidth=3.00,
            markersize=4, markerfacecolor="blue", color="blue")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_, label=label2_, linewidth=3.00,
            markersize=4, markerfacecolor="red", color="red")
    ax.plot(np.linspace(0.02, (len(y_val3_) * 0.02), len(y_val3_)), y_val3_, label=label3_, linewidth=3.00,
            marker='*', markersize=4, markerfacecolor="red", color="black")
    ax.plot(np.linspace(0.02, (len(y_val4_) * 0.02), len(y_val4_)), y_val4_, label=label4_, linewidth=3.00,
            marker='*', markersize=4, markerfacecolor="orange", color="green")
    ax.plot(np.linspace(0.02, (len(y_val5_) * 0.02), len(y_val5_)), y_val5_, label=label5_, linewidth=3.00,
            marker='o', markersize=4, markerfacecolor="black", color="purple")
    ax.plot(np.linspace(0.02, (len(y_val6_) * 0.02), len(y_val6_)), y_val6_, label=label6_, linewidth=3.00,
            marker='s', markersize=4, markerfacecolor="black", color="gray")
    ax.plot(np.linspace(0.02, (len(y_val7_) * 0.02), len(y_val7_)), y_val7_, label=label7_, linewidth=3.00,
            marker='s', markersize=4, markerfacecolor="black", color="orange")
    ax.set_ylim(ymin=10)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("average packet latency")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "sweepTraffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_) + "rot-" + str(rot_)
    # stri = "sweepTraffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    fig.savefig("DRAIN-period_sweep_plots_13_03_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()

def plot18_line_graph_sweep(injr, y_val1_, label1_, y_val2_, label2_, y_val3_, label3_,
                            y_val4_, label4_, y_val5_, label5_, y_val6_, label6_,
                            y_val7_, label7_, y_val8_, label8_, y_val9_, label9_,
                            y_val10_, label10_, y_val11_, label11_, y_val12_, label12_,
                            y_val13_, label13_, y_val14_, label14_, y_val15_, label15_,
                            y_val16_, label16_, y_val17_, label17_, y_val18_, label18_,
                            vc_, traffic_, fault_, rot_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    # print "y_val4_: ", y_val4_

    fig, ax = subplots()
    ###### Fault-16 ######
    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_, label=label1_,
            linewidth=3.00, ls='-', color="blue")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_, label=label2_,
            linewidth=3.00, ls=':', color="blue")
    ax.plot(np.linspace(0.02, (len(y_val3_) * 0.02), len(y_val3_)), y_val3_, label=label3_,
            linewidth=3.00, ls='-.', color="blue")

    ###### Fault-64 ######
    ax.plot(np.linspace(0.02, (len(y_val4_) * 0.02), len(y_val4_)), y_val4_, label=label4_,
            linewidth=3.00, ls='-', color="red")
    ax.plot(np.linspace(0.02, (len(y_val5_) * 0.02), len(y_val5_)), y_val5_, label=label5_,
            linewidth=3.00, ls=':', color="red")
    ax.plot(np.linspace(0.02, (len(y_val6_) * 0.02), len(y_val6_)), y_val6_, label=label6_,
            linewidth=3.00, ls='-.', color="red")

    ###### Fault-128 ######
    ax.plot(np.linspace(0.02, (len(y_val7_) * 0.02), len(y_val7_)), y_val7_, label=label7_,
            linewidth=3.00, ls='-', color="black")
    ax.plot(np.linspace(0.02, (len(y_val8_) * 0.02), len(y_val8_)), y_val8_, label=label8_,
            linewidth=3.00, ls=':', color="black")
    ax.plot(np.linspace(0.02, (len(y_val9_) * 0.02), len(y_val9_)), y_val9_, label=label9_,
            linewidth=3.00, ls='-.', color="black")

    ###### Fault-1024 ######
    ax.plot(np.linspace(0.02, (len(y_val10_) * 0.02), len(y_val10_)), y_val10_, label=label10_,
            linewidth=3.00, ls='-', color="green")
    ax.plot(np.linspace(0.02, (len(y_val11_) * 0.02), len(y_val11_)), y_val11_, label=label11_,
            linewidth=3.00, ls=':', color="green")
    ax.plot(np.linspace(0.02, (len(y_val12_) * 0.02), len(y_val12_)), y_val12_, label=label12_,
            linewidth=3.00, ls='-.', color="green")

    ###### Fault-4096 ######
    ax.plot(np.linspace(0.02, (len(y_val13_) * 0.02), len(y_val13_)), y_val13_, label=label13_,
            linewidth=3.00, ls='-', color="purple")
    ax.plot(np.linspace(0.02, (len(y_val14_) * 0.02), len(y_val14_)), y_val14_, label=label14_,
            linewidth=3.00, ls=':', color="purple")
    ax.plot(np.linspace(0.02, (len(y_val15_) * 0.02), len(y_val15_)), y_val15_, label=label15_,
            linewidth=3.00, ls='-.', color="purple")

    ###### Fault-65536 ######
    ax.plot(np.linspace(0.02, (len(y_val16_) * 0.02), len(y_val16_)), y_val16_, label=label16_,
            linewidth=3.00, ls='-', color="gray")
    ax.plot(np.linspace(0.02, (len(y_val17_) * 0.02), len(y_val17_)), y_val17_, label=label17_,
            linewidth=3.00, ls=':', color="gray")
    ax.plot(np.linspace(0.02, (len(y_val18_) * 0.02), len(y_val18_)), y_val18_, label=label18_,
            linewidth=3.00, ls='-.', color="gray")

    ####### patch #######
    if len(y_val1_) == 0:
        y_val1_.append(0)
    if len(y_val2_) == 0:
        y_val2_.append(0)
    if len(y_val3_) == 0:
        y_val3_.append(0)
    if len(y_val4_) == 0:
        y_val4_.append(0)
    if len(y_val5_) == 0:
        y_val5_.append(0)
    if len(y_val6_) == 0:
        y_val6_.append(0)
    if len(y_val7_) == 0:
        y_val7_.append(0)
    if len(y_val8_) == 0:
        y_val8_.append(0)
    if len(y_val9_) == 0:
        y_val9_.append(0)
    if len(y_val10_) == 0:
        y_val10_.append(0)
    if len(y_val11_) == 0:
        y_val11_.append(0)
    if len(y_val12_) == 0:
        y_val12_.append(0)
    if len(y_val13_) == 0:
        y_val13_.append(0)
    if len(y_val14_) == 0:
        y_val14_.append(0)
    if len(y_val15_) == 0:
        y_val15_.append(0)
    if len(y_val16_) == 0:
        y_val16_.append(0)
    if len(y_val17_) == 0:
        y_val17_.append(0)
    if len(y_val18_) == 0:
        y_val18_.append(0)

    ax.set_ylim(ymin=min(min(y_val1_), min(y_val2_), min(y_val3_), min(y_val4_), min(y_val5_), min(y_val6_),
                         min(y_val7_), min(y_val8_), min(y_val9_), min(y_val10_), min(y_val11_), min(y_val12_),
                         min(y_val13_), min(y_val14_), min(y_val15_), min(y_val16_), min(y_val17_), min(y_val18_)) - 5)
    max1 = max(max(y_val1_), max(y_val2_), max(y_val3_), max(y_val4_), max(y_val5_), max(y_val6_),
                         max(y_val7_), max(y_val8_), max(y_val9_), max(y_val10_), max(y_val11_), max(y_val12_),
                         max(y_val13_), max(y_val14_), max(y_val15_), max(y_val16_), max(y_val17_), max(y_val18_)) + 5
    max2 = 8000

    ax.set_ylim(ymax=min(max1, max2))
    # ax.set_ylim(ymax=100)
    # ax.set_ylim(ymin=10)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    # ax.set_ylabel("average bubble movement per drain")
    # ax.set_ylabel("packets received/cycle/node")
    # ax.set_ylabel("average packet latency")
    # ax.set_ylabel("total spins")
    # ax.set_ylabel("average fwd progress of flits per drain")
    # ax.set_ylabel("average mis-route of flits per drain")
    ax.set_ylabel("average bubble movement per drain")
    # ax.legend(loc=4)
    # ax.legend(loc=0, prop={'size': 12})

    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width * 0.6, chartBox.height])
    ax.legend(loc='upper right', prop={'size': 11},
              bbox_to_anchor=(1.45, 0.96), shadow=True, ncol=1)

    stri = "bubbleMovement-sweep-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    # fig.savefig("bubbleMovement_sweep_plots_03_07_2019/" + str(stri) + ".png")
    fig.savefig("bubbleMovement_sweep_plots_03_07_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()

def plot1_line_graph(y_val1, vc_, traffic_, fault_):
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    fig, ax = subplots()
    ax.plot(np.linspace(0.02, (len(y_val1) * 0.02), len(y_val1)), y_val1, linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="grey", color="black")
    ax.set_ylim(ymin=min(y_val1)-5)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("average packet latency")
    ax.legend(loc=4)

    title_ = "spin-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(title_)
    file_name = title_
    # file_name = "plots/" + title_ + ".png"
    # file_name = "eVC_lat_plot_05_03_2019/" + title_ + ".png"
    # file_name = "spin_lat_plot_05_03_2019/" + title_ + ".png"
    fig.savefig(file_name)


def plot6_scatter_graph(y_val1_, y_val2_, y_val3_, y_val4_, y_val5_,
                        y_val6_, vc_, traffic_, fault_, limit):
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    fig, ax = subplots()

    ax.scatter(y_val1_, y_val1_, s=100, label="escapeVC(rr)", marker='+', color="blue")
    ax.scatter(y_val2_, y_val2_, s=100, label="escapeVC(fcfs)", marker='.', color="red")
    ax.scatter(y_val3_, y_val3_, s=100, label="SPIN-128", marker='*', color="black")
    ax.scatter(y_val4_, y_val4_, s=100, label="SPIN-1024", marker='x', color="green")
    ax.scatter(y_val5_, y_val5_, s=100, label="DRAIN-128", marker='o', color="purple")
    ax.scatter(y_val6_, y_val6_, s=100, label="DRAIN-1024", marker='^', color="gray")

    ax.set_ylim(ymin=0.02)
    ax.set_ylim(ymax=limit + 0.02)
    ax.set_xlim(xmin=0.02)
    ax.set_xlim(xmax=limit + 0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("saturation-throughput (packets received/cycle/node)")
    ax.legend(loc=2, prop={'size': 12})

    stri = "scatterPlot-Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    fig.savefig("scatter_plots_28_02_2019/" + str(stri) + ".png")


def plot6_bar_graph(variance_, vc_, traffic_, fault_):

    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    schemes_ = ('escapeVC(rr)', 'escapeVC(fcfs)', 'DRAIN-128',
                'DRAIN-1024', 'SPIN-128', 'SPIN-1024')
    y_pos = np.arange(len(schemes_))


    fig, ax = subplots()

    plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.20,
                        bottom=0.24, right=0.96, top=0.90)

    ax.bar(y_pos, variance_, align='center', alpha=0.5)

    plt.xticks(y_pos, schemes_, rotation=45) # this is important

    # ax.set_xlabel("Schemes")
    ax.set_ylabel("Variance in saturation throughput")
    ax.legend(loc=0, prop={'size': 12})

    stri = "barPlot-Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    fig.savefig("bar_plots_28_02_2019/" + str(stri) + ".png")


def plot6_bar_sweep_graph(variance_, vc_, traffic_, fault_, rot_):

    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    schemes_ = ('DRAIN-16', 'DRAIN-64', 'DRAIN-128',
                'DRAIN-1024', 'DRAIN-4096', 'DRAIN-65536')
    y_pos = np.arange(len(schemes_))


    fig, ax = subplots()

    plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.20,
                        bottom=0.28, right=0.90, top=0.90)

    ax.bar(y_pos, variance_, align='center', alpha=0.5)

    plt.xticks(y_pos, schemes_, rotation=65) # this is important

    # ax.set_xlabel("Schemes")
    ax.set_ylabel("Variance in saturation throughput")
    ax.legend(loc=0, prop={'size': 12})

    stri = "Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_) + "rot-" + str(rot_)
    ax.set_title(stri)
    # fig.savefig(str(stri) + ".png")
    fig.savefig("sweep_bar_plots_04_03_2019/" + str(stri) + ".png")

def stackedBarPlot(bubble_movement, routed_pkt, mis_routed_pkt, vc_, traffic_, fault_, rot_, period_):

    raw_data = {'bubble_movement': bubble_movement, 'routed_pkt': routed_pkt, 'mis_routed_pkt': mis_routed_pkt}
    df = pd.DataFrame(raw_data)

    fig, ax = subplots()
    # From raw value to percentage
    totals = [i + j + k for i, j, k in zip(df['bubble_movement'], df['routed_pkt'], df['mis_routed_pkt'])]
    bubble_movement = [i / j * 100 for i, j in zip(df['bubble_movement'], totals)]
    routed_pkt = [i / j * 100 for i, j in zip(df['routed_pkt'], totals)]
    mis_routed_pkt = [i / j * 100 for i, j in zip(df['mis_routed_pkt'], totals)]

    # plot
    barWidth = 0.85

    # Create green Bars
    ax.bar(np.linspace(0.02, (len(bubble_movement) * 0.02), len(bubble_movement)), bubble_movement,
            width=0.2 / len(bubble_movement), color='#b5ffb9', edgecolor='white', label="bubble_movement",
           align="center")
    # Create orange Bars
    ax.bar(np.linspace(0.02, (len(routed_pkt) * 0.02), len(routed_pkt)), routed_pkt, bottom=bubble_movement,
            width=0.2 / len(routed_pkt), color='#f9bc86', edgecolor='white', label="routed_pkt", align="center")
    # Create blue Bars
    ax.bar(np.linspace(0.02, (len(mis_routed_pkt) * 0.02), len(mis_routed_pkt)), mis_routed_pkt,
            width=0.2 / len(mis_routed_pkt), bottom=[i + j for i, j in zip(bubble_movement, routed_pkt)],
           color='#a3acff', edgecolor='white', label="mis_routed_pkt", align="center")

    ax.set_ylim(ymax=120)
    # Custom x axis
    # plt.xticks(r, names)
    # np.set_printoptions(formatter={'float_kind': float_formatter})
    xlabels_positions = np.linspace(0.02, (len(bubble_movement) * 0.02), len(bubble_movement))

    print xlabels_positions

    ax.set_xticks(xlabels_positions)
    xtick_labels = [ "0.02", "0.04", "0.06", "0.08",
                     "0.10", "0.12", "0.14", "0.16",
                     "0.18", "0.20", "0.22", "0.24",
                     "0.26", "0.28", "0.30", "0.32",
                     "0.34", "0.34", "0.36", "0.38",
                     "0.40", "0.42", "0.44", "0.46"]
    ax.set_xticklabels(xtick_labels[:len(bubble_movement)], rotation=45)
    ax.set_xlabel("injection rates")
    stri = "Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_) + "rot-" + str(rot_) + \
           "period-" + str(period_)

    ax.set_title(stri)
    ############
    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width * 1.0, chartBox.height])
    ax.legend(loc='upper right', prop={'size': 11},
              bbox_to_anchor=(0.95, 0.97), shadow=True, ncol=3)
    ############
    # ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
    # fig.savefig("tmp.png")
    fig.savefig("stackBarPlot_03_19_2019/" + str(stri) + ".png")
    # Show graphic
    # plt.show()
