print("-"*25)
print("Aulas sobre operadores aritméticos")
print("-"*25)

preco1 = float(input("Digite um preço do primeiro produto: "))
preco2 = float(input("Digite um preço do segundo produto: "))
while True:
    print(f"\n\033[3;34mO Primeiro produto custa R${preco1}\nO Segundo produto custa R${preco2}\033[m\n")
    print("-"*25)
    print("""
    [0]  ADIÇÃO
    [1]  SUBTRAIR
    [2]  MULTIPLICAR
    [3]  DIVIDIR
    [4]  SAIR
    """)
    choice = int(input("OPÇÃO: "))
    print("-"*25)
    if choice == 0:
        print(f"{preco1} + {preco2} = {preco1 + preco2}")
        print("-"*25)
    elif choice == 1:
        print(f"{preco1} - {preco2} = {preco1 - preco2}")
        print("-"*25)
    elif choice == 2:
        print(f"{preco1} X {preco2} = {preco1 * preco2}")
        print("-"*25)
    elif choice == 3:
        print(f"{preco1} / {preco2} = {preco1 / preco2}")
        print("-"*25)
    elif choice == 4:
        print("\033[3;35mMUITO OBRIGADO POR UTILIAR A APLICAÇÃO!\033[m")
        print("-"*25)
        break