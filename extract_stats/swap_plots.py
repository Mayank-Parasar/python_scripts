# libraries
# import matplotlib as mpl

# mpl.use('Agg')

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# color codes (in Hex)
#  332288, 88CCEE, 44AA99, 117733, 999933, DDCC77, CC6677, 882255, AA4499

def plot5_line_graph(label1_, y_val1_, label2_, y_val2_,
                     label3_, y_val3_, label4_, y_val4_,
                     label5_, y_val5_, vc_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 18, 'font.family': 'serif', 'font.weight': 'bold'})

    fig, ax = subplots()

    ax.plot(np.linspace(0.02, 0.40, 21), y_val1_[:21], label=label1_,
            linewidth=4.00, ls='-', markersize=4, markerfacecolor="blue", color="#332288")
    ax.plot(np.linspace(0.02, 0.40, 21), y_val2_[:21], label=label2_,
            linewidth=4.00, ls='-', markersize=4, markerfacecolor="red", color="red")
    ax.plot(np.linspace(0.02, 0.40, 21), y_val3_[:21], label=label3_,
            linewidth=4.00, ls='-', marker='*', markersize=4, markerfacecolor="red", color="black")
    ax.plot(np.linspace(0.02, 0.40, 21), y_val4_[:21], label=label4_,
            linewidth=4.00, ls='-', marker='*', markersize=4, markerfacecolor="orange", color="green")
    ax.plot(np.linspace(0.02, 0.40, 21), y_val5_[:21], label=label5_,
            linewidth=4.00, ls='-', marker='o', markersize=4, markerfacecolor="black", color="purple")
    ax.set_ylim(ymin=0)
    ax.set_ylim(ymax=100)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)", fontweight='bold')
    ax.set_ylabel("average packet latency", fontweight='bold')
    # ax.legend(loc=0, prop={'size': 12})
    fig.show()

def plot5_overhead_line_graph(label1_, y_val1_, label2_, y_val2_,
                     label3_, y_val3_, label4_, y_val4_,
                     label5_, y_val5_, vc_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 18, 'font.family': 'serif', 'font.weight': 'bold'})

    fig, ax = subplots()

    ax.plot(np.linspace(0.02, 0.70, 35), y_val1_[:35], label=label1_,
            linewidth=4.00, ls='-', markersize=4, markerfacecolor="blue", color="red")
    ax.plot(np.linspace(0.02, 0.70, 35), y_val2_[:35], label=label2_,
            linewidth=4.00, ls='-', markersize=4, markerfacecolor="red", color="orange")
    ax.plot(np.linspace(0.02, 0.70, 35), y_val3_[:35], label=label3_,
            linewidth=4.00, ls='-', marker='*', markersize=4, markerfacecolor="red", color="green")
    ax.plot(np.linspace(0.02, 0.70, 35), y_val4_[:35], label=label4_,
            linewidth=4.00, ls='-', marker='*', markersize=4, markerfacecolor="orange", color="blue")
    ax.plot(np.linspace(0.02, 0.70, 35), y_val5_[:35], label=label5_,
            linewidth=4.00, ls='-', marker='o', markersize=4, markerfacecolor="black", color="purple")

    ax.set_ylim(ymin=1.5, ymax=max(max(y_val1_[:35]), max(y_val2_[:35]), max(y_val3_[:35]), max(y_val4_[:35]),
                                   max(y_val5_[:35]) + 0.2))
    # ax.set_ylim(ymax=3.2)
    ax.set_xlim(xmin=0.02)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)", fontweight='bold')
    ax.set_ylabel("Reception rate (packets received/cycle)", fontweight='bold')
    # ax.legend(loc=0, prop={'size': 12})
    fig.show()

def plot3_line_graph(label1_, y_val1_, label2_, y_val2_,
                     label3_, y_val3_, vc_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 18, 'font.family': 'serif', 'font.weight': 'bold'})

    fig, ax = subplots()
    x_val = ["sc-1", "sc-2", "sc-4", "sc-8", "sc-16", "sc-32", "sc-64", "sc-128",
             "sc-256", "sc-512", "sc-1024", "sc-1536", "sc-2048"]
    ax.plot(x_val, y_val1_, label=label1_,
            linewidth=6.00, ls='-', markersize=4, markerfacecolor="blue", color="red")
    ax.plot(x_val, y_val2_, label=label2_,
            linewidth=6.00, ls='-', markersize=4, markerfacecolor="red", color="orange")
    ax.plot(x_val, y_val3_, label=label3_,
            linewidth=6.00, ls='-', marker='*', markersize=4, markerfacecolor="red", color="green")

    ax.set_ylim(ymin=0, ymax=max(max(y_val1_), max(y_val2_), max(y_val3_) + 0.05))
    # ax.set_ylim(ymax=3.2)
    # ax.set_xlim(xmin=0.02)
    plt.xticks(rotation=30)
    # ax.set_xlabel("Injection-rate (packets injected/node/cycle)", fontweight='bold')
    ax.set_ylabel("Total number of bailOut per cycle", fontweight='bold')
    # ax.legend(loc=0, prop={'size': 12})
    fig.show()


def plot9_line_graph(label1_, y_val1_, label2_, y_val2_,
                     label3_, y_val3_, label4_, y_val4_,
                     label5_, y_val5_, label6_, y_val6_,
                     label7_, y_val7_, label8_, y_val8_,
                     label9_, y_val9_, vc_, traffic_):
    # Update the matplotlib configuration parameters:
    plt.rcParams.update({'font.size': 18, 'font.family': 'serif', 'font.weight': 'bold'})

    fig, ax = subplots()

    ax.plot(np.linspace(0.02, (len(y_val1_) * 0.02), len(y_val1_)), y_val1_, label=label1_,
            linewidth=4.00, ls='-', color="#332288")
    ax.plot(np.linspace(0.02, (len(y_val2_) * 0.02), len(y_val2_)), y_val2_, label=label2_,
            linewidth=4.00, ls='-', color="#88CCEE")
    ax.plot(np.linspace(0.02, (len(y_val3_) * 0.02), len(y_val3_)), y_val3_, label=label3_,
            linewidth=4.00, ls='-', color="#44AA99")
    ax.plot(np.linspace(0.02, (len(y_val4_) * 0.02), len(y_val4_)), y_val4_, label=label4_,
            linewidth=4.00, ls='-', color="#117733")
    ax.plot(np.linspace(0.02, (len(y_val5_) * 0.02), len(y_val5_)), y_val5_, label=label5_,
            linewidth=4.00, ls='-', color="#999933")
    ax.plot(np.linspace(0.02, (len(y_val6_) * 0.02), len(y_val6_)), y_val6_, label=label6_,
            linewidth=4.00, ls='-', color="#DDCC77")
    ax.plot(np.linspace(0.02, (len(y_val7_) * 0.02), len(y_val7_)), y_val7_, label=label7_,
            linewidth=4.00, ls='-', color="#CC6677")
    ax.plot(np.linspace(0.02, (len(y_val8_) * 0.02), len(y_val8_)), y_val8_, label=label8_,
            linewidth=4.00, ls='-', color="#882255")
    ax.plot(np.linspace(0.02, (len(y_val9_) * 0.02), len(y_val9_)), y_val9_, label=label9_,
            linewidth=4.00, ls='-', color="#AA4499")
    ax.set_ylim(ymin=10)
    ax.set_ylim(ymax=70)
    ax.set_xlim(xmin=0.02, xmax=0.26)
    ax.set_xlabel("Injection-rate (packets injected/node/cycle)", fontweight='bold')
    ax.set_ylabel("average packet latency", fontweight='bold')
    # ax.legend(loc=0, prop={'size': 12})
    ax.set_title("VC-"+str(vc_) + " " + traffic_)
    fig.show()

if __name__ == '__main__':
    # list-1
    low_inj = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    med_inj = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    high_inj = [0.179184, 0.086948, 0.045211, 0.02293, 0.011178, 0.005615, 0.002665, 0.0013, 0.000619, 0.000252, 0.000102, 0.000056, 0.000046]
    plot3_line_graph("low_inj", low_inj, "med_inj", med_inj, "high_inj", high_inj, 4)
    # plot9_line_graph("WestFirst", WestFirst, "escapeVC", escapeVC, "Chipper", Chipper, "MinBD", MinBD, "StaticBubble",
    #                  StaticBubble, "SPIN", SPIN, "sc-1", sc_1, "sc-64", sc_64, "sc-1024", sc_1024, 3, "BitReverse")

