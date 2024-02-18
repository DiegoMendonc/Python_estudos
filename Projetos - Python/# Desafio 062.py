from emoji import emojize
print("\033[2;33m--\033[m"*10)
print(emojize("\033[2;30;43m🚀🚀 SUPER P.A 🚀🚀 \033[m"))
print("\033[2;33m--\033[m"*10)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1 
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end ="")
        termo = termo + razao
        cont = cont +1
    print("PAUSA")
    print("\033[2;33m--\033[m"*10)
    mais = int(input("QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS? "))
print("\033[2;33m--\033[m"*10)
print("\nP.A FINALIZADA COM SUCESSO, FORAM CALCULADOS UM TOTAL DE \033[4;31m{} TERMOS.\033[m\n\n\033[2;34mVOLTE SEMPRE!\033[m\n".format(total))