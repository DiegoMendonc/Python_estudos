from emoji import emojize
print("=-"*20)
print("\033[2mANALISADOR DE INFORMAÇÕES\033[m")
print("=-"*20)
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1, 5):
    print("\n------{}ª PESSOA------".format(p))
    nome = str(input("\nQual é o nome: "))
    idade = int(input("Qual é a idade: "))
    sexo = str(input("Qual é o sexo da pessoa(M/F): ")).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
         
mediaidade = somaidade / 4
print("\nA MÉDIA DE IDADE DAS PESSOAS É DE \033[33m{:.1f} ANOS\033[m".format(mediaidade))
print(emojize("O HOMEM MAIS VELHO TEM {} ANOS E SE CHAMA {} 👴".format(maioridadehomem, nomevelho)))
print(emojize("\033[31mAO TODO TEMOS {} MULHERES COM MENOS DE 20 ANOS DE IDADE\033[m 🤷\n".format(totmulher20)))