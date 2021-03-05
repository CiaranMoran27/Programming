import os
import sys

os.chdir(os.path.dirname(__file__))

def readNumber():
    filename = "count.txt"

    try:
        with open(os.path.join(sys.path[0], filename), "r") as f:
            number = int(f.read())
            print("read file")
            return number

    except IOError:
        print("didnt read file")
        
    # this file will be created when we write back.
    # no file assumes first time running
    # ie 0 previous runs
        return 0
    
readNumber()