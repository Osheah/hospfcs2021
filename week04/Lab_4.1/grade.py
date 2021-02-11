# program that reads in a students % mark and outputs their grade - program checks if grade is valid i.e < 40 = fail etc 
# helen o'shea
# 20210210

myGrade = int(round(float(input("Enter the percentage: ")),0))
print("Your grade is", myGrade)
if myGrade >=70:
  print("Distinction")
elif myGrade >=60 and myGrade<70:
  print("Merit 1")
elif myGrade >=50 and myGrade <60:
  print("Merit 2")
elif myGrade >=40 and myGrade<50:
  print("Pass") 
else: 
  print("Fail")     
