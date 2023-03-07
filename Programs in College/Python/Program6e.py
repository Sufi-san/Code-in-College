import sqlite3
db = sqlite3.connect( 'database.db')
qry= " DELETE from book where publisher='Sandip Publications'"
try:
    cur=db.cursor()
    cur.execute(qry)
    db.commit()
    print(" Record Deleted Successfully")
except:
    print(" Error in Operation")
    db.rollback()
    db.close()
