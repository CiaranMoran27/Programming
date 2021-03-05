import os.path
import sys


os.chdir(os.path.dirname(__file__))
#reference: https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory

filename = "count.txt"

if  os.path.isfile(filename):
    print ("File does  exist")

