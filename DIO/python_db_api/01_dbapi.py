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
    cursor.execute("UPDATE clientes SET profissao=?, salario=? WHERE id=?;", data)
    conn.commit()

def DELETE(conn, cursor, id):
    data = (id, )
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conn.commit()

def INSERT_MANY(conn, cursor, dados):
    cursor.executemany("INSERT INTO clientes (profissao, salario) VALUES (?,?);", dados)
    conn.commit()


# dados = [((input("PROFISSAO: "), input("SALARIO: ")))]

# UPDATE(conn, cursor, "analista administrativo", 3200, 2)
# UPDATE(conn, cursor, "operador de produção", 2500, 3)
# UPDATE(conn, cursor, "supervisor de produção", 5000, 4)
# UPDATE(conn, cursor, "assistente de faturamento", 2300, 5)
# UPDATE(conn, cursor, "auxiliar administrativo", 1900, 6)
# UPDATE(conn, cursor, "encarregado operacional", 3500, 7)
# UPDATE(conn, cursor, "analista de rotas", 5500, 8)
# UPDATE(conn, cursor, "engenheiro de dados", 9000, 9)
# UPDATE(conn, cursor, "engenheiro de produção", 8500, 10)
# UPDATE(conn, cursor, "analista de logística", 2900, 11)

# UPDATE(conn, cursor, "Ana Beatriz Carvalho Rosa", "abcr@outlook.com.br", 12)
# UPDATE(conn, cursor, "Janaína Godoi", "janadoi@hotmail.com", 14)