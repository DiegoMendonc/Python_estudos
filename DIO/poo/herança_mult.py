# Herança Múltipla

class animal:
    
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"
               
class ave(animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
    def __str__(self):
        return "Ave"     
    

class mamifero(animal):
    def __init__(self,  cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    
    def __str__(self):
       return __class__.__name__
        

class gato(mamifero):
    pass

class ornitorrinco(mamifero, ave):
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        print(ornitorrinco.__mro__)
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
    
    def __str__(self):
        return "Ornitorrinco"

cat = gato(nro_patas=4, cor_pelo="preto")
print(cat)

orni = ornitorrinco(nro_patas=2, cor_pelo="vermeho", cor_bico="laranja")
print(orni)