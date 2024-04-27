import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado
    
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá Mundo! {nome}")
    return nome.upper()
# ola_mundo = meu_decorador(ola_mundo)   
    
print(ola_mundo.__name__)