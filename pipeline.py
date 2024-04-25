import psycopg2
from queries_copy import DROP_CHARACTER_TABLE, GET_CHARACTERS, CREATE_CHARACTER_TABLE, INSERT_BRADEN
from sqlite_ex import connect_to_db, execute_q

# PostgreSQL Connnection Credentials

# 'user and default database' from elephantsql
 # open the elephant sql page your using and get the string
DBNAME = 'kfslimqb'
USER = 'kfslimqb'

# 'password' from esql
PASSWORD = 'OrzzIXQVjkDY42c90Ur0iOAA4E77_SqL'

#'server' from esql
HOST = 'stampy.db.elephantsql.com'

def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()

if __name__ == "__main__":
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)
    pg_conn, pg_curs = connect_to_pg()
    modify_db(pg_conn, pg_curs, DROP_CHARACTER_TABLE)
    modify_db(pg_conn, pg_curs, CREATE_CHARACTER_TABLE)
    modify_db(pg_conn, pg_curs, INSERT_BRADEN)

    for character in sl_characters:
        modify_db(pg_conn, pg_curs,
                f'''
                INSERT INTO characters("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
                VALUES ('{character[1]}', {character[2]}, {character[3]}, {character[4]}, {character[5]}, {character[6]}, {character[7]}, {character[8]});
                '''
                   )

    # pg_curs.execute(DROP_TEST_TABLE)
    # pg_curs.execute(CREATE_CHARACTER_TABLE)
    # pg_curs.execute(INSERT_BRADEN)
    # pg_conn.commit()
