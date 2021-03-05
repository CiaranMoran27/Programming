import os
import sys

filename = 'count.txt'

def writeNumber(number):
    with open(os.path.join(sys.path[0], filename), "wt") as f:
        f.write((str(number)))

writeNumber(3)

