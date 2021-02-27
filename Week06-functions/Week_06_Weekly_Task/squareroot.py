# squareroot.py
# The program asks the user for a positive floatint-point number and outputs an approx. square root. 
# based on if the input number is odd or even. The progam ends if 1 is entered.
# Author: Ciaran Moran


def userValidation():
    
    while True:
        number = input("Please enter a positive number: ")
        try:

            numberFloat = float(number)  # try convert number variable to float
            if numberFloat < 0:          # checks the float is positive
                continue                    # jump back to start of while loop            
            else:
                sqrt(numberFloat)           # pass float into sqrt function
                break                       # exit loop 
                        
                
        except ValueError:            # if error raised between try and except statement:  
            continue                     # jump back to start of while loop


def sqrt(numberFloat,tolerance = 0.000001):
    estimate = numberFloat                          # initial estimate
    diff = 9999999999                               # diff is used as a limit, that when exceeded the while loop ends

    while diff > tolerance:
        newEstimate = estimate - ((estimate**2 - numberFloat) / (2*estimate))   # Newton's Method
        diff = newEstimate - estimate                  # difference between two guesses
        diff = abs(diff)                               # return absolute difference
        estimate = newEstimate
    print("The square root of {} is approx. {}".format(numberFloat,round(newEstimate,2)))

userValidation() 


# References:   
# 1. https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# 1. https://bitbucket.org/nerdfirst/newtons-method-square-root/src/master/approx_sqrt.py

