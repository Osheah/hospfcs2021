# program to read in a string and trip any leading/trailing spaces and convert string to lower case and output the lenght of the input and output strings
# helen o'shea
# 20210203

string = input('Please enter a string: ')
striped = string.strip()
lowercase = striped.lower()
print('We reduced the input string from {} to {} characters'.format(len(string), len(lowercase)))