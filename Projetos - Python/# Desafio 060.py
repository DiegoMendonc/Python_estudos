#Tambem conseguimos transformar pelo módulo: from math import factorial
#f = factorial(n)
#print("O FATORIAL DE {} É {}".format(n, f))
from math import factorial
print("=-"*15)
print("CÁLCULADORA DE FATORIAL")
print("=-"*15)
print("\nVAMOS COMEÇAR!")
n = int(input("\nFavor digite um número para calcular: "))
c = n
f = factorial(n)
print("\n\033[2mCalculando {}! = \033[m".format(n), end ="")
while c > 0:
    print("\033[2m{}\033[m".format(c), end ="") 
    print("\033[2m x \033[m" if c > 1 else " = ", end = "")
    c = c - 1 
print("\033[2m{}\033[m\n".format(f))