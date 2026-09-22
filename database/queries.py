create_products_table = """ CREATE TABLE IF NOt EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER,
    product_id INTEGER NOT NULL,
    photo TEXT
) """


create_products__detail_table = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        product_id INTEGER NOT NULL,
        category TEXT
    )
"""


insert_product = 'INSERT INTO products (name, price, product_id, photo) VALUES (?, ?, ?, ?)'

insert_product_detail = 'INSERT INTO products_detail (description, product_id, category) VALUES (?, ?, ?)'


get_products = """
    SELECT products.name, products.price, products_detail.description, products_detail.category, products.product_id, products.photo
    FROM products
    INNER JOIN products_detail on products.product_id = products_detail.product_id;
"""

update_product = 'UPDATE {table} SET {field} = ? WHERE products.product_id = ?;'


delete_product = "DELETE FROM products WHERE product_id = ?"
delete_product_detail = "DELETE FROM products_detail WHERE product_id = ?"


create_staff_table = """
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        full_name TEXT,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""


check_staff = 'SELECT 1 FROM staff WHERE user_id = ?'

insert_staff = 'INSERT INTO staff (user_id, full_name) VALUES (?, ?)'

get_staff_list = 'SELECT user_id, full_name FROM staff;'