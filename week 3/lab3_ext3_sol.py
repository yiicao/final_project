'''
Write queries for the following:

- List the total number of items in stock for each category. 
Return the category ID and the number of items, one row per category.

- List the number of Customers from each country. 
Return the country name and number of customers in descending order 
from most to least.

- Rank all employees in terms of the total number of Orders they 
placed in 2014. Print out the Employee’s first name, last name, 
and the number of orders placed.
'''
import sqlite3

q1 = '''
    SELECT CategoryId, SUM(UnitsInStock)
    FROM Product
    GROUP BY CategoryId
'''

q2 = '''
    SELECT Country, COUNT(*)
    FROM Customer
    GROUP BY Country
    ORDER BY COUNT(*) DESC
'''

q3 = '''
    SELECT FirstName, LastName, COUNT(*)
    FROM [Order]
        JOIN Employee
            ON [Order].EmployeeId = Employee.Id
    WHERE OrderDate LIKE "2014%"
    GROUP BY Employee.Id
    ORDER BY COUNT(*) DESC
'''

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

cur.execute(q1)
for row in cur:
    print(f"Category {row[0]} has {row[1]} items in stock.")

cur.execute(q2)
for row in cur:
    print(f"There are {row[1]} customers from {row[0]}.")

cur.execute(q3)
for row in cur:
    print(f"{row[0]} {row[1]} placed {row[2]} orders in 2014.")

conn.close()