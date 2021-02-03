# program to read take in a float and output an int rounded down
# helen o'shea
# 20210203

from math import floor

number = float(input('Enter a float number: '))
floored = floor(number)
print('{} floored is {}'.format(number, floored))