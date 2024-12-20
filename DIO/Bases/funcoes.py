def menu(x):
    print("-"*50)
    print(x.center(50))
    print("-"*50)
    print()

def esp():
    print()

def mensagem1(nome="Anônimo"):
    print(f"Seja muito bem-vindo(a) Sr(a) {nome}!")
    esp()

def retorna_num(num):
    antecessor = num - 1
    sucessor = num + 1
    
    return antecessor, sucessor

menu("FUNÇÕES")
mensagem1()
mensagem1("Diego")
esp()
retorna_num(5)

menu("PARÂMETROS ESPECIAIS")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação de {a} e {b} é = {resultado}")
    
resultado(10, 20, somar)
esp()
resultado(20, 10, subtrair)
esp()

menu("ESCOPO GLOBAL")

salario = float(input("Favor digite o valor do seu salário: R$"))

def bonus_salario(bonus):
    global salario
    salario += bonus
    esp()
    return f"O valor do salário acrescido com o bonús é: \033[3;31mR${salario:.2f}\033[m\n"
    

salario_com_bonus = bonus_salario(300)
print(salario_com_bonus)