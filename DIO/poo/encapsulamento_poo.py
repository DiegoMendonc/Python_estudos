# Encapsulamento

def cabecalho(x):
    
    print("-"*50)
    print(f"{x:^50}")
    print("-"*50)

def linha():
    
    print("~"*25)

class conta:
    
    def __init__(self, nro_agencia, saldo=float(0), ):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self, valor):
        # ...
        self._saldo += valor
    
    def sacar(self, valor):
        # ...
        self._saldo -= valor
    
    def mostrar_saldo(self):
        # ...
        return f"\nO valor total é de: R${self._saldo}"
    
# Programa:
cabecalho("ANTES DE COMEÇAR, FAVOR INSIRA SUA CONTA: ")

con = str(input("Favor, insira qual é a sua conta: "))
print()
    
cabecalho("BEM-VINDOS AO BANCO DIMDIM!")
print("""
FAVOR SELECIONE QUAL OPERAÇÃO DESEJA INICIAR:

[0] SALDO
[1] SACAR
[2] DEPOSITAR
[3] SAIR

""")

while True:
    
    cc = conta (con, 0)
    
    choice = int(input("OPÇÃO: "))
   
    
    if choice == 0:
        
        print(cc.mostrar_saldo())
        linha()
        
    elif choice == 1:
        
        saque = float(input("Favor informe o valor de saque: R$"))
        saque = cc ()
        linha()
        
    elif choice == 2:
        
        deposito = float(input("Favor informe o valor de depósito: R$"))
        cc += deposito
        
    elif choice == 3:
        
        print("\nMuito obrigado por utilizar a aplicação!")
        linha()
        break
    
    else:
        print("\033[3;31mCÓDIGO INSERIDO INCORRETO, FAVOR DIGITAR O CÓDIGO CORRETO!\033[m")