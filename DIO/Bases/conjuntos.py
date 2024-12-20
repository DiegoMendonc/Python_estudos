def menu(x):
    print("-"*50)
    print(x.center(50))
    print("-"*50)
    print()

def esp():
    print()

menu("Explorando CONJUNTOS em Python - SET")

print(set([1, 2, 3, 1, 3, 4]))
esp()

print(set("abacaxi"))
esp()

print(set(("palio", "celta", "uno")))
esp()

menu("Manipulando dados com SET - com dicionários")

numeros = {1, 2, 3, 2, 1}
numeros = list(numeros)

print(numeros)
esp()

print(numeros[0])
esp()

menu("Conjuntos Matemáticos com SET")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(f"O conjunto A é: {conjunto_a}")
print(f"O conjunto B é: {conjunto_b}")
esp()

menu("União de conjuntos")

print(f"A União entre A e B é: {conjunto_a.union(conjunto_b)}")
esp()

menu("Intersecção de conjuntos")

print(f"A intersecção entre A e B é: {conjunto_a.intersection(conjunto_b)}")
esp()

menu("Diferença de conjuntos")

print(f"A Diferença entre A e B é: {conjunto_a.difference(conjunto_b)}\n")
print(f"A Diferença entre B e A é: {conjunto_b.difference(conjunto_a)}")
esp()

menu("Diferença Simétrica de Conjuntos")

print(f"A diferença simétrica entre A e B é: {conjunto_a.symmetric_difference(conjunto_b)}")
esp()

menu("Subconjunto de conjuntos")
conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

print(f"O conjunto C é: {conjunto_c}\nO conjunto D é: {conjunto_d}")
esp()

print(f"O conjunto C é subconjunto de D: {conjunto_c.issubset(conjunto_d)}\n")
print(f"O conjunto D é subconjunto de C: {conjunto_d.issubset(conjunto_c)}")
esp()

menu("Disconjunto de conjuntos")
conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}
conjunto_e = {0, 10}

print(f"O conjunto C é: {conjunto_c}\nO conjunto D é: {conjunto_d}\nO conjunto E é: {conjunto_e}")
esp()

print(f"O conjunto D é disconjunto de C: {conjunto_c.isdisjoint(conjunto_c)}\n")
print(f"O conjunto E é disconjunto de C: {conjunto_e.isdisjoint(conjunto_c)}")
esp()
