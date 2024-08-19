import webbrowser as web

def linha():
    print("-"*50)

def titulo(x):
    print(f"\033[3;34m{x:^50}\033[m")
    print("-"*50)

def espaco():
    print()


linha()
titulo("Bem-Vindo ao Pesquisador Python!")
espaco()

frase = input("Digite o que deseja pesquisar no \033[3;33mGoogle\033[m: ")
pesquisar = (f"https://www.google.com.br/search?q={frase}")
web.open(pesquisar)