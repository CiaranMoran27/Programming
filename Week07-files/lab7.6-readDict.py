import json
import os

os.chdir(os.path.dirname(__file__))
filename="testdict.json"

def readDict():
 # this will throw an error if the file does  not exist
 # it should readly just return an empty dict
 # we can do this later
    with open(filename) as f:
        return json.load(f)

somedict = readDict()
print(somedict)