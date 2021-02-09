# Author: Ciaran Moran
# This program prints out a random fruit
import random

fruits = ('Pineapple', 'Orange', 'Banana', 'Apple')

# Generates a random index number between Index  0 and -1 of tuple
# Uses the randomly generated number to index the fruits tuple and store the answer in "fruit" variable
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]

print("A Random Fruit:{}".format(fruit))