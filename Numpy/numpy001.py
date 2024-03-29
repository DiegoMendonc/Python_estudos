import numpy as np
minha_lista = [1, 2, 3]
print("-"*25)
print("\033[5;33mArray de 1 dimensão - Numpy\033[m\n")
print(minha_lista)
d1 = np.array(minha_lista)
print(d1)
print("\nFIM")
print("-"*25)
print("\033[5;34mArray de 2 Dimensão\033[m\n")
minha_matriz = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
d2 = np.array(minha_matriz)
print(minha_matriz)
print()
print(d2)
print("\nFIM")
print("-"*25)
print("\033[5;33mArange em Numpy\033[m\n")
a = np.arange(0, 10, 2)
print(a)
print("\nFIM")
print("-"*25)
print("\033[5;33mMatriz de zeros\033[m\n")
zero = np.zeros((4, 4))
print(zero)
print()
um = np.ones((3, 3))
print(um)
print("\nFIM")
print("-"*25)
print("\033[5;35mMatriz de identidade\033[m\n")
i = np.eye(4)
print(i)
print()
ls = np.linspace(0, 10, 3)
print(ls)
print()
r = np.random.rand(5)
print(r)
print()
rn = np.random.randn(5)
print(rn)
print()
ri = np.random.randint(0, 100, 10)
print(ri)
print()
print("-"*25)
print("\033[3;31mATRIBUTOS E MÉTODOS NO NUMPY\033[m\n")
rn1 = np.random.randn(25)
print(rn1)
print()
print(rn1.reshape(5, 5))
print()
print(rn1.shape)
print(rn1.max)
print(rn1.argmax)