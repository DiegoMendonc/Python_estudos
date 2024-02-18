resp = "S"
num = quant = soma = media = maior = menor = 0
while resp in "Ss":
    num = int(input("FAVOR DIGITE UM NÚMERO: "))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("QUER CONTINUAR? [S/N] ")).upper().strip()[0]
media = soma / quant
print("VOCÊ DIGITOU \033[33m{}\033[m NÚMEROS\n A MÉDIA FICOU EM \033[34m{:.2f}\033[m\n".format(quant, media))
print("O MAIOR VALOR FOI: \033[31m{}\033[m\nO MENOR VALOR FOI: \033[33m{}\033[m".format(maior, menor))