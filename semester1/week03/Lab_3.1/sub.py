# program to read in two numbers and subtract first from second
# helen o'shea
# 20210203
try: 
  first = int(input("Enter first number: "))
  second = int(input("Enter second number: "))
except:
  print('your number is not an integer, enter first number again') 
  first = float(input("Enter first number: "))
  second = float(input("Enter second number: "))
answer = first - second
print('{} minus {} is {:.2f}'.format(first, second, answer))

