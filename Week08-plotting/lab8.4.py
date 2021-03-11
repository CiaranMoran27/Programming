#Modify the program so that it increases all the salaries by 5% (store in anotherarray).

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)    # this is so that the "random" numbers are the same each time t

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
salariesMult = salaries *1.05
newSalaries = salariesMult.astype(int)


print(salaries)
print(salariesMult)
print(newSalaries)