import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt

import pandas as pd

ROOTH_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOTH_PATH / "meu_banco.db")
df = pd.read_sql_query("SELECT * FROM clientes", conn)

# bar = plt.bar(df["uf"], df["salario"])
pl = plt.bar(
    df["uf"],
    df["salario"],
    0.9,
    None)

plt.show()

pl2 = plt.pie(
    df["salario"],
    None,
    df["uf"],
    None,
    None)

plt.show()