# program read in a text file from an existing text
# helen oshea
# 20210224

fileName = 'count.txt' # location of the file

def read_number(): # function to read in the text
  with open(fileName) as f:
    num = int(f.read()) # convert the number string to an integer
    return num  # return the integer

print(read_number())   # call and print the function

