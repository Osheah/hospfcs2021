# program that uses the myFunctions module (which has the fibonacci sequence code). This program prompts user for a number and returns the list of fibonacci sequence (stored in the module myFunctions)
# helen oshea 
#20210324


import myFunctions as mf

fibLen = int(input("Enter the length of fibonacci sequence"))
print(mf.fibonacci(fibLen))


