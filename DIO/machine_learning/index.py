import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression as mr

def titulo(x):
    print("~"*50)
    print(f"{x:^50}")
    print("~"*50)

def espace():
    print()
    
x, y = mr(n_samples=200, n_features=1, noise=30)
titulo("Utilizando Matplotlib: Machine Learning intro.")
espace()
plt.scatter(x, y)
plt.show()