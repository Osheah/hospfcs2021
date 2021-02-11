# program that asks user to enter a number and output if that number is odd or even
# helen o'shea
# 20210210

while quit !=-1:
  myNumber = int(input("Enter a number: "))
  if myNumber%2==0:
    parity ="even"
    print('{} is an {} number'.format(myNumber, parity))
  else:
    parity="odd"
    print('{} is an {} number'.format(myNumber, parity))
  quit=input("Do you want to quit y or n?")
  if quit=="y":
    quit=-1
    print("goodbye")