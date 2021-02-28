# the with statement will automatically close the file when it is finished with it
'''
with open("test-a.txt") as f:
  data = f.read()
  print(data)
 #this is the same 
'''
'''
 f = open("test2.txt")
 data = f.read()
 print(data)
 f.close()
'''

# the above will give an error unless there is a file called test-a.txt present. 

# the with statement will automatically close the file when it is finished with it
with open("test-b.txt", "w") as f:
  data = f.write("test b\n") # returns the number of chars written
  print(data)

with open("test-b.txt", "w") as f2:
  data = f2.write("another line\n") # returns the number of chars written
  print(data)  

  # this will create the file test-b.txt and write the number of characters in test b\n 7 then create the file again and writes the number of characters in "another line\n" 13 so there will be one line on the test-b.txt written and it will be another line

  # the with statement will automatically close the file when it is finished with it
with open("test-d.txt", "w") as f:
  data = f.write("test d\n") # returns the number of chars written
  print(data)

with open("test-d.txt", "a") as f2:
  data = f2.write("another line\n") # returns the number of chars written
  print(data)  

# the first part will do the same as the pervious first part and output 7 but the second part will append the text to the first 
#giving an output. The ouput should be the same but the text files will be different. 

