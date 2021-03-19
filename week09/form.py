# a programme to create a data form with data in it
# helen o'shea
# 20210318

import pandas as pd 


formList =[ ['Mary', 'Maths', 45], ['Alice', 'English', 65],
['Simon', 'French', 35], ['Peter', 'Maths', 65], ['George', 'English', 87 ], ['Jenny', 'French', 47]]
#print(formList)
headers = ['Name', 'Subject', 'Grade']
df = pd.DataFrame(formList, columns=headers)
print(df.head())
print("\nthe descibe output is\n",df.describe())
print("\nThe type is \n",type(df))

df.to_csv('grades.csv', index=False)

df.to_excel('grades.xlsx', sheet_name="data", index=False)


with pd.ExcelWriter('grades.xlsx', engine="openpyxl", mode='a') as writer:
  df.to_excel(writer, sheet_name='summary', index=False)

means = df['Grade'].mean()  
print("{:.2f}".format(means))