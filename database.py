import sqlite3

con = sqlite3.connect('simpledb.db', check_same_thread=False)
c = con.cursor()


def create_table(table_name, columns):
    columns_list = ''
    for i in columns:
        columns_list = columns_list + i + ' TEXT,'
    c.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, {});".format(table_name, columns_list[:-1]))


def insert_data(table_name, columns, value):
    columns_list = ''
    value_list = ''
    for i, j in zip(columns, value):
        columns_list = columns_list + i + ','
        value_list = value_list + "'" + j + "',"
    print("INSERT INTO USER ({}) VALUES ({})".format(columns_list[:-1], value_list[:-1]))
    c.execute("INSERT INTO USER ({}) VALUES ({})".format(columns_list[:-1], value_list[:-1]))
    con.commit()


def login_user(tablename, id):
    c.execute("SELECT * FROM {} where username = '{}';".format(tablename, id))
    return c.fetchall()
