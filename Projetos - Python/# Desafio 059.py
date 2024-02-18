from emoji import emojize
from time import sleep
print("\033[31m-\033[m"*35)
print(emojize("\033[7;33;41mCALCULADORA DE DOIS TERMOS 1️⃣ 2️⃣ 3️⃣\033[m"))
print("\033[31m-\033[m"*35)
print("\n\033[33mBEM VINDO(A) EM NOSSA CALCULADORA DE DOIS TERMOS!\033[m\n")
n1 = int(input("\n\033[2mFAVOR DIGITE O PRIMEIRO NÚMERO: \033[m"))
n2 = int(input("\033[2mFAVOR DIGITE O SEGUNDO NÚMERO: \033[m"))
choice = 0
while choice != 5:
    print("""\n\033[34mFAVOR SELECIONAR A OPÇÃO DESEJADA:
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA\033[m\n""")
    choice = int(input("DIGITAR OPÇÃO: "))
    if choice == 1:
        print("\n\033[33mA SOMA ENTRE O {} E {} SERÁ DE {}\033[m".format(n1, n2, (n1 + n2)))
    elif choice == 2:
        print("\n\033[33mA MULTIPLICAÇÃO ENTRE {} E {} SERÁ DE {}\033[m".format(n1, n2, n1 * n2))
    elif choice == 3:
        if n1 > n2:
            print("\n\033[33mO NÚMERO {} É MAIOR QUE {}\033[m".format(n1, n2))
        elif n1 == n2:
            print("\n\033[33mOS NÚMEROS {} E {} SÃO IGUAIS\033[m".format(n1, n2))
        else:
            print("\n\033[mO NÚMERO {} É MAIOR QUE {}\033[m".format(n2, n1))
    elif choice == 4:
        print("\n\033[34mFAVOR, INFORMAR OS NÚMEROS ABAIXO: \033[m")
        n1 = int(input("\n\033[2mFAVOR DIGITE O PRIMEIRO NÚMERO: \033[m"))
        n2 = int(input("\033[2mFAVOR DIGITE O SEGUNDO NÚMERO: \033[m"))
    elif choice == 5:
        print("\n\033[33mCERTO, ESTAREMOS ENCERRANDO A EXECUÇÃO...\033[m\n")
    else:
        print("\n\033[2;31;44mOPÇÃO NÃO RECONHECIDA, FAVOR REINICIAR O PROGRAMA!\033[m\n")
    sleep (2)
print("\033[31m-\033[m"*35)
print(emojize("\033[2;34mFIM DA EXECUÇÃO, VOLTE SEMPRE! ✅\033[m"))
print("\033[31m-\033[m"*35)