from tkinter import *
from tkinter import ttk
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

#Criando a janela

janela = Tk()
janela.title("Dashboard - Projeto")
janela.geometry("1190x500")
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela principal em duas usando frames:
frame_top = Frame(janela, width=1370, height=45, pady=0, padx=0, bg=branco, relief="flat")
frame_top.grid(row=0, column=0)

frame_quadro = Frame(janela, width=1370, height=700, pady=15, padx=7, bg=branco, relief="flat")
frame_quadro.grid(row=1, column=0, sticky=NW)

# Configuração do Frame top:

app_nome = Label(frame_top, text="Dashboard - Projeto" , width=20, height=2, pady=-1, padx=0, bg=branco, fg=valor, relief="flat", anchor=N, font=("Ivy 14 bold"))
app_nome.place(x=0, y=5)


janela.mainloop()