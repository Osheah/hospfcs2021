import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="")

cursor=db.cursor()
'''sql = "insert into student (name, address) values (%s, %s)"
values = ("Mary", "Galway")
cursor.execute(sql, values)
db.commit()


sql2= "select * frm student where id = %s"
values2 = (1,)
cursor.execute(sql2, values2)
for x in result: 
  print(x)
'''
#sql = "create database if not exists cyber"
#cursor.execute(sql)
#db.commit()
sql = "use cyber;"
cursor.execute(sql)
db.commit()
#sql="create table books (id int not null auto_increment, title varchar(250), author varchar(250), price int(250), primary key (id)) "
#cursor.execute(sql)
#db.commit()
sql="insert into books (title, author, price) values ('book3', 'author1', 10); "
cursor.execute(sql)
db.commit()
sql = "select * from books where id = %s;"
sql = "select * from books;"
#values=(1,)
#cursor.execute(sql, values)
cursor.execute(sql)
results = cursor.fetchall()
for x in results: 
  print(x)