# program that makes a list called ages that has the same number random value as salaries range 21 to 65 and shows a scatter plot of that data with the salaries. Then add a plot of y = x**2 over it 
#  

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5) # modify the programe so random salaries are the same each time
salaries = np.random.randint(20000, 80000, 10)
ages = np.random.randint(21, 66, 10)
x = np.arange(0, 100, 10)
y = x**2

plt.scatter(ages, salaries)
plt.title("Plot of ages vs salaries\nwith y=x**2 superimposed")
plt.xlabel("Ages in years")
plt.ylabel("Salaries in euro")
plt.plot(x,y, 'r')
plt.savefig('prettier-plot.jpg')
plt.show()