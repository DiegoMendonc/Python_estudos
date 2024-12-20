def menu(x):
    print("-"*50)
    print(x.center(50))
    print("-"*50)
    print()

def esp():
    print()

menu("Métodos de trabalho com Listas em Python")
menu("Método APPEND")
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

esp()
print(f"""
Olá! Bem-vindo!
A lista foi adicionada com os seguintes valores:

\033[3;35m{lista}\033[m
""")
esp()

menu("Método CLEAR")
li = [1, "carro", 1.5, False]

print(li)
esp()

li.clear()
print(li)
esp()

menu("Método COPY")
lis = [1, 2, 3, 8, 10]
l2 = lis.copy()

print(f"A lista original é {lis};\nA lista copiada é: {l2}.")
esp()

print(id(lis), id(l2))
esp()

l2[2] = "DIEGO"
print(l2)
esp()
print(lis)
esp()

menu("Método EXTEND")

lis1 = ["Python", "C", "Java"]

print(lis1)
esp()

lis1.extend(["C++", "Delphi"])
print(lis1)
esp()

menu("Método POP")

print(lis1)
esp()

lis1.pop()  # Remoção no estilo pilha - exemplo de pilha de pratos
print(lis1)
esp()

menu("Método REVERSE")

print(lis1)
esp()

lis1.reverse()
print(lis1)
esp()

menu("Método SORT")

print(lis1)
esp()

lis1.sort() # Ordem Alfabética
print(lis1)
esp()

lis1.sort(reverse=True) # Espelhamento dos itens da lista = caso TRUE
print(lis1)
esp()

lis1.sort(key=lambda x: len(x))
print(lis1)
esp()

lis1.sort(key=lambda x: len(x), reverse=True)
print(lis1)
esp()

menu("FIM")