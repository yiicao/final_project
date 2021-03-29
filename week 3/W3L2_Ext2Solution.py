'''
Write and test queries to get the following data:

- q1: Return the number of customers in the North America Region
- q2: Return the number of unique Titles held by Customers
- q3: Return only the top 3 most heavily stocked Products (those with the largest UnitsInStock values)
'''

import sqlite3

conn = sqlite3.connect('data/Northwind_small.sqlite')
cur = conn.cursor()


q1 = '''
SELECT COUNT(*)
FROM Customer
WHERE Region="North America"
'''

q2 = '''
SELECT COUNT(DISTINCT ContactTitle)
FROM Customer
'''

# what if we want to see what those title are? Remove COUNT
q2b = '''
SELECT DISTINCT ContactTitle
FROM Customer
'''

q3 = '''
SELECT ProductName
FROM Product
ORDER BY UnitsInStock DESC
LIMIT 3
'''


for q in [q1, q2, q2b, q3]:
    cur.execute(q)  
    for row in cur:
        print(row)
    print('-' * 60)
conn.close()