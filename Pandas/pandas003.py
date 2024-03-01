import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())
print("-"*25)
print("\033[3;34mAULA SOBRE DATAFRAMES pt.2\033[m\n")
print(df)
print("-"*25)

print(df > 0)
print()
print("-"*25)

bol = df > 0
print(df[bol])
print("-"*25)
print()

print(df[df["W"] > 0])
print("-"*25)
print()

print(df[df["W"] > 0]["Y"])
print("-"*25)
print()

print("\033[3;33mUTILIZAÇÃO DO INDEX\033[m\n")
print(df.reset_index)
print()
print(df)
print()

print("-"*25)
col = "RS RJ SP AM SC".split()
print(col)
print()
df["Estado"] = col
print(df)
print()

print("-"*25)
print(df.set_index("Estado"))
print()
print(df)
print()