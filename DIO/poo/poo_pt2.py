class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")
        
    def falar(self):
        print("auau")
      
        
def criar_cachorro():
    d = cachorro("Zeus", "Branco e Preto", False)
    print(d.nome)

#criar_cachorro()

        
c = cachorro("Chppie", "amarelo")
c.falar()

print("Hello World!")
print("Hello World!")
del c

print("Hello World!")
print("Hello World!")