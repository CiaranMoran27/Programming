#Write a program that makes a list called ages that has, the same number random
#values as salaries, (range:21 to 65) . Make scatter plot of this data


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
plt.show()
