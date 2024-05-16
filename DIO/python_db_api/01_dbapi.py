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
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conn.commit()

def UPDATE(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conn.commit()

def DELETE(conn, cursor, id):
    data = (id, )
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conn.commit()

def INSERT_MANY(conn, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conn.commit()
    
dados = [((input("NOME: "), input("EMAIL: "))), (input("NOME: "), input("EMAIL: ")), (input("NOME: "), input("EMAIL: ")), (input("NOME: "), input("EMAIL: "))]

INSERT_MANY(conn, cursor, dados)