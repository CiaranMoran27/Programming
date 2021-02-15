# This program is a modified version of lab4.1.1 which the user for a number and tells the user if its an odd or even number.
# This program continues to ask the user for a number until they enter -1 
# Author: Ciaran Moran

#initialise condition variable
number =int(input("Enter a number: "))

#use of Sentinal controlled While loop
while number !=-1:
    if number%2 ==0:
        print(str(number) + " is an even number")
    else:
        print(str(number) + " is an odd number")
    #change conditional variable
    number =int(input("Enter a number (-1 to quit): "))