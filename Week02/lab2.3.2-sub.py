# Program that subtracts one number from another
# Author: Ciaran Moran

#input reads in a string which is converting to type(int) to allow a mathematical operation
x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))

answer = x - y
print('{} - {} = {}'.format(x,y,answer))

#Extra: when the program is running, try entering in something that is not an int
#Answer: ValueError: invalid literal for int(), one would have to convert the data type to int or float to allow maths operation