print("~"*30)
print("ANALISADOR DE DADOS")
print("~"*30)
n = (int(input("DIGITE UM VALOR: ")), int(input("DIGITE MAIS UM VALOR: ")), 
     int(input("DIGITE O PENÚLTIMO VALOR: ")), int(input("DIGITE O ÚLTIMO VALOR: ")))
print("~"*30)
print(f"Os valores digitados foram agrupados em: {n}")
print(f"O tipo desta variável é: {type(n)}")
print("~"*30)
print(f"O VALOR 9 APARECE \033[34m{n.count(9)} VEZES\033[m")
if 3 in n:
    print(f"O VALOR 3 APARECE NA \033[31m{n.index(3) + 1}ª POSIÇÃO\033[m")
else:
    print(f"O VALOR 3 NÃO FOI DIGITADO EM \033[31mNENHUMA POSIÇÃO!\033[m")
print("A VALORES DE NÚMEROS PARES SÃO: ", end= "")
for num in n:
    if num % 2 == 0:
        print(f"\033[33m{num}\033[m", end=" ")
print("\n\nMUITO OBRIGADO POR UTILIZAR A APLICAÇÃO!")
print("~"*30)
