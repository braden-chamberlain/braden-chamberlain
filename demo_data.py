import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

curs.execute('''
    CREATE TABLE demo (
    S VARCHAR,
    X INT,
    Y INT
    );
    ''')

curs.execute('''INSERT INTO demo (S,X,Y) VALUES ('g', 3, 9);''')
curs.execute('''INSERT INTO demo (S,X,Y) VALUES ('v', 5, 7);''')
curs.execute('''INSERT INTO demo (S,X,Y) VALUES ('f', 8, 7);''')

conn.commit()

row_count_q = '''
    SELECT COUNT(*) AS row_count
    FROM demo;
'''

xy_at_least_5_q = '''
    SELECT COUNT(*) AS xy_at_least_5
    FROM demo
    WHERE X > 4 AND Y > 4;
'''

unique_y_q = '''
    SELECT COUNT(DISTINCT y) AS unique_y
    FROM demo;
'''

row_count = curs.execute(row_count_q).fetchall()
xy_at_least_5 = curs.execute(xy_at_least_5_q).fetchall()
unique_y = curs.execute(unique_y_q).fetchall()
