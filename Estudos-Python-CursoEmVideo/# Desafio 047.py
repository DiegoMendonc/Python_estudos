print("=-"*20)
print("CONTAGEM DE NÚMEROS PARES")
print("=-"*20)
print("\nBEM-VINDO(A) NA CONTAGEM DE NÚMEROS PARES!\n")
choice = str(input("Deseja começar a contagem? "))
if choice == "SIM" or choice == "Sim" or choice == "sim":
    i = int(input("\nFavor digite o primeiro intervalo numérico: "))
    f = int(input("Favor digite qual é o final do intervalo número: "))
    print("\n")
    for n in range(i, f+1):
        if n % 2 == 0:
            print(n, end=" ")
elif choice == "não" or choice == "Não" or choice == "NÃO":
    print("\nQUE PENA...\n")
else: 
    print("\n\033[2;31mRESPOSTA NÃO ENTENDIDA, FAVOR REINICIAR O PROGRAMA!\033[m\n")
print("")
print("=-"*20)
print("MUITO OBRIGADO POR UTILIZAR NOSSO SISTEMA!")
print("=-"*20)