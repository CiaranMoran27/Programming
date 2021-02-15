# This Program continues to prompts the user to guess a random number between 0 to 100, until the guess is correct
# Author: Ciaran Moran

import random

# assign random number between 1 to 100 to the variable
numberToGuess = random.randint(0,100)
guess = int(input("Please guess the number:"))

#use of Sentinal controlled While loop
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else:
        print ("too high")
    #change conditional variable
    guess = int(input("Please guess again:"))
    
print ("Well done! Yes the number was ", numberToGuess)