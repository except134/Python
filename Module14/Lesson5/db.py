import sqlite3

DB_FILE = 'Products.db'

def dbTableIsEmpty(tbl: str):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        return cursor.execute(f'SELECT COUNT(*) FROM {tbl}').fetchone()[0] == 0

def initiate_db():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products(
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL,
                    picfile TEXT NOT NULL
                )
            """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER DEFAULT 1000 NOT NULL
                )
            """)

        if dbTableIsEmpty('Products'):
            for i in range(1, 5):
                cursor.execute('INSERT INTO Products (title, description, price, picfile) VALUES (?,?,?,?)',
                               (f'Product{i}', f'Описание Product{i}', f'{i * 100}', f'Img/Product{i}.jpg'))

        connection.commit()

def get_all_products():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        ret = cursor.execute('SELECT * FROM Products')
        return ret

def add_user(username, email, age):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        if not is_included(username):
            cursor.execute('INSERT INTO Users (username, email, age) VALUES (?,?,?)', (username, email, age))

def is_included(username: str):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()
        ret = cursor.execute('SELECT * FROM Users WHERE username==?', (username,))
        return ret.fetchone() != None

