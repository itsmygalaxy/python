#!usr/bin/python
import MySQLdb
db = MySQLdb.connect(host = "localhost", user = "root", passwd="", db="DB_NAME")
cur = db.cursor()
cur=db.cursor()
cur.execute("SELECT * FROM DB_NAME")
#print the first and second cell values of all rows
for row in cur.fetchall():
  print (row[0],'|', row[1])
db.close()
