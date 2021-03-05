import json
import os

# the array we store everything in 
students= []

#change current working directory
os.chdir(os.path.dirname(__file__))

#json filename storing data
filename="students.json"


def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)
    
def readDict(students):
    # this will throw an error if the file does not exist
    # it should readly just return an empty array
    # we can do this later
    with open(filename) as f:
        print(students)
        return json.load(f)


def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(l) load students")
    print("\t(s) save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/l/s/q):").strip()
    return choice

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules


def displayModules(modules):
    print ("\tName \t\tGrade")
    for module in modules:
        print("\t{} \t\t{}".format(module["name"], module["grade"])) 


def doView():
    #print(students)
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])


def doSave():
    writeDict(students)
    print("students saved")


def doLoad(students):
    students = readDict(students)
    print ("students loaded")

#main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 'l':
        doLoad(students)
    elif choice == 's':
        doSave()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    #print(students)
    choice=displayMenu()