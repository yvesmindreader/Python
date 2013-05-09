import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'test')

try:
    cur = con.cursor()
    rowcounts = cur.execute("SELECT * FROM Writers")
    #for i in range(rowcounts):
    #   row = cur.fetchone()
    #  print row[0], row[1]
    rows = cur.fetchall()
    desc = cur.description
    print 'cur.description:', desc
    print "%s %3s" % (desc[0][0], desc[1][0])
    for row in rows:
        print "%s %s" % (row[0], row[1])

    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
                ("Van Goh", "4"))
    cur.execute("UPDATE Writer SET Name = %s WHERE Id = %s",
                ("Guy ee Maupasant", "4"))
    
    cur.execute("SELECT * FROM Writers")
    rows = cur.fetchall()
    desc = cur.description
    print 'cur.description:', desc
    print "%s %3s" % (desc[0][0], desc[1][0])
    for row in rows:
        print "%s %s" % (row[0], row[1])
    con.commit()

    cursor.close()
    con.close()
except mdb.Error, e:
    con.rollback()
    print "Error %d: %s" %(e.args[0], e.args[1])
