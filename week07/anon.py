# code to anonymise the sub domains of ip addresses by xing out the last two triplets. The new lines should be stored in another file. 
# helen oshea
# 20210301

import re

fileName = 'sampleAccess.log'
regex = '\.\d{1,3}\.\d{1,3} ' # the suggested regex was also masking other digits so added a . to both the regex and replace string
replace = '.XXX.XXX'
anonFileName = 'anonIP.txt'  # where the masked ip file will be stored
with open(fileName) as logFile: # open the sample access log file
  with open(anonFileName, 'wt') as output: # open the output file for writing
    for line in logFile:
      replacedLine = re.sub(regex, replace, line) # replace the string found in the regex mask with the replace string
      output. write(replacedLine) # output the masked file to anonIP.txt