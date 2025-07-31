import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            html TEXT,
            title_selector TEXT,
            price_selector TEXT,
            threshold_price REAL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            title TEXT,
            price REAL,
            timestamp TEXT,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, html, title_selector, price_selector, threshold_price):
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO products (name, html, title_selector, price_selector, threshold_price)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, html, title_selector, price_selector, threshold_price))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products

def save_price_to_db(product_id, title, price):
    conn = sqlite3.connect("prices.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO price_history (product_id, title, price, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (product_id, title, price, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
