# program to read in two numbers and divid first by second and give integer results and remainder
# helen o'shea
# 20210203

x = int(input('Enter first number: '))
y = int(input ('Enter the number you want to divide by: '))
ans = int(x//y)
remainder = x%y
print('{} divided by {} is {} with remainder {}'.format(x, y, ans, remainder))