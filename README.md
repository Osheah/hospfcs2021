# pfcs-labs
# Lab work for programming for Cybersecurity
The following are found in semester1 folder

## Week 1
The task was to push a test file to git hub which can be foudn in test.txt
## Week 2
* addNumber.py
* addOne.py
* hello.py
* hello2.py
* helloWorld.py
* is TwoThree.py
* lab1.py
* multiply.py
* nameAndAge.py
* sendGmail.py

## Week 3
week 3 is found in week03 and contains five labs  namely Lab_3.1, Lab_3.2, Lab_3.3, Lab_3.4, Lab_3.5
### Lab_3.1
* div.py
* extra.py
* randomFruit.py
* randomFruit2.py
* randomGenerator.py
* sub.py
* testTypes.py
### Lab_3.2
* absolute.py
* convert.py
* floor.py
* round.py
### Lab_3.3
* hibye.py
* len.py
* normalise.py
### Lab_3.4
* lines.py
* queue.py
* testLists.py
### Lab_3.5
* info.py
* questions.py

## Week 4
week 4 is found in week04 and contains two labs  namely Lab_4.1 and Lab_4.2
### Lab_4.1
* grade.py
* isEven.py
### Lab_4.2
* evens.py
* guess1.py

## Week 5
week 5 is found in week05 and contains the answers for the single lab that week.
* extra.py contains small code on variable functions
* func.py contains the answers to the questions on what a function will print out
* students.py contains a program to enter student first and last name and modules taken with respective grade. It contains an option to view this information 
* studentsExtra.py is a rejigging of students.py that has choices called from keys in a dict rather than set in a if/elif/else loop
* test.py was helper code for debugging the doView function on student.py 

## Week 6
Week 6 labs are found in week06 directory. There was one lab in week 6 and it included a continuation of the week 5 lab.
* jsonWriteDict.py contains a program to write a dictonary to file
* labquiz.py contains the answers to the lab quiz in week 6
* readsNumber.py contains a program to read a number from a txt file
* readWriteNumber.py contains a program to read in a text file and write a number to a txt file. 
* studentData.json is the output dictonary from the students.py program
* students.py is a continuation of students.py in week05 and adds some more functionality with reading in students via doLoad and saving them via doSave
* test-b.txt was code results from exploring lab quiz problems.
* test-d.txt was code results from exploring lab quiz problems.
* writeNumber.py is code to write to a text file

## Week 7
Week 7 lab is found in week07 directory. There was one lab in week 7. The focus was on regex expressions so some of the lab work was to try out  regex in the search box of visual studio code. The files in this directory contain the following
* access.log - this is from www1 in the tutorial data for splunk which can be dowloaded [here](https://docs.splunk.com/images/Tutorial/tutorialdata.zip)
* anon.py contains code to mask the last two triplets of an ip address in the sample log file (sampleAccess.log). 
* anonIP.txt is the output file for the masked ip in anon.py code
* labquiz.py is the code and answers for the lab quiz in week 7
* regex.py is code to pull out the date segement from the sampleAccess.log file
* sampleAccess.log is the first 6 or so entries in the access.log file from splunk [found here](https://docs.splunk.com/images/Tutorial/tutorialdata.zip)

## Week 8
Week 8 lab is found in week08 directory. There was one lab in week 8. The focus was on plots eg matplotlib. 
* ages.py contains a program that makes a list called ages that has the same number random value as salaries range 21 to 65 and shows a scatter plot of that data with the salaries. Then add a plot of y = x**2 over it
* countries.py contains program that has a list of countries (long) that picks five countries. Some countries should appear in the list more than once. Make a pie chart and a barchart
* extra.py contains program that makes a list called ages that has the same number random value as salaries range 21 to 65 and shows a scatter plot of that data with the salaries. Then add a normal dist plot over it
* prettier-plot.jpg contains output from ages.py
* salaries.py contains a program that makes a list called salaries, that has 10is random numbers from 20k to 80k
* salariesHist.py contains a program that makes a list called salaries, that has 10is random numbers from 20k to 80k and then plots a histogram
* squaredPlot.py contains a program that plots y = x^2

## Week 9
Week 9 is found in week09 directory. There was one lab in week 9. The focus was on pandas

* form.py contains a programme to create a data form with data in it
* grades.csv contains output from form.py
* grades.xlsx contains output from form.py
* readLog.py contains read from an access.log file in to a dataframe - assuming the delimiter is ''. The access log is then cleaned and plotted. 

## Week 10
Week10 is found in week10 directory. The topic is logging. The lab's aim is to create a module that has the fibonacci sequence function i.e. lists the fibonacci sequence of inputed length, with error control that is called from the useFib.py code.  The error controlled module can be found in **myFunctions.py** and the code calling it can be found in **useFib.py**

## Week 11

## Week 12

The following are found in semester2 folder
# ABStuff-NotMine
This is not my material and I will remove it later. It is class material which is  here for handiness sake.
# week0
# week1
This contains programmes to run a flask server and connect to a database. 
it contains
* createDb.py - this is code to create a database table in mysql
* createTable.py - this is code to create a database table in mysql
* insertinto.py This is code to insert entries into a mysql databse 
* requirements.txt - this is a list of requirments for the venv enviroment
* rest_server.py - this is the flask server
# week1hos
This is a redo of week1 to tease out issues it contains the following
* static - folder for static pages
* static_pages other folder for static pages
* templates - folder to store html templates for the flask rest server
* venv - this is not uploaded to github its the virtual enviroment
* .gitignore - ignore file to ignore the virtual enviroment venv
* connect.py - connects the server to a database
* dao.py - this is where curl abilities can be performed on the database 
* requirements.txt - the requirements for the virtual enviroment venv
* rest_server.py flask server
* server.py also flask server
# week2
* dao.py - this is where curl abilities can be performed on the database 
* staticpages other folder for static pages
* templates - folder to store html templates for the flask rest server
* vul_hos - an attempt at codign a vulnerability sql injection - not done
* BookDao.py book database object for connecting server input to the database
* server1-improper-inputs.py - AB's code for improper inputs to illustrate CWE
* testinegerwraper.py 

# week3
* echo-client.py - simple socket client
* echo-server.py - simple socket server
* multiconn-client.py - multiple socket client
* multiconn-server.py - multiple socket server
# week4
* scanip.py programme to scan for open ports



# site
This folder contains simplified code from week 2 on CWE
* staticpages other folder for static pages
* templates - folder to store html templates for the flask rest server
* dao.py book database object for connecting server input to the database
* db.sql - sql commands to run in mysql
* server.py restful flask server


