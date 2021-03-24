#  program to store fibonacci function as a module  
# the fibonacci function takes in a number and returns a list containing the fibonacci sequence of that many numbers
# helen oshea
# 20210324

import logging
#logging.basicConfig(level=logging.DEBUG)


def fibonacci(number):
  if number ==0: 
    return[]
  elif number < 0: 
    raise ValueError('Number must be > 0')   
  else: 
    a = 0
    b = 1
    fibonacciSequence = [0]
    for i in range(1, number):
      fibonacciSequence.append(b)
      a, b = b, a+b 
    logging.debug("%d: %s", number, fibonacciSequence)  
    return fibonacciSequence


if __name__ =='__main__':
  # test cases
  return0 = []
  return1=[0]
  return7 = [0, 1, 1, 2, 3, 5, 8]
  return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
  assert fibonacci(7) == return7
  assert fibonacci(11) == return11
  assert fibonacci(0) == return0
  assert fibonacci(1)== return1
  try: 
    fibonacci(-1)
  except ValueError:
    # no negative values  
    pass
  else: 
    assert False
  print("all good")