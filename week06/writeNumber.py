# program read in a text file number and overwrites a file with that number from an existing text
# helen oshea
# 20210224

fileName = 'count.txt' # file location
# function to write a number
def writeNumber(): 
  with open(fileName, 'wt') as f: # open the file for writing text
    num =input("enter a number: ") # enter a number
    int(f.write(num)) # convert the string number to an integer
    return num  # return the integer

print(writeNumber())   # call the function

