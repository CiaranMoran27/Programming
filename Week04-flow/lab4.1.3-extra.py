# Method 1: Employed below, addition of round() function to percentage which will round 69.5 to 70
# Method 2: Not used, import math module and use math.ceil() function will round up decimal values
# Author: Ciaran Moran

percentage = round(float(input("What percentage did you get?")))

if percentage < 0 or percentage > 100:
    print("This is not a valid percentage, enter a number between 1 and 100")


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