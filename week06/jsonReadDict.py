# function to read a dict obj from file 
# helen oshea
# 20210224


import json # import the json module

fileName = 'dict.json' # name the file

def readDict(): # function to read the file
  with open(fileName) as f : # open the file
      data = json.load(f) # load the dictonary
  return data # return the info in the file  in json format


data = readDict() #call the function
print(data)     # print the data