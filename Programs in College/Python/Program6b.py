import sqlite3
db=sqlite3.connect('database.db')
qry="insert into book (title, author, publisher) values('Internet Programming', 'Arya More', 'Sandip Publications'),('Machine Learning', 'Sufiyan Chougule', 'Arif Publications');"
try: 
    cur=db.cursor()
    cur.execute(qry)
    db.commit() 
    print ("Two Records Added Successfully") 
except:
    print ("Error in operation")
    db.rollback() 
    db.close()
