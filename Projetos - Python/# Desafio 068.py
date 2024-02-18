from time import sleep
from random import randint
print("\033[2;31m-\033[m"*30)
print("\033[33mPAR OU IMPAR: VAMOS JOGAR?\033[m")
print("\033[2;31m-\033[m"*30)
print("\n\033[5;32;44mSE EU GANHAR O JOGO ACABA, HEIN!!\033[m\n")
v = 0
while True:
    print("\033[2;31m-\033[m"*30)
    num = int(input("FAVOR DIGITE UM NÚMERO: "))
    num_pc = randint(0,11)
    total = num + num_pc
    tipo = " "
    while tipo not in "PI":
        print("\033[2;31m-\033[m"*30)
        tipo = str(input("PAR OU ÍMPAR? [P/I] ")).strip().upper()[0]
    print("\033[2;31m-\033[m"*30)
    print("1, 2, 3...")
    sleep(1.5)
    print("EEE", end="")
    sleep(1.5)
    print("...")
    sleep(1)
    print("JÁ!!!\n")
    sleep(0.5)
    print(f"Você jogou \033[2;33m{num}\033[m e o computador jogou \033[2;31m{num_pc}\033[m. Total foi \033[2;34m{total} \033[m", end="")
    print(": DEU PAR!" if total % 2 == 0 else ": DEU ÍMPAR!")
    if tipo == "P":
        if total % 2 == 0:
            print("\n\033[2;34mVOCÊ VENCEU!\033[m")
            v += 1
        else:
            print("\n\033[2;31mVOCÊ PERDEU!\033[m")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("\n\033[2;34mVOCÊ GANHOU!\033[m")
            v += 1
        else:
            print("\n\033[2;31mVOCÊ PERDEU!\033[m")
            break
    print("-"*30)
    print("Vamos jogar novamente...")
print(f"\nGAME OVER! VOCÊ VENCEU {v} vezes!")
print("\033[2;31m-\033[m"*30)
print("MUITO OBRIGADO POR JOGAR! VOLTE SEMPRE!")
print("\033[2;31m-\033[m"*30)