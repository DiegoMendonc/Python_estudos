
def calculadora(operacao):
    def soma(a, b):
        return f"O resultado da operação é: {a + b}"
    
    def sub(a, b):
        return f"O resultado da operação é: {a - b}"
    
    def mult(a, b):
        return f"O resultado da operação é: {a * b}"
    
    def div(a, b):
        return f"O resultado da operação é: {a / b}"
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div
        
def cabecalho(x):
    print("~"*25)
    print(f"{x:^25}")
    print("~"*25)
    
cabecalho("Calculadora Rápida")
a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = str(input("Qual operação deseja realizar? (+, -, * , /): "))
print()
print(calculadora(c)(a, b))