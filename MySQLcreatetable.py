import MySQLdb as mdb

con = mdb.connect('localhost', 'root', '1234', 'demo')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(256))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London ')")
