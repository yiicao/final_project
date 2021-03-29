'''
Write queries that will answer the following:

- How many different job titles are represented in the Customer table?

- What is the minimum UnitPrice among products in the Confections 
category? Return the product name and UnitPrice.

- What would be the most expensive product to reorder, assuming 
that “ReorderLevel” units would be ordered if a reorder were triggered? 
Return the product name and the total cost to reorder.

- What was the average Freight of orders that were shipped in 
April 2014?
'''

import sqlite3

q1 = '''
    SELECT COUNT(DISTINCT ContactTitle)
    FROM Customer
'''

q2 = '''
    SELECT Product.ProductName, MIN(UnitPrice)
    FROM Product
        JOIN Category
            ON Product.CategoryId = Category.Id
    WHERE Category.CategoryName = "Confections"
'''

q3 = '''
    SELECT ProductName, MAX(UnitPrice * ReorderLevel)
    FROM Product
'''

q4 = '''
    SELECT AVG(Freight)
    FROM [Order]
    WHERE OrderDate LIKE "2014_04%"
'''

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

cur.execute(q1)
print (f"There are {cur.fetchone()[0]} different titles")

cur.execute(q2)
print (f"The cheapest confection is {cur.fetchone()[0]}")

cur.execute(q3)
print (f"The most expensive product to reorder would be {cur.fetchone()[0]}")

cur.execute(q4)
print (f"Average freight for April 2014 was {cur.fetchone()[0]}")

conn.close()