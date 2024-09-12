class Main:
    pass

print("\033[3;33mIniciando o projeto\033[m")

def quebrar_linha():
    print("\n")
    
from Cliente import Cliente
from time import sleep
from Conta import Conta

c1 = Cliente(str(input("Escreva o nome do cidadão: ")), str(input("Favor digitar o telefone de contato: ")))

quebrar_linha()
sleep(0.5)

print(f"""
Olá \033[3;31m{c1.nome}\033[m! Seja muito bem-vindo(a) ao projeto \033[3;33mConta Bradesco POO\033[m!

Seu telefone de contato é \033[3;31m{c1.telefone}\033[m
E o seu ID é: \033[3;31m{c1}\033[m

""")

quebrar_linha()
sleep(0.5)

conta = Conta(c1.nome, int(input("Qual é o seu número de conta: ")), float(input("Digite o seu saldo: R$")))

sleep(1.5)

print(f"""
Titular: \033[3;31m{conta.titular}\033[m
Número da conta: \033[3;31m{conta.numero}\033[m
Saldo: \033[3;31mR${conta.saldo}\033[m
""")

