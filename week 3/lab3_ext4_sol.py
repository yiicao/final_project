'''
Write queries for the following:

- Find all categories with less than 300 total UnitsInStock. 
Return the category name and total number of units in stock for each.

- Find all employees who have been responsible for more than 100 orders. 
Return the employee’s first and last name, along with the number of 
orders they’ve handled. Results should be ordered from most to least 
orders handled.
'''

import sqlite3

q1 = '''
    SELECT CategoryName, SUM(UnitsInStock) AS sum
    FROM Product AS p
        JOIN Category AS c
            ON p.CategoryId = c.Id
    GROUP BY CategoryId
    HAVING sum < 300
'''

q2 = '''
    SELECT FirstName, LastName, COUNT(*) AS countnum 
    FROM Employee AS e
        JOIN [Order] AS o
            ON e.Id = o.EmployeeId
    GROUP BY e.Id
    HAVING countnum > 100
    ORDER BY countnum DESC
'''

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

cur.execute(q1)
for row in cur:
    print(f"Category {row[0]} has {row[1]} items in stock.")

cur.execute(q2)
for row in cur:
    print(f"{row[0]} {row[1]} has placed {row[2]} orders.")

conn.close()