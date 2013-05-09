import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'test')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(256))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London ')")
    cur.execute("INSERT INTO Writers(Name) VALUES('JK Rolin')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Brian Enstein')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Mark Twean')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Bob Florid')")
