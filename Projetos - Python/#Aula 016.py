# Conceito de Variáveis Compostas - Tuplas () - Listas [] - Dicionários {}:
print("~"*25)
print("TUPLAS")
print("~"*25)
lanche = ("hambúrguer", "suco", "pizza", "pudim", "batata")
for cont in range (0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("~"*25)
print(lanche[1])
print(lanche[:-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print("~"*25)
for c in lanche:
    print(c, end=", ") 
print("FIM")
print("~"*25)
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida}! Na posição {pos}")