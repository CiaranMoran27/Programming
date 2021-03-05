# es.py
# This program reads in a text file that is requested by user.
# It outputs the number of "e" characters in the file.
# Author: Ciaran Moran

import os

os.chdir(os.path.dirname(__file__))      #change directory to that of current .py file

def userInput():
    choice = input("Enter text file name for uppercase/lowercase 'e' character count: ").strip()
    return choice


def readFile(choice):
    while True:
        try:

            with open(choice,'r') as f:           # open file in read only mode, use of alias means no need to close file
                data = (f.read())                    # call the read function on the alias
                return data

        except IOError:                        # if error encountered the user input-file does not exist
            print("This file does not exist")
            choice =userInput()                   # ask user for another choice and overwrited it into the choice variable
            continue                              # back to start of while loop

def eCharacterCount(data):
    e_List = []
    E_List = [] 

    for line in data:
        for character in line:
            if character == 'e':
                e_List.append(character)
            elif character == 'E':
                E_List.append(character)

    print("There are {} lowercase 'e' characters in this text file".format(len(e_List)))
    print("There are {} uppercase 'E' characters in this text file".format(len(E_List)))


choice = userInput()                             
data = readFile(choice)
eCharacterCount(data)
 


# main reference list is in pands-problem-sheet reposotory README file
#Refernces used: 
# 1.Docs.python.org, 2021, 7.2. Reading and Writing Files — Python 3.9.2 Documentation, viewed 05 March 2021, https://docs.python.org/3/tutorial/inputoutput.html
# 2.GeeksforGeeks, 2019, With statement in Python, viewed 05 March 2021, https://www.geeksforgeeks.org/with-statement-in-python.
# 3.Gutenberg.org, 2000, Moby Dick, viewed 05 March 2021, https://www.gutenberg.org/files/2701/old/moby10b.txt
