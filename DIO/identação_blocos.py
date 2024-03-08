saldo = 0
valor = 0
    
def sacar(valor):
    saldo = 0
    print("-"*25)
    if saldo >= valor:
        print("\033[3;34mValor Sacado com Sucesso!\033[m")
        print("\033[3;34mFavor retirar o valor em Caixa!\033[m")
        print("-"*25)
        
    else:
        print("\n\033[3;31mValor Indisponível!\033[m\n")
        print("-"*25)
    print("\n\033[3;34mMuito obrigado por utilizar nosso serviço!\033[m\n")
    print("-"*25)

def depositar(saldo):
    saldo += saldo 
    print("\n\033[3;34mValor depositado!\033[m\n")
    print("-"*25)

def extrato(saldo):
    print(f"\n\033[3;34mO VALOR TOTAL É DE R${saldo}\033[m\n")
    print("-"*25)


while True:
    print("""
        BEM-VINDO(A) AO BANCO DO FULANO! FAVOR DIGITE A OPERAÇÃO QUE DESEJA REALIZAR!
    [0] SACAR
    [1] DEPOSITAR
    [2] EXTRATO
    [3] SAIR
        """)
    escolha = int(input("OPÇÃO: "))
    if escolha == 0:
        valor = int(input("Favor digite o valor para o saque: R$"))
        sacar(valor)
        saldo -= valor
    elif escolha == 1:
        saldo = int(input("Favor inserir o valor à ser depositado: R$"))
        depositar(saldo)
        saldo += valor
    elif escolha == 2:
        extrato(saldo)
    elif escolha == 3:
        break
    else:
        print("\033[3;31mOPÇÃO INCORRETA! FAVOR DIGITAR CORRETAMENTE!\033[m")
    while True:
        escolha2 = str(input("DESEJA CONTINUAR? [S/N] ")).strip().upper()[0]
        if escolha2 in "Ss":
            break
        elif escolha2 not in "SsNn":
            print("\033[3;31mRESPOSTA INVÁLIDA! FAVOR RESPONDER CORRETAMENTE\033[m")
        elif escolha2 in "Nn":
            print("-"*25)
            print("\n\033[3;34mMUITO OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS!\033[m\n")
            print("-"*25)
            break
        