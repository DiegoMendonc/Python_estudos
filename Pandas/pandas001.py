import numpy as np
import pandas as pd

labels = ["a", "b", "c"]
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {"a":10, "b":20, "c":30}

series = pd.Series(minha_lista, labels)

print(series["b"])
print("-"*50)
print()

ser1 = pd.Series([1, 2, 3, 4], ["EUA", "Alemanha", "URSS", "JPN"])
print(ser1)
print("-"*50)
print()

ser2 = pd.Series([1, 2, 3, 4], ["EUA", "Alemanha", "Itália", "JPN"])
print(ser2)
print("-"*50)
print()

print(ser1 + ser2)
print("-"*50)
print()