# Interfaces e Classes Abstratas:
from abc import ABC, abstractmethod, abstractproperty
from time import sleep

class controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        return "LG"
    
class controle_tv(controle_remoto):
    def ligar(self):
        print("Ligando a TV...")
        sleep(1.5)
        print("...")
        sleep(1)
        print("TV LIGADA!!")
        
    def desligar(self):
        print("Desligando a TV...")
        sleep(1.5)
        print("...")
        sleep(1)
        print("TV DESLIGADA!!")

class controle_ar_condicionado(controle_remoto):
    def ligar():
        print("Ligando o ar...")
        sleep(1.5)
        print("...")
        sleep(1)
        print("AR LIGADO!!")
        
    def desligar(self):
        print("Desligando o ar...")
        sleep(1.5)
        print("...")
        sleep(1)
        print("AR DESLIGADA!!")
         
controle = controle_tv()
controle.ligar()
print()
controle.desligar()

print()
controle = controle_ar_condicionado()
controle.ligar()