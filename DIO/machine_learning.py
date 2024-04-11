import pandas as pd

def linha():
    print("-"*50)

def titulo(x):
    print(f"\033[3;34m{x:^50}\033[m")
    print("-"*50)

def espaco():
    print()


linha()
titulo("Introdução à Machine Learning: Redes Neurais")
espaco()
