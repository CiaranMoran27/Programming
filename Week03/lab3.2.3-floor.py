#This program takes a user input as a float and rounds it down to the nearest integer 
# Author: Ciaran Moran
import math

numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))