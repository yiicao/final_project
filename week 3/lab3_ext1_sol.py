'''
Write a python program that does the following:

- Print out the first and last name of the employee with the ID 2 
(use `fetchone()`).

- Print out the 3rd most expensive product, in terms of UnitPrice 
(use `fetchall()`).
'''

import sqlite3

conn = sqlite3.connect('f:/2021Winter/SI507/week 3/Northwind_small.sqlite')
cur = conn.cursor()

q1 = '''
    SELECT FirstName, LastName 
    FROM Employee
    WHERE Id = 2
'''
cur.execute(q1)
emp_name = cur.fetchone()
print(f"Employee #2 is {emp_name[0]} {emp_name[1]}.")

q2 = '''
    SELECT ProductName, UnitPrice 
    FROM Product
    ORDER BY UnitPrice DESC
'''
cur.execute(q2)
results = cur.fetchall()
print(f"The 3rd most expensive product is {results[2][0]}.")

conn.close()