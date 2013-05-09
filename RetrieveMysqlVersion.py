import MySQLdb as mdb

con = None

try:
    con = mdb.connect('localhost', 'root','1234', 'demo')
    cur = con.cursor()

    cur.execute("SELECT VERSION()")

    data = cur.fetchone()
    print "Database version : %s" % data
finally:
    if con:
        con.close()
