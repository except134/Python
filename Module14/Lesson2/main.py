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

cursor.execute("DELETE FROM Users WHERE id=?", (6,))
connection.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.close()


