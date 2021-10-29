# program to print out variables and their type
# helen o'shea
# 20210203



i=3
fl = 3.5
isa = True
memo = "how now brown cow" 
lots = []
types = [i, fl, isa, memo, lots]
for t in types:
  print('variable {} is of type:{} and value: {}'.format('t', type(t), t))
