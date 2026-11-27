'''Operadores de Comparação em Python'''
def linha():
    print("\n" + "-" * 50 + "\n")

linha()
print(f"\nOperadores de Comparação\n")
saldo_bancario = 1000.00
valor_saque = float(input("Digite o valor do saque: "))
linha()

print(f"\nSaldo bancário: {saldo_bancario}")
print(f"\nValor do saque: {valor_saque}")

linha()

print(f"\nSaldo bancário é igual ao valor do saque? {saldo_bancario == valor_saque}")
print(f"\nSaldo bancário é diferente do valor do saque? {saldo_bancario != valor_saque}")
print(f"\nSaldo bancário é maior que o valor do saque? {saldo_bancario > valor_saque}")
print(f"\nSaldo bancário é menor que o valor do saque? {saldo_bancario < valor_saque}")
print(f"\nSaldo bancário é maior ou igual ao valor do saque? {saldo_bancario >= valor_saque}")
print(f"\nSaldo bancário é menor ou igual ao valor do saque? {saldo_bancario <= valor_saque}")
print(f"\nO valor do saque é positivo? {valor_saque > 0}")
print(f"\nO valor do saque é negativo? {valor_saque < 0}")
print(f"\nO valor do saque é zero? {valor_saque == 0}")
print(f"\nO valor do saque é diferente de zero? {valor_saque != 0}")
print(f"\nO valor do saque é maior que zero e menor ou igual ao saldo bancário? {valor_saque > 0 and valor_saque <= saldo_bancario}")
print(f"\nO valor do saque é menor que zero ou maior que o saldo bancário? {valor_saque < 0 or valor_saque > saldo_bancario}")
print(f"\nO valor do saque é maior que zero e menor ou igual ao saldo bancário? {0 < valor_saque <= saldo_bancario}")
print(f"\nO valor do saque é menor que zero ou maior que o saldo bancário? {valor_saque < 0 or valor_saque > saldo_bancario}")
print(f"\nO valor do saque é maior que zero e menor ou igual ao saldo bancário? {0 < valor_saque <= saldo_bancario}")
print(f"\nO valor do saque é menor que zero ou maior que o saldo bancário? {valor_saque < 0 or valor_saque > saldo_bancario}")
print(f"\nO valor do saque é maior que zero e menor ou igual ao saldo bancário? {0 < valor_saque <= saldo_bancario}")

linha()
