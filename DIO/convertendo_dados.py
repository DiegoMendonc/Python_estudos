dados_01 = 1.25
print(dados_01)
print(int(dados_01))
print(str(dados_01))
print(bool(dados_01))

dados_02 = input("Favor digite um número: ")
choice = str(input("Deseja converter em número? [S/N] ")).strip().upper()[0]
if choice in "Ss":
    dados_03 = int(dados_02)
    print(dados_03)
else:
    print("Valor não é número, muito obrigado por utilizar o aplicativo! \n")