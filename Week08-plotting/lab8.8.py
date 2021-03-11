# Add a line to this plot from lab8.7.py that shows y= x2 in a different colour.

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000

minAges = 21
maxAges = 65
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(minAges,maxAges,numberOfEntries)
plt.scatter(ages,salaries)


#plt.show() # if you do this the proram will halt here until the plot is closed add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself
plt.plot(xpoints, ypoints, color= 'r')
plt.show() 