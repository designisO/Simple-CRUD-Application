import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('Orion','123', 37)")
cursor.execute("INSERT INTO users VALUES ('Lenny','Password-Lenny', 37)")
cursor.execute("INSERT INTO users VALUES ('Paul','Password-Paul', 18)")
cursor.execute("INSERT INTO users VALUES ('John','Password-John', 40)")
cursor.execute("INSERT INTO users VALUES ('Eli','Password-Eli', 42)")


connection.commit()