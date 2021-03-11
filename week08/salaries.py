# a program that makes a list called salaries, that has 10is random numbers from 20k to 80k

# helen oshea
#20210310

import numpy as np
np.random.seed(5) # modify the programe so random salaries are the same each time
salaries = np.random.randint(20000, 80000, 10)
rise = 5000
 # modify  the program to make another array of numbers that has the saleries plus 5k 
print("salaries before the rise are:\n{}\nand  are\n{}\nafter the rise of 5k and\n{}\nafter 5\% \rise".format(salaries, salaries+rise, salaries*1.05))
