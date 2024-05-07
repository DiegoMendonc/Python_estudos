# Leitura de Arquivos CSV (Planilha EXCEL):  -> CSV (Comma Separated Values = Colunas separadas por vírgulas)

import csv
from pathlib import Path

ROOTH_PATH = Path(__file__).parent 

# try:
#     with open(ROOTH_PATH / "usuarios.csv", "w") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["01", "Maria"])
#         escritor.writerow(["02", "Joao"])
        
# except IOError as exc:
#     print(f"\n\033[3;31mERRO AO ABRIR O ARQUIVO:\n{exc}\033[m")
    
try:
    with open(ROOTH_PATH / "usuarios.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
            
except IOError as exc:
    print(f"\n\033[3;31mERRO AO ABRIR O ARQUIVO:\n{exc}\033[m")