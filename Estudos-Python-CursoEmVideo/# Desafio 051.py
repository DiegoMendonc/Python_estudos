from emoji import emojize
from time import sleep
print("\033[2;31m=\033[m"*25)
print(emojize(" 10 TERMOS DE UMA P.A📊  "))
print("\033[2;31m=\033[m"*25)
t1 = int(input("\n\033[33mFavor, digite o primeiro termo: \033[m"))
r = int(input("\033[33mFavor digite a razão: \033[m"))
dec = t1 + (10 - 1) * r
print("\n\033[2mÓTIMO, VAMOS CALCULAR!\033[m\n")
print("\n\033[31mPROCESSANDO\033[m", end="")
sleep(1.5)
print("\033[31m...\033[m\n")
sleep(1.5)
for pa in range(t1, dec + r, r):
    print("{}".format(pa), end=" -> ")
print("\033[2;31mACABOU\033[m\n")