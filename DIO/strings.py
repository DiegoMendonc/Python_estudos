# Métodos Úteis
curso = "pYtHon"

print(curso.upper()) # Maiúsculos
print(curso.lower()) # Minúsculos
print(curso.title()) # Padrão Título

curso1 = "    Python "

print(curso1.strip()) # Eliminar todas os espaços
print(curso1.lstrip()) # Eliminas os espaços à esquerda

curso2 = "Python"
print(curso2.center(50, "-")) # Centralizar com caractere especial
print(".".join(curso2)) # Join para colocar string dentro de uma variavel
print()
print()
# Interpolação de String

menu = "PRÁTICA"
print(menu.center(50, "-"))
print()

while True:
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    profissao = str(input("Digite sua profissão: "))

    print("-"*50)
    print(f"\nPrazer me te conhecer, {nome}!\nSua idade é de {idade} anos de idade;\nSua profissão é {profissao}.\n")
    
    choice = " "
    
    while choice not in "SsNn":
        choice = str(input("CONFIRMA AS INFORMAÇÕES? [S/N] ")).strip().upper()[0]
        if choice not in "NnSs":
            print("\nNão entendi... Favor repetir\n")
    if choice in "Ss":
        print(f"\nMuito obrigado por nos informar em nossa base, {nome}!\n")
        print("-"*50)
        break
    if choice in "Nn":
        print("\nFavor repetir o processo\n")
        print("-"*50)
        continue
print()

#Fatiamento de Strings

nome = "Diego Felipe"

print(nome[0])
print(nome[:9])
print(nome[5:])
print(nome[::-1])

print()

#Strings de Múltiplas linhas

print(f"""
==================== MENU =========================

Olá Pessoal, meu nome é {nome} e desejo boas-vindas
em nosso menu protótipo!
Bem-Vindo(a)!
Qualquer dúvida, apenas entrar em contato conosco!

==================================================
      """)

print()

PI = 3.14159
print(f"{PI:.2f}")