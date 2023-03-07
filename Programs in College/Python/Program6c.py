import sqlite3
db=sqlite3.connect('database.db') 
sql="SELECT * from book;"
cur=db.cursor()
cur.execute(sql) 
while True:
    record=cur.fetchone()
    if record==None:
     break
    print (record)
db.close()
