import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("UPDATE users SET age = 99")

connection.commit()