# This program generates 10 random numbers, prints them out, then prints out the top 3
# Author: Ciaran Moran

import random

#set variables
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100

# generate list and populate with random numbers from 0 - 100
numbers = []
for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))
print ("{} random numbers\t {}".format(howMany,numbers))


# sorts number list in Descending order & prints the first 3 list entries [1]/
numbers.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,numbers[0:topHowMany]))



#Reference:
#1 .Programiz. 2020. Python List sort(). [online] Available at: https://www.programiz.com/python-programming/methods/list/sort/ [Accessed 10 February 2021].


