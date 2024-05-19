import sqlite3 as sq
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conn = sq.connect(ROOT_PATH / "meu_banco.db")
cursor = conn.cursor()

def CREATE(conn, cursor):
    cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(50))")
    conn.commit()
    
def INSERT(conn, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (status, uf) VALUES (?, ?);", data)
    conn.commit()

def UPDATE(conn, cursor, cidade, id):
    data = (cidade, id)
    cursor.execute("UPDATE clientes SET salario=? WHERE id=?;", data)
    conn.commit()

def DELETE(conn, cursor, id):
    data = (id, )
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conn.commit()

def INSERT_MANY(conn, cursor, dados):
    cursor.executemany("INSERT INTO clientes (cidade, estado) VALUES (?,?);", dados)
    conn.commit()

UPDATE(conn, cursor, 6500, 1)
UPDATE(conn, cursor, 3500, 2)
UPDATE(conn, cursor, 1700, 3)
UPDATE(conn, cursor, 4500, 4)
UPDATE(conn, cursor, 2300, 5)
UPDATE(conn, cursor, 1900, 6)
UPDATE(conn, cursor, 3900, 7)
UPDATE(conn, cursor, 9500, 9)
UPDATE(conn, cursor, 6000, 10)
UPDATE(conn, cursor, 4000, 11)
UPDATE(conn, cursor, 4500, 12)
UPDATE(conn, cursor, 6500, 13)
UPDATE(conn, cursor, 850, 14)