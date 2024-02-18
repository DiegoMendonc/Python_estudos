from emoji import emojize
print("-"*50)
print(emojize("\033[33mVALIDAÇÃO DE DADOS\033[m 🙅🙅"))
print("-"*50)
print("\n\033[2mOLÁ, BEM VINDO(A) AO CADASTRO!\033[m\n")
sex = str(input("\n\033[mFAVOR DIGITE O SEU SEXO [M/F]: \033[m")).strip().upper()[0]
while sex not in "MmFf":
    sex = str(input("DADOS INVÁLIDOS! FAVOR DIGITE O SEU SEXO: ")).strip().upper()[0]
print("\n\033[34mSEXO {} REGISTRADO COM SUCESSO!!\033[m\n".format(sex))