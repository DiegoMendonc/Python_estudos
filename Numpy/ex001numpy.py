import numpy as np

print("-"*25)
print("\033[5;34mATIVIDADE 01\033[m\n")
a01 = np.zeros(10)
print(a01)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 02\033[m\n")
a02 = np.ones(10)
print(a02)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 03\033[m\n")
a03 = a02.copy() * 5
print(a03)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 04\033[m\n")
a04 = np.arange(10, 51, 1)
print(a04)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 05\033[m\n")
a05 = np.arange(10, 51, 2)
print(a05)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 06\033[m\n")
a06 = np.arange(0, 9).reshape(3, 3)
print(a06)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 07\033[m\n")
a07 = np.eye(3, 3)
print(a07)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 08\033[m\n")
a08 = np.random.rand(1)
print(a08)
print()
print("-"*25)


print("-"*25)
print("\033[5;34mATIVIDADE 09\033[m\n")
a09 = np.random.randn(25)
print(a09)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 10\033[m\n")
a10 = np.arange(0, 101) / 100
print(a10)
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 11\033[m\n")
a11 = np.linspace(0, 1, 20)
print(a11) 
print()
print("-"*25)

print("\033[5;31mSEGUNDA ETAPA\033[m\n")
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print()
print("-"*25)
print("\033[5;34mATIVIDADE 12\033[m\n")
print(mat[2:, 1:])
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 13\033[m\n")
print(mat[3, 4])
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 14\033[m\n")
print(mat[:3, 1:2])
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 15\033[m\n")
print(mat[4:])
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 16\033[m\n")
print(mat[3:, :])
print()
print("-"*25)

print("\n\033[3;31mOperações Matemáticas\033[m\n")
print("-"*25)
print("\033[5;34mATIVIDADE 17\033[m\n")
print(np.sum(mat))
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 18\033[m\n")
print(np.std(mat))
print()
print("-"*25)

print("-"*25)
print("\033[5;34mATIVIDADE 18\033[m\n")
print(mat.sum(axis=0))
print(mat.sum(axis=1))
print()
print("-"*25)