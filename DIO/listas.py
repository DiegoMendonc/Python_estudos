def menu(x):
    print("-"*50)
    print(x.center(50))
    print("-"*50)
    print()

def esp():
    print()
    
    
menu("LISTAS")

frutas = ["laranja", "maca", "uva"]
print(frutas)
esp()

frutas1 = []
print(frutas1)
esp()

letras = list("python")
print(letras)
esp()

numeros = list(range(10))
print(numeros)
esp()

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)
esp()

menu("ÍNDICES")

print(frutas)
esp()
print(frutas[-1])
esp()
print(frutas[-3])
esp()

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz)
esp()

print(matriz[0])
esp()

print(matriz[0][0])
esp()

print(matriz[0][-1])
esp()

print(matriz[-1][-1])
esp()

menu("FATIAMENTO")

lis = ["p", "y", "t", "h", "o", "n"]
print(lis)
esp()

print(lis[2:])
esp()

print(lis[:2])
esp()

print(lis[1:3])
esp()

print(lis[0:3:2])
esp()

print(lis[::])
esp()

print(lis[::-1])
esp()

menu("Iteração de Listas - FOR")
car = ["GOL", "CELTA", "PALIO"]
print(car)
esp()

print("Leitura com for")
for car in car:
    print(car)
esp()
for indice, car in enumerate(car):
    print(f"{indice}: {car}")

menu("Compreensão de Listas")
num = [1, 30, 21, 2, 9, 65, 34]
pares = []
impares = []

for numero in num:
    if numero % 2 == 0:
         pares.append(numero)
    elif numero % 2 != 0:
        impares.append(numero)
         
print(f"A lista completa é: {num};\n")
print(f"Os números pares são: {pares};\n")
print(f"Os números ímpares são: {impares}\n")
esp()

menu("MODIFICANDO VALORES")
nume = [2, 4, 8, 10, 12]
quadrado = []

for numero in nume:
    quadrado.append(numero ** 2)

print(f"A lista original é: {nume}\n")
esp()
print(f"A lista elevado ao quadrado é: {quadrado}\n")
esp()

menu("FIM")
