# program that makes a list called ages that has the same number random value as salaries range 21 to 65 and shows a scatter plot of that data with the salaries. Then add a normal dist plot over it

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(5) # modify the programe so random salaries are the same each time
salaries = np.random.randint(20000, 80000, 10)
ages = np.random.randint(21, 66, 10)
x=np.random.standard_normal(size=100)
sns.displot(x, kde=True)
plt.scatter(ages, salaries, norm=True)
plt.title("Plot of normalised ages vs normalised salaries\nwith superimposed normal distributon")
plt.xlabel("Ages in years")
plt.ylabel("Salaries in euro")

#plt.savefig('prettier-plot_with_normal.jpg')
plt.show()