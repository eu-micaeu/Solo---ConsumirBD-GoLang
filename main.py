import sqlite3

conn = sqlite3.connect('teste.db')

cur = conn.cursor()

cur.execute("SELECT id, nome, email FROM clientes")

rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}")

conn.close()
