# program that has a list of countries (long) that picks five countries. Some countries should appear in the list more than once. Make a pie chart and a barchart

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

allCounties = ['Antrim', 'Armagh', 'Carlow', 'Cavan', 'Clare', 'Cork', 'Derry', 'Donegal','Down', 'Dublin', 'Fermanagh', 'Galway', 'Kerry', 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Tyrone', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow']
random5 = np.random.choice(allCounties, 5) # pick 5 random counties from the list
weightedRandom5 = np.random.choice(random5, size=5, p=[0.3, 0.2, 0.1, 0.24, 0.16]) # the counties are weighted by their respective p value  with some more likely to occur than others
countyList = weightedRandom5.tolist() # turn it back to a list
# the list comprehension was lifted from https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item user2314737
tally = [[i, countyList.count(i)] for i in set(countyList)] # get the counties and their respective frequncies
#print(tally)

# split out the counties and frequencies by creating two empty lists county and count and puting all the first elements of the tally into the county list and all the second elements of the tally into the count list
county = []
for i in list(list(zip(*tally))[0]):
  county.append(i)

count=[]
for i in list(list(zip(*tally))[1]):
  count.append(i)

#print(county)
#print(count)  
#create a pie chart with the counts and county as label

# my solution is overly complicated use np.unique as per Andrew Beatty lab - doh
county, count = np.unique(weightedRandom5, return_counts=True) 

plt.pie(count, labels=county)
plt.title("pie plot of 5 random weighted counties of ireland")
plt.show()


plt.bar(county, count)
plt.title("bar plot of 5 random weighted counties of ireland")
plt.xlabel("county")
plt.ylabel("frequency count")
plt.show()







