# This program prints out a random fruit
# helen o'shea
# 20210203

import random
fruits = ['Apple', 'Pear', 'Banana', 'Lemon', 'Orange', 'Strawberry', 'Raspberry', 'Kiwi']
index = random.randint(0, len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}".format(fruit))