import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Employee')
for row in cur:
    print(row)

conn.close()
