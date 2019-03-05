import matplotlib as mpl

mpl.use('Agg')

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

def plot6_bar_graph(variance_, vc_, traffic_, fault_):
    schemes_ = ('escapeVC(rr)', 'escapeVC(fcfs)', 'DRAIN-128',
                'DRAIN-1024', 'SPIN-128', 'SPIN-1024')
    y_pos = np.arange(len(schemes_))

    plt.rcParams.update({'font.size': 16, 'font.family': 'serif'})

    fig, ax = subplots()
    plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.20,
                        bottom=0.24, right=0.96, top=0.90)

    ax.bar(y_pos, variance_, align='center', alpha=0.5)

    plt.xticks(y_pos, schemes_, rotation=45) # this is important

    # ax.set_xlabel("Schemes")
    ax.set_ylabel("variance in saturation throughput")
    ax.legend(loc=0, prop={'size': 12})

    stri = "barPlot-Traffic-" + str(traffic_) + "VC-" + str(vc_) + "fault-" + str(fault_)
    ax.set_title(stri)
    fig.savefig(str(stri) + ".png")


var_ = [0.00000000e+00,   0.00000000e+00,   9.87654321e-05,   6.91358025e-05,
        2.44000000e-04,   2.44000000e-04]
plot6_bar_graph(var_, 2, "transpose", 8)
