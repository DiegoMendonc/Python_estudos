print("-"*25)
print("\033[3m ANALISADOR DE PRODUTOS\033[m")
print("-"*25)
produto = preco = soma_gasto = cont = valor_barato = barato =  mais_1000 = 0
while True:
    produto = str(input("\n\033[3mNOME DO PRODUTO: \033[m")).upper()
    preco = float(input("\033[3mPREÇO: R$\033[m"))
    cont += 1
    soma_gasto += preco
    choice = " "
    if preco >= 1000.00:
        mais_1000 += 1
    if cont == 1 or preco < valor_barato:
        valor_barato = preco
        barato = produto
    while choice not in "SN":
        print("-"*25)
        choice = str(input("\n\033[3;33mDESEJA CONTINUAR? [S/N] \033[m")).strip().upper()[0]
    if choice == "N":
        break
print("-"*25)
print(f"\033[3mO TOTAL DA COMPRA FOI DE \033[2;31mR${soma_gasto:.2f}\033[m\033[m")
print(f"\033[3mTEMOS {mais_1000} PRODUTOS CUSTANDO MAIS DE R$1000.00\033[m")
print(f"\033[3mO PRODUTO MAIS BARATO É O/A {barato}, CUSTANDO R${valor_barato:.2f}\033[m")
print("-"*25)
print("\033[mMUITO OBRIGADO PELAS COMPRAS!")
print("-"*25)