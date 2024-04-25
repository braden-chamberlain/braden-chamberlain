import psycopg2
import sqlite3
# import pandas as pd

DBNAME = 'kfslimqb'
USER = 'kfslimqb'
PASSWORD = 'OrzzIXQVjkDY42c90Ur0iOAA4E77_SqL'
HOST = 'stampy.db.elephantsql.com'

def connect_to_db(db_name='titanic.sqlite3'):
    return sqlite3.connect(db_name)

def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()

### Queries ###
CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic
    (
    "index" SERIAL NOT NULL PRIMARY KEY,
    "survived" INT NOT NULL,
    "class" INT NOT NULL,
    "name" VARCHAR(150) NOT NULL,
    "sex" VARCHAR(15) NOT NULL,
    "age" INT NOT NULL,
    "num_sib_spouse" INT NOT NULL,
    "num_parent_child" INT NOT NULL,
    "fare" FLOAT NOT NULL
    );'''

GET_PASSENGERS = '''
    SELECT * FROM titanic;
'''

if __name__ == '__main__':
    # df = pd.read_csv('titanic.csv')
    sl_conn = connect_to_db()
    # df.to_sql('titanic', sl_conn)
    sl_curs = sl_conn.cursor()
    sl_curs.execute(GET_PASSENGERS)
    passengers = sl_curs.fetchall()
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, 'DROP TABLE IF EXISTS titanic;')
    modify_db(pg_conn, pg_curs, CREATE_TITANIC_TABLE)

    for passenger in passengers:
        name = passenger[3].replace("'", "''")
        modify_db(pg_conn, pg_curs,
                  f"""
                   INSERT INTO titanic("index", "survived", "class", "name", "sex", "age", "num_sib_spouse", "num_parent_child", "fare")
                   VALUES ({passenger[0]}, {passenger[1]}, {passenger[2]}, '{name}', '{passenger[4]}', {passenger[5]}, {passenger[6]}, {passenger[7]}, {passenger[8]});
                   """
                   )
    
    