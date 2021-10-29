import mysql.connector
db =""
def __init__(self):
  self.do=mysql.connector.connect(host="localhost", user="root", password="", database="cyber")

def create(self, values):
  cursor = self.db.cursor()
  sql = "insert into books (title, author, price) values (%s, %s, %s);"
  cursor.execute(sql, values)
  self.db.commit()
  return cursor.lastrowid

def get_all(self):
  cursor = self.db.cursor()
  sql = "select * from books;"
  cursor.execute(self)
  result = cursor.fetchall()  
  return result

def find_by_id(self, id):
  cursor = self.db.cursor()
  sql = " update books set title = %s, author = %s, price = %s where id = %s"
  values = ('title', 'author', 'price', id)
  cursor.execute(sql, values)
  self.db.commit()

  def delete(self, id):
    cursor = self.db.cursor()
    sql = "delete from books where id = %s;"
    values = (id,)
    cursor.execute(sql, values)  
    self.db.commmit()

  
  
