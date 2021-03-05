import os
import sys

filename = 'count.txt'

def readNumber():
    with open(os.path.join(sys.path[0], filename), "r") as f:
        number = int(f.read())
    return number

# test it
num = readNumber()
print (num)
