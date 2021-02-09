# Program that read in two numbers and outputs the integer answer and the remainder
# Author: Ciaran Moran

#input read in a string which is converting to type(int) to allow a mathematical operation
x = int(input('Enter First Number: '))
y = int(input('Enter Number you want to divide by: '))

# // operator performs  division giving result as a rounded down integer
# % operator gives the remainder
answer = int(x // y)
remainder = x % y

print('{} divided by {} is {} with remainder of {}'.format(x,y,answer,remainder))