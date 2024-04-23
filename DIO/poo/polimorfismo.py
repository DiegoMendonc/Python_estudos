# Prática em Polimorfismo com herança

class passaro:
    def voar(self):
        print("Voando...")
    
class Pardal(passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(passaro):
    def voar(self):
        print("Avestruz não pode voar...")

class Aviao(passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar()
    
p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

print()
plano_voo(p1)
print()
plano_voo(p2)
print()
plano_voo(p3)
print()
