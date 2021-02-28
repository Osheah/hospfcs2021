#20210228
#helen o'shea
#continuation of week05 student problems. I took the code from Andrew Beatty's code https://raw.githubusercontent.com/andrewbeattycourseware/pforcs2021/main/code/week06-files/lab06.07-loadStudents.py
# and adapted it

import json
import os.path

# the array we store everything in 
students= [] # initialise the student list
filename="studentData.json" # the location of the student data in json form.


# from https://raw.githubusercontent.com/andrewbeattycourseware/pforcs2021/main/code/week06-files/lab06.02d-checkfileexists.py
if not os.path.isfile(filename): # check if the file name is present
    print ("File does not exist") # if its not path then its not created 
    
# function to write to a dictonary
def writeDict(obj):
  with open(filename, 'wt') as f:
    json.dump(obj,f)

 # function to read a dictonary   
def readDict():
    try: # try opening the file for reading
      with open(filename) as f:
          return json.load(f)
    except IOError: # throw an error if file does not exist
        print('File does not exits')
        return 0      

# function to display the menu
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(l) load students")
    print("\t(s) save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice
# function to add a student 
def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("Enter name :") # enter students name
    currentStudent["modules"]= readModules() # and their modules by calling the readModules function
    students.append(currentStudent) # append the info to the students list
# function to read in the modules and grades of the student
def readModules():
    modules = [] # initailise module list
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip() # enter the module
    
    while moduleName != "": # do as long as the module is not blank
        module = {} # dictonary for storing the module course and grade is initialised
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:")) # enter the moduel grade
        modules.append(module)# append course/module and grade to the module
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules # return the modules i.e. the module and grade
#function to show the modules    
def displayModules(modules):
    print ("\tName   \tGrade") # headings
    for module in modules: # print out the module and grade inline
        print("\t{}  \t{}".format(module["name"], module["grade"])) 


# function to view the student details
def doView():
    #print(students)
    for currentStudent in students:
        print(currentStudent["name"]) # print the name
        displayModules(currentStudent["modules"]); # print the module details

# function to save student details in dict format
def doSave():
    writeDict(students)
    print("students saved")


# function to load student details in dict format
def doLoad():
    # we are changing the global variable students 
    # so we need to indicate this
    # (this stumped me for a little bit)
    global students 
    students = readDict()
    print ("students loaded")

#main program
choice = displayMenu()
doLoad() # autoload the student data
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment

    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 'l':
        doLoad()
    elif choice == 's':
        doSave()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    #print(students)
    choice=displayMenu()
        
        