# import sqlite3
from database.queries import create_products_table, create_products__detail_table, insert_product, insert_product_detail
import aiosqlite

path_db = 'database/bot.db'


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(create_products_table)
        await conn.execute(create_products__detail_table)
        await conn.commit()
    print('database connect')


async def add_product_db(name, price, description, product_id, photo, category):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(insert_product, (name, price, product_id, photo))
        await conn.execute(insert_product_detail, (description, product_id, category))
        await conn.commit()

# =================== sqlite3 ================

# path_db = 'database/sqlite3.db'

# def init_db():
#     conn = sqlite3.connect(database=path_db)
#     cursor = conn.cursor()
#     cursor.execute(create_products_table)
#     print('БД подключена!')
#     conn.commit()
#     conn.close()


# def add_product_db(name, price, description):
#     conn = sqlite3.connect(database=path_db)
#     cursor = conn.cursor()
#     cursor.execute(insert_product, (name, price, description))
#     conn.commit()
#     conn.close()