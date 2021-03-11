import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

Mean, stdDev = 0, 0.1 # mean and standard deviation
s = np.random.normal(Mean, stdDev, 1000)

abs(Mean - np.mean(s))
0.0  

abs(stdDev - np.std(s, ddof=1))
0.1 


count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(stdDev * np.sqrt(2 * np.pi)) *np.exp( - (bins - Mean)**2 / (2 * Mean**2) ),linewidth=2, color='r')
plt.show()

# ref: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html