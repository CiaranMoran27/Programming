# This program reads in a percent result from user and check what Grade it is
# Author: Ciaran Moran

percentage = float(input("What percentage did you get?"))

if percentage < 0 or percentage > 100:
    print("This is not a valid percentage, enter a number between 1 and 100")

# use of nested if statements that only run if percentage is between 1 and 100
else: 
    if percentage <40:
        print("Fail")
    elif percentage <50:
        print("Pass")
    elif percentage <60:
        print("Merit1")
    elif percentage <70:
        print("Merit2")
    else:
        print("Distinction")