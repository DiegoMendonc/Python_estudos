print("\033[33m~\033[m"*30)
print("\033[2;33mTRATAMENTO DE VÁRIOS ELEMENTOS\033[m")
print("\033[33m~\033[m"*30)
num = 0
soma = 0 
cont = 0
num = int(input("\nFAVOR DIGITE UM NÚMERO \033[31m[999 PARA PARAR]\033[m: "))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input("\nFAVOR DIGITE UM NÚMERO \033[31m[999 PARA PARAR]\033[m: "))
print("\n\033[2;33mOPERAÇÃO FINALIZADA!\33[m")
print("NÚMEROS DIGITADOS: \033[2;31m{}\033[m\nSOMATÓRIO DOS NÚMEROS: \033[2;31m{}\033[m".format(cont, soma))
print("\033[33m~\033[m"*30)
print("MUITO OBRIGADO POR UTILIZAR NOSSO APLICATIVO!")
print("\033[33m~\033[m"*30)