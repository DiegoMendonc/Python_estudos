from emoji import emojize
from time import sleep
print("=-"*25)
print(emojize("SOMA DE NÚMERO ÍMPARES MÚLTIPLOS DE TRÊS 3️⃣"))
print("=-"*25)
print("\nBEM VINDO(A) EM NOSSA SOMA DE NÚMEROS: 1 À 500\n")
choice = str(input("\nDeseja prosseguir? "))
if choice == "sim" or choice == "SIM" or choice == "Sim":
    print("\nÓTIMO! VAMOS COMEÇAR!\n")
    sleep(1)
    soma = 0
    cont = 0
    for tr in range(1, 500, 2):
        if tr % 3 == 0:
            cont = cont + 1
            soma = soma + tr
    print("A soma de todos os \033[31m{}\033[m valores é de \033[33m{}\033[m".format(cont, soma))         
    print("\n\033[2;35mMUITO OBRIGADO POR UTILIZAR A APLICAÇÃO!\033[m")
elif choice == "NÃO" or choice == "Não" or choice == "não":
    print("\n\033[37mMUITO OBRGADO POR UTILIZAR O APLICATIVO!\033[m\n")
else:
    print("\n\033[2;33;41mNÃO ENTENDI A SUA RESPOSTA...\nFAVOR REINICAR O PROGRAMA\033[m\n")
print("=-"*25)