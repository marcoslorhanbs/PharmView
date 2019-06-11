import sqlite3

conn = sqlite3.connect('Data/Usuarios.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL, 
    Email TEXT NOT NULL, 
    User TEXT NOT NULL, 
    Password TEXT NOT NULL,
    Tag TEXT NOT NULL,
    Status TEXT NOT NULL)
""")

print("Tabela Criada Com Sucesso")

