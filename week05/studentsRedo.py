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
 

# function to add courses and grades
def read_modules():
  modules = []
  course = input("Enter the Module name:" ).strip() # get entry for module name
  while course !="":    # do while course is entered i.e. it will stop if no info added
    module={}
    module['course'] = course
    module['grade'] = float(input("Enter the grade: ").strip()) # get entry for grade (as a float)
    modules.append(module) # 
    course = input("Enter the Module name:" ).strip()     # ask for more input - if this is blank the function will return   
  return modules        


def view_modules(modules):
  print("Course Name"   "\tGrade")
  for module in modules:
    print("{}   \t{}".format(module['course'], module['grade']))

# funtion to view the entries
def do_view(students):
  print("\n") # leave a gap between this function call and the show_menu function
  if len(students)<1: # if this is true then there are no entries to show
    print("your student list is empty")
  for student in students:
    print(student['firstname'], " ", student['lastname'])
    view_modules(student['modules'])



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

