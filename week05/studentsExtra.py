# programme to input student details and view them 
# this is a modification of students.py but using a dict for choices/options

# helen o'shea
# 20210218

# function to show the menu - same as students.py
def showMenu():
  print("What would you like to do? \n\
  \t(a) Add new student\n\
  \t(v) View students\n\
  \t(q) Quit")
  option = input("Type one letter (a/v/q): ").strip() # takes input from user 
  return option

# function to add student first name last name  and modules - same as students.py
def doAdd(students):
  myStudent = {} # initalise the dict
  myStudent['firstname'] = input("Enter your first name: ").strip()
  myStudent['lastname'] = input("Enter your last name: ").strip()
  myStudent['modules'] =  readModules() # modules are entered via another function and called here
  students.append(myStudent) # add dict entries to the student list
  #print(type(students))
  return students

# function to add courses and grades - same as students.py
def readModules():
  myCourses = {'course':[], 'grade':[]} # initalise dict with empty list for values for courses and grades
  course = input("Enter the Module name:" ).strip() # get entry for module name
  while course !="":    # do while course is entered i.e. it will stop if no info added
    grade = float(input("Enter the grade: ").strip()) # get entry for grade (as a float)
    myCourses['course'].append(course) # add entry to myCourses with key 'course' and value of course entry
    myCourses['grade'].append(grade) # add entry to myCourses with key grade and value of grade entry
    course = input("Enter the Module name:" ).strip()     # ask for more input - if this is blank the function will return   
  return myCourses        

# funtion to view the entries - same as students.py
def doView(students):
  print("\n") # leave a gap between this function call and the showMenu function
  if len(students)<1: # if this is true then there are no entries to show
    print("your student list is empty")
  for index in range(len(students)): # iterate over the number of students added
    for fname in students[index]['firstname'].split('\n'):  # get the first name - .split('\n') added to prevent item being displayed vertically 
      print( "First Name: ", fname.capitalize() ) # show capitalised first name 
    for lname in students[index]['lastname'].split('\n'):    # get the last name - .split('\n') added to prevent item being displayed vertically 
      print("Last Name: ", lname.capitalize()  )    # show capitalised last name  
    keys = {"course", "grade"} # this is to tidy the course grade dict so that it can be displayed inline
    coursesAndGrades = {k: students[index]['modules'][k] for k in keys } # used to put course and grade together
    for i in range(len(coursesAndGrades['course'])  ):    
      print("Module: {} with Grade {:.0f}%".format  (coursesAndGrades['course'][i],   coursesAndGrades['grade'][i])) # display module name and grade for each student
    print("\n")  
  return students 

# option for q
def doNothing(dumby):
  pass
# option to call various functions depending on input
choiceMap = {
  'a': doAdd,
  'v': doView,
  'q': doNothing
  
}
# this function is the main function that calls the other functions
def main():
  students = [] # initalise student list
  option = showMenu() # show the menu and sets the option
  while(option != 'q'): # while q has not been selected 
    if option in choiceMap: # look at the choiceMap and select function based on input 
      choiceMap[option](students)
    else: # catch for a non valid entry
      print("\n\nplease select either a,v or q")
    option=showMenu() # show the menu again for more choices if q is not selected

# this calls the main function
if __name__ == "__main__":
  main()

