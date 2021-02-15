# This program asks the user for a number and tells the user if its an odd or even number.
# Author: Ciaran Moran

number =int(input("Enter a number: "))

if number%2 ==0:
    print(str(number) + " is an even number")
else:
    print(str(number) + " is an odd number")