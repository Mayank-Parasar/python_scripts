# libraries
import matplotlib as mpl

mpl.use('Agg')

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# Data
def stackedBarPlot(bubble_movement, routed_pkt, mis_routed_pkt):
        r = [0, 1, 2, 3, 4]
        # raw_data = {'bubble_movement': [20, 1.5, 7, 10, 5], 'routed_pkt': [5, 15, 5, 10, 15], 'mis_routed_pkt': [2, 15, 18, 5, 10]}
        # bubble_movement = bubble_movement[:5]
        # routed_pkt = routed_pkt[:5]
        # mis_routed_pkt = mis_routed_pkt[:5]
        raw_data = {'bubble_movement': bubble_movement, 'routed_pkt': routed_pkt, 'mis_routed_pkt': mis_routed_pkt}
        df = pd.DataFrame(raw_data)

        # From raw value to percentage
        totals = [i + j + k for i, j, k in zip(df['bubble_movement'], df['routed_pkt'], df['mis_routed_pkt'])]
        bubble_movement = [i / j * 100 for i, j in zip(df['bubble_movement'], totals)]
        routed_pkt = [i / j * 100 for i, j in zip(df['routed_pkt'], totals)]
        mis_routed_pkt = [i / j * 100 for i, j in zip(df['mis_routed_pkt'], totals)]

        # plot
        barWidth = 0.85
        names = ('A', 'B', 'C', 'D', 'E')
        # Create green Bars
        plt.bar(np.linspace(0.02, (len(bubble_movement) * 0.02), len(bubble_movement)), bubble_movement, width=0.2/len(bubble_movement),
                color='#b5ffb9', edgecolor='white')
        # Create orange Bars
        plt.bar(np.linspace(0.02, (len(routed_pkt) * 0.02), len(routed_pkt)), routed_pkt, bottom=bubble_movement, width=0.2/len(routed_pkt),
                color='#f9bc86', edgecolor='white')
        # Create blue Bars
        plt.bar(np.linspace(0.02, (len(mis_routed_pkt) * 0.02), len(mis_routed_pkt)), mis_routed_pkt, width=0.2/len(mis_routed_pkt),
                bottom=[i + j for i, j in zip(bubble_movement, routed_pkt)], color='#a3acff', edgecolor='white')

        # Custom x axis
        # plt.xticks(r, names)
        plt.xlabel("injection rates")

        plt.savefig("tmp.png")
        # Show graphic
        plt.show()
