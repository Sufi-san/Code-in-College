import sqlite3
db=sqlite3.connect('database.db') 
try:
 cur =db.cursor()
 cur.execute('''CREATE TABLE book (
 BookID INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT (20) NOT NULL,
 author TEXT (30),
 publisher TEXT (20));''')
 print ('Table Created Successfully') 
except:
 print ('Error in Operation') 
db.rollback()
db.close()
