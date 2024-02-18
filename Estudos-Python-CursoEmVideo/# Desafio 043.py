import emoji
print("\033[44m- \033[m"*20)
print(emoji.emojize("\033[2mDesafio 043: Cálculo de IMC 🏃"))
print("\033[44m- \033[m"*20)
print("\n\033[2;31;40mOlá! Bem vindo na calculador de IMC (ÍNDICE DE MASSA CORPORAL)\033[m\n")
peso = float(input("Qual é o seu peso? (KG) "))
altura = float(input("Qual é a sua altura? (M) "))
imc = peso / (altura ** 2)
if imc > 40:
    print(emoji.emojize("O seu IMC foi de \033[2;30;41m{:.2f}\033[m, escala de OBESIDADE MÓRBIDA! 🚨".format(imc)))
elif imc > 30 and imc <= 40:
    print(emoji.emojize("O seu IMC foi de \033[2;31m{:.2f}\033[m, escala de OBESIDADE ⚠".format(imc)))
elif imc > 25 and imc <= 30:
    print(emoji.emojize("O seu IMC foi de \033[2;33m{:.2f}\033[m, escala de SOBREPESO ⚠".format(imc)))
elif imc > 18.5 and imc <= 25:
    print(emoji.emojize("O seu IMC foi de \033[2;37m{:.2f}\033[m, escala de PESO IDEAL ✅".format(imc)))
else:
    print(emoji.emojize("O seu IMC foi de \033[2;31m{:.2f}\033[m, escala de ABAIXO DO PESO ⚠".format(imc)))
print(emoji.emojize("\n\033[2mMuito obrigado por utilizar o aplicativo! 🤙\033[m\n"))