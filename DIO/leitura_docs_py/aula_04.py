# Tratamento de erros em Python:
import os
import shutil
from pathlib import Path

def linha():
    print("~"*40)
    

ROOTH_PATH = Path(__file__).parent

# try:
#     arquivo = open("meu-arquivo.py")
# except FileNotFoundError as exc:
#     print("\n\033[3;31mARQUIVO NÃO ENCONTRADO!\033[m\n")
#     print(exc)

linha()
try:
    arquivo = open(ROOTH_PATH / "novo-diretorio")
except PermissionError as exc:
    print(f"\033[3;31mNÃO FOI POSSÍVEL ABRIR O ARQUIVO:\n{exc}\033[m")
linha()
