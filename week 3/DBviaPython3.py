
import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

query = '''
  SELECT LastName, Firstname, City, Country
  FROM Employee
  WHERE Title='Sales Representative'
'''
cur.execute(query)

for row in cur:
    print(f'{row[1]} {row[0]} lives in {row[2]}, {row[3]}')

conn.close()