import sqlite3

connection = sqlite3.connect("Not_Telegram.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
""")

cursor.execute("DELETE FROM Users")
connection.commit()

for i in range(10):
    cursor.execute("INSERT OR IGNORE INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", (i+1)*10, 1000))
connection.commit()

for i in range(1,11,2):
    cursor.execute("UPDATE Users SET balance=? WHERE id=?", (500, i))
connection.commit()

for i in range(1,11,3):
    cursor.execute("DELETE FROM Users WHERE id=?", (i,))
connection.commit()

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age!=?", (60,))
users = cursor.fetchall()

for i in users:
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]} | Баланс: {i[3]}')

connection.close()


