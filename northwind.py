import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

expensive_items = '''
    SELECT * FROM product
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

avg_hire_age = '''
    SELECT AVG(HireDate - BirthDate) AS avg_age_at_hire
    FROM employee
'''

ten_most_expensive = '''
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product
    JOIN Supplier
    ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

largest_category = '''
    SELECT CategoryName, COUNT(pd.ProductName) AS num_products
    FROM Product as pd
    JOIN Category as cg
    ON pd.CategoryId = cg.id
    GROUP BY CategoryName
    ORDER BY num_products DESC
    LIMIT 1
'''
