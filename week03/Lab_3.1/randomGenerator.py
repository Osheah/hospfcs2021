# program that prints out a random number between 1 and 10
# helen o'shea
# 20210203
import random
start = int(input("Enter the lowest value of the range"))
end = int(input("Enter the highest value of the range"))
print('A random number between {} and {} is {}'.format(start, end, random.randint(start,end)))

