# answers to lab quiz for week 7
# helen oshea
# 20210301

import re
regex = "^Hell*o"
#filename = '../../../splunk/tutorial_datasets/tutorialdata/www1/access.log'
filename = 'quiz.txt'
with open(filename) as quizFile:
  for line in quizFile:
    searchResult = re.search(regex, line)
    if (searchResult):
      matchingLine = line
      print(matchingLine, end="")

# regex = 'hello' will print out the first line hello
# regex = 'Hello' wil print out lin 2, line 3 line 5
#regex = '^Hello' will print out lines 2 3 not line 5 as it starts with tab tab
# regex = '^Hell*o will print out 2, 3, 6? it printed out 2 3 and 4 - i got that wrong - why- * matches zero or more l's
# regex = '^Hell+o startw with Hell and one or more l's 2 3 
# regex = '^Hell?o will print out 2 3 4
# regex='^hello [A-Z]' starts with hello and any upper text nothing 
#regex='^Hello [A-Z]' starts with Hello and any upper text Hello World 3 
#regex = '=' prints line 7 
#regex = '#' this will print ou the comment line 8
#regex = '[' prints out line 9 no it crashes the program because it needs to be escaped
# regext = '^$' starts with the end of the string blank lines? line 10

# go over ^Hell+o * ? as im not sure what is going on here is the symbol related to the character before or string befor or is it after