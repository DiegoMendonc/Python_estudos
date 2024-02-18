from random import randint
print("-"*25)
print("JOGO DA ADIVINHAÇÃO!")
print("-"*25)
comp = randint(0, 10)
print("\nSOU SEU COMPUTADOR, ACABEI DE PENSAR EM UM NÚMERO DE 0 A 10...\nVOCÊ CONSEGUE ADIVINHAR?\n")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite: "))
    palpite = palpite + 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print("\n\033[31mMAIS...\033[m\nTENTE NOVAMENTE...\n")
        else:
            print("\n\033[31mMENOS...\033[m\nTENTE NOVAMENTE...\n")
print("\n\033[2;34mPARABÉNS! VOCÊ ACERTOU MEU PALPITE! O VALOR É {}!\033[m\n".format(comp))
print("\n\033[2mVOCÊ ACERTOU COM \033[2;33m{}\033[m TENTATIVAS, PARABÉNS!\033[m\n".format(palpite))