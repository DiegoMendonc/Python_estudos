# Prática Encapsulamento:

class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property    # retornar o valor de x 
    def x(self):
        return self._x or 0
    
    @x.setter   # Edição da variavel encapsulado
    def x(self, value):
        self._x += value

    @x.deleter  # Instãncia para deletar o atributo
    def x(self):
        self._x = -1
        
foo = Foo(10)
print(foo.x)

foo.x = 20
print(foo.x)

del foo.x
print(foo.x)