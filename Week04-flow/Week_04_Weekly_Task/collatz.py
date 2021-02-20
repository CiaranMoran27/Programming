# collatz.py
# The program asks the user for a positive integer and outputs successive values 
# based on if the input number is odd or even. The progam ends if 1 is entered.
# Author: Ciaran Moran

numberList = []

number = input("Enter a number: ")

while True:
    try:
        numberInt = int(number)  # Convert to float check (string etc...)
  
    except ValueError:
        input("Enter a Enter a whole number: ")


numberInt = int(number)
while True:
    if numberInt< 0:
        input("Enter a Enter a positive number: ")




    #if numberInt < 0:
        #input("Enter a Enter a positive number: ")


#numberInt = int(number)

'''
while numberInt!=1:         # stops proceeding calculation at 1
    if numberInt % 2 == 0:  # check if number is even
        numberInt = numberInt // 2  
    else:
        numberInt = (numberInt * 3) + 1  # check if number is odd
    numberList.append(numberInt)


        
# References: 
# 1. Real Python, 2021, 8.3 Handling exceptions, viewed 19 Feb 2021,<https://docs.python.org/3/tutorial/errors.html>.
# 2. Cunningham, P, 2014, Check if input is positive integer, viewed 19 Feb 2021, <https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer>.
# 3. Programiz, 2021, What is the use of break and continue in Python?, viewed 19 Feb 2021,<https://www.programiz.com/python-programming/break-continue>.  
'''