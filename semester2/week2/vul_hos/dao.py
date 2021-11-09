import mysql.connector
from mysql.connector import cursor

class Dao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='cwe'
        )
        #print ("connection made")

    def create(self, forms):
        cursor = self.db.cursor()
        #correct way to do it
        sql = "insert into forms (first_name, last_name, email, comment) values (%s,%s,%s,%s)"
        values = [
            forms['first_name'],
            forms['last_name'],
            forms['email'],
            forms['comment']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # bad create
    def bad_create(self, email):
      cursor = self.db.cursor()
      cursor.execute("insert into forms (email) values (%s)", (email))
      self.db.commit()
      return cursor.lastrowid


    def convertToDict(self, result):
        colnames = ['first_name','last_name', 'email', 'comment']
        forms = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                forms[colName] = value
        return forms

dao = Dao()
