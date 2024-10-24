import sqlite3

def dbTableIsEmpty(tbl: str):
    with sqlite3.connect('Products.db') as connection:
        cursor = connection.cursor()
        return cursor.execute(f'SELECT COUNT(*) FROM {tbl}').fetchone()[0] == 0

def initiate_db():
    with sqlite3.connect('Products.db') as connection:
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

        if dbTableIsEmpty('Products'):
            for i in range(1, 5):
                cursor.execute('INSERT INTO Products (title, description, price, picfile) VALUES (?,?,?,?)',
                               (f'Product{i}', f'Описание Product{i}', f'{i * 100}', f'Img/Product{i}.jpg'))

        connection.commit()

def get_all_products():
    with sqlite3.connect('Products.db') as connection:
        cursor = connection.cursor()
        ret = cursor.execute('SELECT * FROM Products')
        return ret


