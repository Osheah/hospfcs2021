# function to write a dictonary in json format 
# helen oshea
# 20210224


import json # import the json module to write in json format

fileName = 'dict.json' # the location of the json file
data = dict(name='mary', age=19, modules = ['english', 'irish', 'maths'],  grades=[50, 60, 48]) #dictonary data

def write_dict(data): # function to write file in json/dict format
  with open(fileName, "wt") as f : 
      json.dump(data, f)



write_dict(data)    # call the function

#note to self dont name any python file json.py and then attempt to run json.dump 