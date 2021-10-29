# program that creates an array that has tuples of x,y coordinates and prints ou the distance each of those points are from the origin
# helen o'shea
# 20210206
import math
points =[(1,2), (3,3), (4,3)]

for x, y in points:
  distance = math.sqrt(x**2 + y**2) 
  print("point ({}, {}) is {:.2f}, from the origin".format(x,y,distance))