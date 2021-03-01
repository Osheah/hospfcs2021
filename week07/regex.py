# helen o'shea
# 2021301
# program to get the date out of the access.log 

import re

regex = '\[\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}\]'

filename = 'sampleAccess.log'

with open(filename) as logFile:
  for line in logFile:
    searchResult = re.findall(regex, line)
    if (len(searchResult)!=0):
      print(searchResult[0])
      print(searchResult[0][1:-1])