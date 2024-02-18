import time
import emoji
import random
print("\033[2;31;40m- \033[m"*20)
print(emoji.emojize("\033[7;41mDESAFIO 045 - GAME - JO KEN PO! 👊 🖐 ✌\033[m"))
print("\033[2;31;40m- \033[m"*20)
print("\n\033[2mVamos começar!\033[m\n")
print(""" Escolha uma das opções para tentar me vencer!
      
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA""")
choice = int(input("\n\033[2;33mQual é a sua escolha? \033[m"))
compchoi = random.choice([1, 2, 3])
print("\n\033[2;31mJO\033[m")
time.sleep(1)
print("\n\033[2;33mKEN\033[m\n")
time.sleep(1)
print("\033[2;36mPO!!\033[m\n")
time.sleep(1)
if choice == 1 and compchoi == 2:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = 👊\nEU = 🖐\n\n\033[31mVOCÊ PERDEU!!\033[m"))
    print("-="*20)
elif choice == 1 and compchoi == 3:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = 👊\nEU = ✌\n\n\033[36mVOCÊ GANHOU!!\033[m"))
    print("-="*20)
elif choice == 1 and compchoi == 1:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = 👊\nEU = 👊\n\n\033[33mEMPATE!!\033[m"))
    print("-="*20)
elif choice == 2 and compchoi == 2:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = 🖐\nEU = 🖐\n\n\033[33mEMPATE!!\033[m"))
    print("-="*20)
elif choice == 2 and compchoi == 3:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = 🖐\nEU = ✌\n\n\033[31mVOCÊ PERDEU!!\033[m"))
    print("-="*20)
elif choice == 2 and compchoi == 1:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = 🖐\nEU = 👊\n\n\033[36mVOCÊ GANHOU!!\033[m"))
    print("-="*20)
elif choice == 3 and compchoi == 2:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = ✌\nEU = 🖐\n\n\033[36mVOCÊ GANHOU!!\033[m"))
    print("-="*20)
elif choice == 3 and compchoi == 3:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = ✌\nEU = ✌\n\n\033[33mEMPATE!!\033[m"))
    print("-="*20)
elif choice == 3 and compchoi == 1:
    print("-="*20)
    print(emoji.emojize("\nVOCÊ = ✌\nEU = 👊\n\n\033[31mVOCÊ PERDEU!!\033[m"))
    print("-="*20)
else:
    print(emoji.emojize("\n\033[2;31mFAVOR, DIGITE UM VALOR VÁLIDO PARA JOGARMOS 😅\033[m\n"))