from emoji import emojize
from time import sleep
print("=-"*25)
print(emojize("\033[2;33mGERADOR DE TABUADAS 📝📈\033[m"))
print("=-"*25)
print("\nBEM VINDO(A) NO GERADOR DE TABUADAS\n")
sleep(0.5)
n = int(input("Favor digite o número para gerar a tabuada até o 10: "))
print("\n\033[31mPROCESSANDO\033[m", end="")
sleep(1)
print("\033[31m...\033[m\n")
for tab in range(1, 11):
    print("\033[33m{} X {:2} = {}\033[m".format(n, tab, n*tab))
print(emojize("\n\033[2;36mMUITO OBRIGADO POR UTILIZAR A APLICAÇÃO! ✅\033[m"))
print("=-"*25)