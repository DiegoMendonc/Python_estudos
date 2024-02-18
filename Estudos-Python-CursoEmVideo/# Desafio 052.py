from time import sleep
from emoji import emojize
print("\033[31m=\033[m"*50)
print(emojize("\033[33mVERIFICADOR DE NÚMEROS PRIMOS 🧑👩\033[m"))
print("\033[31m=\033[m"*50)
n = int(input("\n\033[2mFavor digite um número: \033[m"))
print("\n\033[33mO número digitado é {}\033[m".format(n))
choice = str(input("\nDeseja prosseguir? """))
tot = 0
if choice == "Sim" or choice == "SIM" or choice == "sim":
    print("\n\033[2;36mCERTO! VAMOS PROSSEGUIR\033[m!")
    print("\nPROCESSANDO", end="")
    sleep (1.5)
    print("...\n")
    for p in range(1, n +1):
        if n % p == 0:
            tot = tot + 1
            print("\033[33m", end="")
        else:
            print("\033[30m", end="")
        print("{} ".format(p), end="")
    print("\n\n\033[mO número {} foi divisível {} vezes\n".format(n, tot))
    if tot == 2:
        print("E POR ISSO \033[33mÉ UM NÚMERO PRIMO!\033[m\n")
    else:
        print("E POR ISSO \033[31mNÃO É UM NÚMERO PRIMO\033[m\n")
elif choice == "Não" or choice == "NÃO" or choice == "não":
    print("\n\033[33mMUITO OBRIGADO POR UTILIZAR O APLICATIVO\033[m\n")
else:
    print("\n\033[31mNÃO RECONHECI A SUA RESPOSTA, FAVOR REPETIR A APLICAÇÃO\033[m\n")