# Atributos de classes em Python:

class estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
        
al01= estudante("Guilherme", 5502)
al02 = estudante("Giovana", 6606)
print()
mostrar_valores(al01, al02)
print()

estudante.escola = "Python"
al03 = estudante("Chappie", 3)
mostrar_valores(al01, al02, al03)
print()
