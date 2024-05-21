import sqlite3
import pandas as pd
from tkinter import *
from tkinter import ttk
from pathlib import Path
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Cores:
preto = "#f0f3f5"
branco = "#f3ffff"
azul = "#6f9fd"
valor = "#38576b"
letra = "403d3d"
co5 = "#e06636"
co06 = "#6dd695"
fundo = "#3f729b"

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