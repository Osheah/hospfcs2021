# programme to input student details and view them

# helen o'shea
# 20210218


def showMenu():
  print("What would you like to do? \n\
  \t(a) Add new student\n\
  \t(v) View students\n\
  \t(q) Quit")
  option = input("Type one letter (a/v/q): ").strip()
  return option

def doAdd(students):
  myStudent = {}
  myStudent['firstname'] = input("Enter your first name: ").strip()
  myStudent['lastname'] = input("Enter your last name: ").strip()
  myStudent['modules'] =  readModules()
  students.append(myStudent)
  print(type(students))
  return students

def readModules():
  myCourses = {'course':[], 'grade':[]}
  course = input("Enter the Module name:" ).strip()
  while course !="":    
    grade = float(input("Enter the grade: ").strip())
    myCourses['course'].append(course)
    myCourses['grade'].append(grade)
    course = input("Enter the Module name:" ).strip()        
  return myCourses        

def doView(students):
  print("\n")
  if len(students)<1:
    print("your student list is empty")
  for index in range(len(students)):
    for fname in students[index]['firstname'].  split('\n'):   
      print( "First Name: ", fname.capitalize() )
    for lname in students[index]['lastname'].split  ('\n'):    
      print("Last Name: ", lname.capitalize()  )     
    keys = {"course", "grade"}
    coursesAndGrades = {k: students[index]  ['modules'][k] for k in keys }
    for i in range(len(coursesAndGrades['course'])  ):    
      print("Module: {} with Grade {:.0f}%".format  (coursesAndGrades['course'][i],   coursesAndGrades['grade'][i]))
    print("\n")  
   

  return students 

def main():
  students = []
  option = showMenu()
  while(option != 'q'):
    if option == 'a':
      doAdd(students)
    elif option == 'v':
      doView(students)
    elif option !='q':
      print("\n\nplease select either a,v or q")
    option=showMenu()
  
if __name__ == "__main__":
  main()

