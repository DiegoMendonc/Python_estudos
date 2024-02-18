print("~"*50)
print("ESCOLHA E SOMA DE VÁRIOS DADOS")
print("~"*50)
cont = soma = 0
while True:
    n = int(input("FAVOR DIGITE UM NÚMERO \033[31m[999 PARA CANCELAR]\033[m: "))
    if n == 999:
        break
    cont += 1
    soma += n
print("~"*50)
print(f"TEMOS UM TOTAL DE \033[2;31m{cont}\033[m NÚMEROS DIGITADOS...\nTOTALIZANDO UM VALOR DE \033[2;31m{soma}\033[m")
print("~"*50)