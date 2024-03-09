def menu(x):
    print("-"*50)
    print(x.center(50))
    print("-"*50)
    print()

def esp():
    print()

menu("TUPLAS em Python")
print("""      
Tuplas são idênticas na execução e manuseio com as listas, PORÉM, 
as tuplas são imutáveis, limitando muito o manuseio da tupla
""")
frutas = ("laranja", "maca", "uva")
print(frutas)
esp()

numeros = tuple([1, 2, 3, 4])
print(numeros)
esp()

pais = ("Brasil", )
print(pais)

menu("Utilizando as tuplas")

print(frutas)
print()

print(frutas[::-1])
esp()

print(frutas[2])
esp()