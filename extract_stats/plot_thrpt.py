import matplotlib as mpl

mpl.use('Agg')

from pylab import *
import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
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
    stri = traffic_ + " ( VC-" + str(vc_) + " )"

    # x0, xmax = plt.xlim()
    # y0, ymax = plt.ylim()
    # print xmax
    # print ymax
    # ax.text(0.15, 0.030, stri, fontsize=20, color="black")
    # ax.text(xmax / 4, ymax / 2, stri, fontsize=20, color="black")
    # ax.set_title(stri)
    ax.set_title(title_)
    # file_name="irregular_fig/"+traffic_+"_VC-"+str(vc_)+".png"
    file_name = "irregular_fig/" + title_ + ".png"
    fig.savefig(file_name)
    # fig.show()


def plot5_line_graph(injr, y_val1_, y_val2_, y_val3_, y_val4_, y_val5_, vc_, traffic_, fault_):
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
    ax.plot(injr, y_val5_, label="DRAIN-1024", linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="black", color="purple")
    ax.set_ylim(ymin=0.02)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("packets received/cycle/node")
    # ax.legend(loc=4)
    ax.legend(loc=4, prop={'size': 12})

    stri = "Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    # fig.savefig("plots_23_02_2019/" + str(stri) + ".png")
    fig.savefig(str(stri) + ".png")
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
    ax.set_ylabel("packets received/cycle/node")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    fig.savefig("plots_25_02_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()

def plot1_line_graph(injr, y_val1, title_):
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})
    fig, ax = subplots()
    ax.plot(injr, y_val1, linewidth=2.00, ls='-', marker='o', markersize=4,
            markerfacecolor="blue")
    ax.set_ylim(ymin=0.02)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("packets received/cycle/node")
    ax.legend(loc=4)

    ax.set_title(title_)
    file_name = "plots/" + title_ + ".png"
    fig.savefig(file_name)
