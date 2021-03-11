# a program that plots y = x^2
# helen oshea
#20210310

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-100, 100, 10)
#print(x)
y = x**2

plt.plot(x,y)
plt.title("Plot of y=x**2")
plt.show()
