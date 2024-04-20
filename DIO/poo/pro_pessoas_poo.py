class Pessoas:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return 2024 - self._ano_nascimento
    
    
pessoa = Pessoas("Diego", 1997)
print(f"Nome: {pessoa.nome}\t Idade: {pessoa.idade} anos")