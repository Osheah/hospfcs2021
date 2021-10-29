import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password = "",
  database = "datarepresentation"
)

mycursor = mydb.cursor()
sql = "Create table student (id int auto_increment primary key, name varchar(255), age int)"

mycursor.execute(sql)
