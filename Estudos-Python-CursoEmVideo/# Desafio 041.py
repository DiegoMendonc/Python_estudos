# Desafio 041 - Classificação de Atletas
import emoji
import datetime
print("\033[2;44m-\033[m"*50)
print(emoji.emojize("\033[2;31;44mDesafio 041 - Clas. de Atletas 🚴‍♂️🏊‍♂️🏋️‍♂️\033[m"))
print("\033[2;44m-\033[m"*50)
print("\n\033[2mBem-Vindo ao aplicativo de Classificação!\033[m\n")
nas = int(input("Qual é o seu ano de nascimento? "))
atual = datetime.date.today().year
idade = atual - nas
if idade > 25:
    print("\nSua idade é de {} anos\nSua categoria é: \033[2;31mMASTER\033[m\n".format(idade))
elif idade > 19 and idade <= 25:
    print("\nSua idade é de {} anos\nSua categoria é: \033[2;31mSÊNIOR\033[m\n".format(idade))
elif idade > 14 and idade <= 19:
    print("\nSua idade é de {} anos\nSua categoria é: \033[2;31mJÚNIOR\033[m\n".format(idade))
elif idade > 9 and idade <= 14:
    print("\nSua idade é de {} anos\nSua categoria é: \033[2;31mINFANTIL\033[m\n".format(idade))
else:
    print("\nSua idade é de {} anos\nSua categoria é: \033[2;31mMIRIM\033[m\n".format(idade))
print(emoji.emojize("\033[2;30;44mMUITO OBRIGADO POR UTILIZAR O APLICATIVO\033[m 🖖\n"))      