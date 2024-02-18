print("- "*20)
print("\033[31mO DÉCIMO TERMO DE UMA PA: pt.2\033[m")
print("- "*20)
primeiro = int(input("\nFAVOR DIGITE O PRIMEIRO TERMO: "))
razao = int(input("FAVOR DIGITE A RAZAO: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end ="")
    termo = termo + razao
    cont = cont +1
print("FIM", end="")