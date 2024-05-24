import sqlite3 as sq
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conn = sq.connect(ROOT_PATH / "meu_banco.db")
cursor = conn.cursor()
cursor.row_factory = sq.Row

try:
    cursor.execute("DELETE FROM clientes WHERE id=?", (15,))
    cursor.execute("INSERT INTO clientes (nome, email, profissao, status, cidade, uf, salario) VALUES(?,?,?,?,?,?,?)", ("Jubileu Nunes", "jubibi@hotmail.com.br", "Agricultor", True, "Ponta Porã", "PR", 5000))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?)", (2, "Teste 01", "teste01@gmail.com"))
    conn.commit()
    
except Exception as exc:
    print(f"Ocorreu algum erro...\n{exc}")
    conn.rollback()
