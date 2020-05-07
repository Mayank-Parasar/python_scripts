# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25

# set height of bar
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
print "r1: ", r1
r2 = [x + barWidth for x in r1]
print "r2: ", r2
r3 = [x + barWidth for x in r2]
print "r3: ", r3

# Make the plot
plt.bar(r1, bars1, alpha=0.5, color='#EE3224', width=barWidth, edgecolor='white', label='var1')
plt.bar(r2, bars2, alpha=0.5, color='#F78F1E', width=barWidth, edgecolor='white', label='var2')
plt.bar(r3, bars3, alpha=0.5, color='#FFC222', width=barWidth, edgecolor='white', label='var3')

# Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
print [r + barWidth for r in range(len(bars1))]
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])

# Create legend & Show graphic
plt.legend()
plt.show()
