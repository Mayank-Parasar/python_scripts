import matplotlib as mpl

mpl.use('Agg')

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

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

def plot3_line_graph_sweep(injr, y_val1_, y_val2_, y_val3_, vc_, traffic_, fault_, rot_, freq_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(injr, y_val1_, label="Rot-1", linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="blue", color="blue")
    ax.plot(injr, y_val2_, label="ROT-4", linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="red", color="red")
    ax.plot(injr, y_val3_, label="ROT-8", linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="red", color="black")
    ax.set_ylim(ymin = min(min(y_val1_), min(y_val2_), min(y_val3_)) - 2)
    ax.set_ylim(ymax = 100)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("packets received/cycle/node")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "RotSweep-" + str(traffic_) + "VC-" + str(vc_) + \
           "fault-" + str(fault_) + "rot-" + str(rot_) + "freq-" + str(freq_)
    ax.set_title(stri)
    # fig.savefig("simType1_sweep_plots_04_03_2019/" + str(stri) + ".png")
    fig.savefig(str(stri) + ".png")
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

def plot6_line_graph_sweep(injr, y_val1_, y_val2_, y_val3_, y_val4_, y_val5_,
                     y_val6_, vc_, traffic_, fault_, rot_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    ax.plot(injr, y_val1_, label="DRAIN-16", linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="blue", color="blue")
    ax.plot(injr, y_val2_, label="DRAIN-64", linewidth=3.00, ls='-', markersize=4,
            markerfacecolor="red", color="red")
    ax.plot(injr, y_val3_, label="DRAIN-128", linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="red", color="black")
    ax.plot(injr, y_val4_, label="DRAIN-1024", linewidth=3.00, ls='-', marker='*', markersize=4,
            markerfacecolor="orange", color="green")
    ax.plot(injr, y_val5_, label="DRAIN-4096", linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="black", color="purple")
    ax.plot(injr, y_val6_, label="DRAIN-65536", linewidth=3.00, ls='-', marker='o', markersize=4,
            markerfacecolor="black", color="gray")
    ax.set_ylim(ymin=0.02)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)")
    ax.set_ylabel("packets received/cycle/node")
    # ax.legend(loc=4)
    ax.legend(loc=0, prop={'size': 12})

    stri = "sweepTraffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_) + "rot-" + str(rot_)
    ax.set_title(stri)
    fig.savefig("simType1_sweep_plots_04_03_2019/" + str(stri) + ".png")
    # fig.savefig(str(stri) + ".png")
    # fig.show()

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
