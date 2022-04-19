import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

# command allowing us to create a table called users.
command = "CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT, age INTEGER)"

# exe command
cursor.execute(command)


