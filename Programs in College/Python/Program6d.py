import sqlite3
db=sqlite3.connect('database.db')
qry="update book set title = 'Microprocessors' where author = 'Arya More'"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print("Record Updated Successfully")
except:
    print("Error in Operation")
    db.rollback()
    db.close()