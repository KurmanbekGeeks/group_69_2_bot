# import sqlite3
# from database.queries import create_products_table, create_products__detail_table, insert_product, insert_product_detail, get_products, 
import aiosqlite
from config import path_db
from database import queries


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_products_table)
        await conn.execute(queries.create_products__detail_table)
        await conn.execute(queries.create_staff_table)
        await conn.commit()
    print('database connect')


async def add_product_db(name, price, description, product_id, photo, category):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product, (name, price, product_id, photo))
        await conn.execute(queries.insert_product_detail, (description, product_id, category))
        await conn.commit()


async def get_products_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_products)
        products = await cursor.fetchall()
    return products



async def update_product_db(field, value, product_id):
    if field in ('name', 'price'):
        table = 'products'
    elif field in ("description", "category"):
        table = 'products_detail'
    else: 
        return

    query = queries.update_product.format(table=table, field=field)

    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(query, (value, product_id))
        await conn.commit()



async def is_staff_db(user_id: int):
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.check_staff, (user_id, ))
        row = await cursor.fetchone()
    return row is not None


async def add_staff_db(user_id, full_name):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_staff, (user_id, full_name))
        await conn.commit()


async def get_staff_list_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_staff_list)
        staff_list = await cursor.fetchall()
        return staff_list

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