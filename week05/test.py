# this is to test out the doView function to display code for students.py without having to keep inputing info

# helen o'shea
# 20210218


students = [{'firstname': 'sam', 'lastname': 'smith', 'modules': {'course': ['english', 'maths'], 'grade': 
[49.0, 40.0]}}, {'firstname': 'jane', 'lastname': 'kelly', 'modules': {'course': ['irish'], 'grade': [55.0]}}]



for index in range(len(students)):
  for fname in students[index]['firstname'].split('\n'):   
    print( "First Name: ", fname.capitalize() )
  for lname in students[index]['lastname'].split('\n'):    
    print("Last Name: ", lname.capitalize())     
  keys = {"course", "grade"}
  coursesAndGrades = {k: students[index]['modules'][k] for k in keys }
  for i in range(len(coursesAndGrades['course'])):    
    print("Module: {} with Grade {:.0f}%".format(coursesAndGrades['course'][i], coursesAndGrades['grade'][i]))
