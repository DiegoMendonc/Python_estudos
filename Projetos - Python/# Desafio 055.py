print("-"*40)
print("DESAFIO 055: MAIOR E MENOR SEQUÊNCIA")
print("-"*40)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Qual é o peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("\n\033[33mO maior peso foi {}Kg\033[m\n\033[32mO menor peso foi {}Kg\033[m\n".format(maior, menor))