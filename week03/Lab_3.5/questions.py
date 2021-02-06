#answer the questions
# helen o'shea
# 20210206

numberOfQuestions=5
averageAge=23.4
debugMode=True
name="joe"
ages=[]
months=('Jan','Feb','Mar')
book={}
stuff=[12,'Fred',False,{}]
someone=dict(firstname="joe")
me={
  "firstName":"Andrew",
  "teaching":[{
    "courseName":"programming","semester":1
    },{
      "courseName":"DataRepresentation","semester":2
      }
      ]
    }
print("numberOfQuestions is an int ", type(numberOfQuestions)) 
print("averageAge is a float ", type(averageAge))   
print("debugMode is a boolean ", type(debugMode))
print("name is a string ", type(name))
print("ages is a list ", type(ages))
print("months is a tuple", type(months))
print("months[1] is a string", type(months[1]))
print("book is a dictonary", type(book))
print("stuff is a list", type(stuff))
print("stuff[2] is a boolean", type(stuff[2]))
print("someone is a dictonary ", type(someone))
print("someone['firstname'] is a string", type(someone['firstname']))
print("me['teaching'] is a list", type(me['teaching']))
print("me['teaching'][0]['semester'] is an int", type(me['teaching'][0]['semester']))
print("me['teaching'][0]['coursename'] throws an undefined error but courseName works as a string", type(me['teaching'][0]['courseName']))
