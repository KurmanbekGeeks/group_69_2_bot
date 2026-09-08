import sqlite3
from database.queries import create_products_table, insert_product


path_db = 'database/sqlite3.db'


def init_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(create_products_table)
    print('БД подключена!')
    conn.commit()
    conn.close()


def add_product_db(name, price, description):
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(insert_product, (name, price, description))
    conn.commit()
    conn.close()