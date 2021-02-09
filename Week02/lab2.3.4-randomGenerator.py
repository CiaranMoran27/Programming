# Program that asks user for Min and Max number and then prints out a random number between the user range selected
# Author: Ciaran Moran

import random

#user inputs (Min and Max)
print('Select a Minimum and a Maximum number')
min = int(input('Enter Min Number: '))
max = int(input('Enter Max Number: '))


#check if Min number entered is greater than Max number entered, if True print warning message 
if min > max:
    print("Warning: The Minimum number must be less than the Maximum number")

else:
    #Generate and print random number between user selected range
    number = random.randrange(min,max)
    print("Random Number = {}".format(number))  