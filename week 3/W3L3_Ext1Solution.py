'''
    Instructions: Write a short program that will print 
    out the 10 products that are least well-stocked, in 
    order from least to most well stocked, with output 
    of the form

    `We have <N> units of <Product name> in stock, and <M> units on order.`

'''


import sqlite3

## make sure you have the right path for connecting to your database
conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

q4 = '''
    SELECT ProductName, UnitsInStock, UnitsOnOrder
    FROM Product
    ORDER BY UnitsInStock 
    LIMIT 10
'''
cur.execute(q4)

for row in cur:
    print(f'We have {row[1]} units of {row[0]}, and {row[2]} on order.')


## Is there a different way we could do this? 
## Does the SELECT order matter? 
print("-"*40)
print("Alternative Query")
print("-"*40)


q4_alt = '''
    SELECT UnitsInStock, ProductName, UnitsOnOrder
    FROM Product
    ORDER BY UnitsInStock 
    LIMIT 10
'''
cur.execute(q4_alt)

for row in cur:
    print(f'We have {row[0]} units of {row[1]}, and {row[2]} on order.')

conn.close()