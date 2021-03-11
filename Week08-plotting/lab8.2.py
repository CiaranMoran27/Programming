#Modify the program so that the “random” salaries are the same each time the
#program is run, to make the program easier to test, ie “seed” the random number
#generator. 

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)    # this is so that the "random" numbers are the same each time t

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)


