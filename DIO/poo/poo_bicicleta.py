from time import sleep

def espaco():
    print()
    
class bicicleta:
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim Plim...")
        espaco()
        
    def parar(self):
        print("Parando a bicicleta")
        sleep(0.5)
        print("...")
        sleep(1)
        print("Parou!")
        espaco()
        
    def correr(self):
        print("Vrummmmmmm!....")
        espaco()

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"
               
               
b1 = bicicleta("vermelha", "caloi", 2022, 600)
b2 = bicicleta("verde", "monark", 2000, 199)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor,"->", b1.modelo,"->", b1.ano,"->", b1.valor)

b2.buzinar() # <- instância é igual à bicicleta.buzinar(b2)

print(b2)