# programme to input student details and view them

# helen o'shea
# 20210218

# function to show the menu
def show_menu():
  print("What would you like to do? \n\
  \t(a) Add new student\n\
  \t(v) View students\n\
  \t(q) Quit")
  option = input("Type one letter (a/v/q): ").strip() # takes input from user 
  return option

# function to add student first name last name  and modules
def do_add(students):
  myStudent = {} # initalise the dict
  myStudent['firstname'] = input("Enter your first name: ").strip()
  myStudent['lastname'] = input("Enter your last name: ").strip()
  myStudent['modules'] =  read_modules() # modules are entered via another function and called here
  students.append(myStudent) # add dict entries to the student list
  #print(type(students))
  return students

# function to add courses and grades
def read_modules():
  myCourses = {'course':[], 'grade':[]} # initalise dict with empty list for values for courses and grades
  course = input("Enter the Module name:" ).strip() # get entry for module name
  while course !="":    # do while course is entered i.e. it will stop if no info added
    grade = float(input("Enter the grade: ").strip()) # get entry for grade (as a float)
    myCourses['course'].append(course) # add entry to myCourses with key 'course' and value of course entry
    myCourses['grade'].append(grade) # add entry to myCourses with key grade and value of grade entry
    course = input("Enter the Module name:" ).strip()     # ask for more input - if this is blank the function will return   
  return myCourses        

# funtion to view the entries
def do_view(students):
  print("\n") # leave a gap between this function call and the show_menu function
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
# this function is the main function that calls the other functions
def main():
  students = [] # initalise student list
  option = show_menu() # show the menu 
  while(option != 'q'): # while q has not been selected function will exit if q selected
    if option == 'a': # show option a
      do_add(students) # option a calls the function to add students
    elif option == 'v': # show option v
      do_view(students) # option v calls the function to show students
    elif option !='q': # catch for a non valid entry
      print("\n\nplease select either a,v or q")
    option=show_menu() # show the menu again for more choices if q is not selected

# this calls the main function
if __name__ == "__main__":
  main()

