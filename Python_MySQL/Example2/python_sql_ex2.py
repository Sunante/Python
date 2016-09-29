#!/usr/bin/env python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "xxxx", "python_sql")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# temperature :: id devices token temperature datelog comment
sql = "SELECT * FROM temperature"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      devices = row[1]      
      temperature = row[3]
	  #datetime = row[4]
	  datetime =30
      # Now print fetched result
      print "id=%d,devices=%s,temperature=%f,datetime=%d" % \ (id, devices, temperature, datetime )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()