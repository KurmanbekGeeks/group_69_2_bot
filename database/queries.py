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
