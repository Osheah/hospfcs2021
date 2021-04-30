# program  to read and write numbers to text file and to count how many times the programe has been run
# helen oshea
# 20210224

import os.path # import this to check if file in directory

fileName = 'count.txt' # location of the file

if not os.path.isfile(fileName): # if the file is not present
  print("files is not here and will be created") # then print message taht the file will be created
  write_number(0) # call the write_number function with argumement 0
else: 
  print('file here') # print a message that the file has already been created

# function to read in a num
def read_number():
  try: # tyr and open the file location and read in the file as f
    with open(fileName) as f:
      num = int(f.read()) # convert the number string to a integer
      return num # return the number
  except IOError:
    return 0   # if it is not possible to read in the number return an error code 0

#function to write a number
def write_number(num):
    with open(fileName, 'wt') as f: # open the file  for writing as text
      f.write(str(num))    # convert the integer to a string to write it to text

num = read_number() # call the function
num+=1 # increment the number from its inital value of 0
print('the current counter entry is {}'.format(num)  ) # output the number on the screen
write_number(num) # write the number to the count.txt file



