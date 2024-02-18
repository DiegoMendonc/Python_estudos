print("======== \033[2;31mLOJA DO DIEGUINHO\033[m ========")
valor = float(input("Preço da compra: R$"))
print("""\nFORMAS DE PAGAMENTO:
    [ 1 ] à vista no dinheiro/cheque
    [ 2 ] à vista no cartão
    [ 3 ] 2x no cartão de crédito
    [ 4 ] 3x ou mais no cartão de crédito\n""")
choice = int(input("Qual é a sua forma de pagamento? "))
if choice == 1:
    desc = valor - (valor * (10 / 100))
    print("\nVocê irá pagar na modalidade à vista no dinheiro/cheque com desconto de 10%")
    print("\nO valor total ficará no total de \033[2;33mR${:.2f}\033[m\n".format(desc))
elif choice == 2:
    desc1 = valor - (valor * (5 / 100))
    print("\nVocê irá pagar na modalidade à vista no cartão, com desconto de 10%\n")
    print("\nO valor total ficará no total de \033[2;33mR${:.2f}\033[m\n".format(desc1))
elif choice == 3:
    parc = valor / 2
    print("\nVocê irá pagar em 2x no cartão de crédito\n")
    print("\nO valor ficará em 2 parcelas de \033[2;33mR${:.2f}\033[m\n".format(parc))
elif choice == 4: 
    cparc = int(input("\nEm quantas vezes deseja parcelar o produto? \n"))
    jparc = valor + (valor * (20 / 100))
    valorparc = jparc / cparc
    print("\nVocê escolheu o total de {} parcelas para a compra.\n".format(cparc))
    print("\nO valor ficou em \033[2;33m{}x\033[m de \033[2;33mR${:.2f}\033[m\n\nValor acrescido de juros no total de \033[2;31mR${:.2f}\033[m\n".format(cparc, valorparc, jparc))
else:
    print("\n\033[2;31mValor digitado não reconhecido, favor repetir o processo.\033[m\n")