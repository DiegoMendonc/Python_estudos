# Desafio 040 - Cálculo de Média
import emoji
import time
print("\033[7;36;47m- \033[m"*16)
print(emoji.emojize("\033[2;30;46mDesafio 040: Cálculo de média 📚\033[m"))
print("\033[7;36;47m- \033[m"*16)
m1 = float(input("\n\033[2mFavor digite sua primeira nota: \033[m"))
m2 = float(input("\033[2mFavor digite a sua segunda nota: \033[m"))
med = (m1 + m2) / 2
print("\033[7;36;47m- \033[m"*16)
print("\n\033[2mMuito obrigado por informar, vamos calcular a média!\033[m\n")
choice = str(input("\nDeseja verificar sua média? "))
if choice == "Sim" or choice == "sim" or choice == "SIM":
    print("\nPROCESSANDO...")
    time.sleep(1)
    if med >= 7.0:
        print("\n\033[2mSua média é {}\nVocê está\033[m \033[2;30;42mAPROVADO!\033[m\n".format(med))
    elif med >= 5.0 and med <= 6.9:
        print("\n\033[2mSua média é {}\nVocê está em \033[m\033[2;30;43mRECUPERAÇÃO\033[m\n".format(med))
    else:
        print("\n\033[2mSua média é {}\nVocê está\033[m \033[2;30;41mREPROVADO\033[m\n".format(med))
elif choice == "Não" or choice == "NÃO" or choice == "não":
    print("\n\033[2mMuito obrigado por utilizar o aplicativo!\033[m\n")
else:
    print("\nNão entendi a sua resposta, favor repetir o processo\n")