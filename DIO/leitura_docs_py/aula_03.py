import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "novo-diretorio")

# arquivo = open(ROOT_PATH / "novo.txt", "w")
# arquivo.close()

#os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH / "alterado.txt")

# arquivo = open("./DIO/leitura_docs_py/novo-arquivo.txt", "r")

#os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")  