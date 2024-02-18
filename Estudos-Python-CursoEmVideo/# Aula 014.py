# estrutura de repetição sem delimitador (while = enquanto)
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n !=0:
        if n % 2 == 0:
            par = par + 1
            print("O valor é par")
        else:
            impar = impar + 1
            print("O valor é ímpar")
print("Você digitou {} números pares e {} números ímpares".format(par, impar))