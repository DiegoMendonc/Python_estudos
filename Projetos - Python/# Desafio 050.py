print("=-"*20)
print("SOMA DOS NÚMEROS PARES")
print("=-"*20)
soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input("\nDigite o {} valor: ".format(c)))
    if n1 % 2 == 0:
        soma = soma + n1
        cont = cont + 1
print("=-"*20)
print("\n\033[33mVOCÊ INFORMOU {} NÚMEROS PARES E A SOMA RESULTOU EM: {}\033[m\n".format(cont, soma))
print("=-"*20)