"""
############################## Homework #2 ##############################

% Student Name: Yi Cao

% Student Unique Name: yiicao

% Lab Section 00X: 006

% I worked with the following classmates: Nobody else

%%% Please fill in the first 4 lines of this file with the appropriate information before submitting on Canvas.
"""

import sqlite3 

def question0():
    ''' Provided for example only.
    Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Region"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question1():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q1 = "SELECT * FROM Territory"
    result = cur.execute(q1).fetchall()
    conn.close()
    return result

def question2():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q2 = "SELECT COUNT(*) FROM Employee"
    result = cur.execute(q2).fetchall()
    conn.close()
    return result

def question3():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q3 = '''
        SELECT * 
        FROM Product
        ORDER BY Id DESC
    '''
    result = cur.execute(q3).fetchall()
    conn.close()
    return result

def question4():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function 
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q4 = '''
        SELECT ProductName, UnitPrice 
        FROM Product
        ORDER BY UnitPrice DESC
        LIMIT 3
    '''
    result = cur.execute(q4).fetchall()
    conn.close()
    return result

def question5():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q5 = '''
        SELECT ProductName, UnitPrice, UnitsInStock
        FROM Product
        WHERE UnitsInStock <= 100 AND UnitsInStock >= 60
    '''
    result = cur.execute(q5).fetchall()
    conn.close()
    return result

def question6():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q6 = '''
        SELECT ProductName
        FROM Product
        WHERE UnitsInStock < ReorderLevel
    '''
    result = cur.execute(q6).fetchall()
    conn.close()
    return result

def question7():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q7 = '''
        SELECT Id
        FROM [Order]
        WHERE ShipCountry = "France" AND ShipPostalCode LIKE "%04"
    '''
    result = cur.execute(q7).fetchall()
    conn.close()
    return result

def question8():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q8 = '''
        SELECT CompanyName, ContactName
        FROM Customer
        WHERE Country = "UK" AND Fax != "NULL"
    '''
    result = cur.execute(q8).fetchall()
    conn.close()
    return result

def question9():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q9 = '''
        SELECT ProductName, UnitPrice
        FROM Product
            JOIN Category
                ON Product.CategoryId = Category.Id
        WHERE Category.CategoryName = "Beverages"
    '''
    result = cur.execute(q9).fetchall()
    conn.close()
    return result


def question10():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q10 = '''
        SELECT ProductName
        FROM Product
        WHERE CategoryId = 6 AND Discontinued = 1
    '''
    result = cur.execute(q10).fetchall()
    conn.close()
    return result

def question11():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q11 = '''
        SELECT [Order].Id, FirstName, LastName
        FROM [Order]
            JOIN Employee
                ON [Order].EmployeeId = Employee.Id
        WHERE ShipCountry = "Germany"
    '''
    result = cur.execute(q11).fetchall()
    conn.close()
    return result

def question12():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    conn = sqlite3.connect("Northwind_small.sqlite")
    cur = conn.cursor()
    q12 = '''
        SELECT Id, OrderDate, ShipName
        FROM [Order]
        WHERE OrderDate LIKE "2012-07-0%" OR OrderDate = "2012-07-10"
    '''
    result = cur.execute(q12).fetchall()
    conn.close()
    return result



#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    pass


if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''

    result = question9()
    print_query_result(result)

#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    pass

