print("~"*30)
print("\033[3;33mANÁLISE DE DADOS DE UM GRUPO\033[m")
print("~"*30)
m = mais_18 = idade = m20 =  0
print("\n\033[5;33mOlá! Seja muito bem vindo(a) em nosso analisador de dados!\033[m\n")
while True:
    idade = int(input("\n\033[3mFavor digite a idade para o cadastro: \033[m"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("\n\033[3mSEXO: [M/F] ")).strip().upper()[0]
    if sexo == "M":
        m += 1
    if idade >= 18:
        mais_18 += 1
    if sexo == "F" and idade < 20:
        m20 += 1
    choice = " "
    while choice not in "SN":
        choice = str(input("\n\033[3mDESEJA CONTINUAR? [S/N] ")).strip().upper()[0]
    if choice == "N":
        break
print("\n\033[3;33;40mANALISANDO OS DADOS INFORMADOS: \033[m\n")
print("-"*30)
print(f"\033[3;34mHá {mais_18} pessoas acima de 18 anos;\n{m} homens cadastrados;\n{m20} Mulheres abaixo de 20 anos de idade.\033[m")
print("-"*30)
print("~"*30)
print("\033[3;33mMUITO OBRIGADO POR UTILIZAR A APLICAÇÃO!\033[m")
print("~"*30)