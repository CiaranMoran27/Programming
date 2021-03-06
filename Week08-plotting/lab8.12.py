#Modify the program to make bar chart of the counties.


import matplotlib.pyplot as plt
import numpy as np

countryList = ['Ireland','England','France','Spain','Turkey']

counties = np.random.choice(countryList ,p=[0.1, 0.3, 0.2, 0.12, 0.28 ],size=(100))

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear

unique, counts = np.unique(counties, return_counts=True)


# same above except
plt.bar(unique, counts)
plt.show()

