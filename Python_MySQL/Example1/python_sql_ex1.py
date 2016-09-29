#!/usr/bin/env python
import os
import time
import datetime
import glob
import MySQLdb
from time import strftime

db = MySQLdb.connect("localhost", "root", "xxxx", "python_sql")
curs = db.cursor()
# temperature :: id devices token temperature datelog comment

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO temperature(devices, token, temperature)
         VALUES ('Arduino MEGA 2560 #2', '4d1c2b56c3af41a55166739a5ade1327', 33.18)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()