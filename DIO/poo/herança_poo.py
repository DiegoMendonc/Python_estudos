# HERANÇA
from time import sleep

class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor...")
        sleep(1.5)
        print("...")
        sleep(1)
        print("Motor ligado com sucesso!!")
        sleep(0.5)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}" 
    
class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"Está carregado" if self.carregado else "Não está carregado")

moto = motocicleta("preta", "ABC-1234", 2)
car = carro("branco", "XDE-0098", 4)
camin = caminhao("roxo", "GFD-1231", 8, False)

print(moto, car, camin)
