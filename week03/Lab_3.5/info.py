#aprogram that stores student name and a list of courses and grades in a dict and then prints out the data
# helen o'shea
# 20210206
# https://www.guru99.com/python-dictionary-append.html appending to dict adapted from this link

myStudent = {'firstname':[], 'lastname':[], 'courses':[] } # creat dictonary keys with empty list values to be inputed by user
myCourses = {"courses":[], "grades":[]} # create a course and grade dictonary with empty list to be inputed by user
fname = input("Students first name:\n ") # user input first name
lname = input("Students last name:\n ") # unser inputs last name
numCourses= int(input("number of courses taken:\n ")) #user inputs the number of courses they are doing
myStudent['firstname'].append(fname) # first name is added to the empty first name list
myStudent['lastname'].append(lname) # last name is added to the empty last name list
for i in range(numCourses): # loop over the number of courses and get course name and grade inputed by user and add them to the MyCourses list
  course = input("Students Course:\n ") 
  grade = input("Grade on course:\n ")
  myCourses["courses"].append(course)
  myCourses["grades"].append(grade)  
myStudent['courses'].append(myCourses)  

print("{} {} is taking {} courses".format(myStudent['firstname'][0], myStudent['lastname'][0], numCourses ))
for i in range(numCourses): # loop over the inner course and grade list and pull out the courses and grades
  for c  in myStudent['courses']:
    print('{} with grade {}'.format(c['courses'][i], c['grades'][i]))

