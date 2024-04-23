# Metodos e Classes estaticas:

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
      
# p = Pessoas("Diego", 27)
# rint(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1997, 7, 7, "Diego")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))