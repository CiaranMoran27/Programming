# This Program continues to prompts the user to guess a number, until the guess is correct
# Author: Ciaran Moran

numberToGuess = 30
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