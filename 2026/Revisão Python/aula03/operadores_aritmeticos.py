
def linha():
    print("\n" + "-" * 50 + "\n")  

'''Operadores em Python.'''

'Operadores Aritméticos'

linha()
print(f"\nOperadores Aritméticos\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

linha()

print(f"\nSoma: {num1 + num2}")
print(f"\nSubtração: {num1 - num2}")
print(f"\nMultiplicação: {num1 * num2}")
print(f"\nDivisão: {num1 / num2}")
print(f"\nDivisão Inteira: {num1 // num2}")
print(f"\nResto da Divisão: {num1 % num2}")
print(f"\nExponenciação: {num1 ** num2}")

linha()

expressao = (num1 + num2) * (num1 - num2)
print(f"\nO resultado da expressão ({num1} + {num2}) * ({num1} - {num2}) é: {expressao}\n")

linha()