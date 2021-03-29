
import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

query = '''
  SELECT LastName, Firstname
  FROM Employee
  WHERE Title='Sales Representative'
'''
cur.execute(query)

for row in cur:
    print(row)

conn.close()