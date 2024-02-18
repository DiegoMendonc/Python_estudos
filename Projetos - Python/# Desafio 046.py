import time
import emoji
print("\033[31m=-\033[m"*20)
print(emoji.emojize("\033[2mCONTAGEM REGRESSIVA DOS FOGOS! 🎆🎇\033[m"))
print("\033[31m=-\033[m"*20)
choice = str(input("\n\033[33mDeseja iniciar a contagem regressiva? \033[m"))
if choice == "Sim" or choice == "SIM" or choice == "sim":
    for fb in range(10, -1, -1):
        print(fb)
        time.sleep(1)
    print("\n\033[2;30;43mEeeeee\033[m", end="")
    time.sleep(1)
    print("\033[2;30;43m...\033[m")
    print("\n\033[31mFO\033[m", end="")
    time.sleep(1)
    print("\033[33mGO!!!\033[m\n")
    print("\033[38m=-\033[m"*20)
    print(emoji.emojize("🎆🎇🎆🎇🎆🎆🎇FELIZ NATAL🎇🎆🎇🎆🎇🎆🎇"))
    print("\033[31m=-\033[m"*20)
elif choice == "Não" or choice == "NÃO" or choice == "não":
    print("\n\033[33mAhh... QUE PENA\033[m")
    print("\033[2;31;40mFELIZ NATAL!\033[m\n")
else:
    print("\n\033[7;31;40mRESPOSTA NÃO ENTENDIDA, FAVOR REPETIR O PROGRAMA...\033[m\n")