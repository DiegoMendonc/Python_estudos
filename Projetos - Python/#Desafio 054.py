from emoji import emojize
from datetime import date
print("-"*25)
print(emojize("\033[31;42mDETECTOR DE MAIORIDADE 🔞\33[m"))
print("-"*25)
ano_atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    idade1 = int(input("Em que ano a {}ª pessoa nasceu? ".format(pess)))
    idade = ano_atual - idade1
    if idade >= 21:
        totalmaior = totalmaior + 1
    else:
        totalmenor = totalmenor + 1
print("\nAo todo, temos \033[32m{} pessoas maiores de idade\033[m e \033[31m{} pessoas menores de idade\033[m\n".format(totalmaior, totalmenor))