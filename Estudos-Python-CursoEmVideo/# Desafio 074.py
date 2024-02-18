from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),
     randint(1,10))
print(f"Os valores sorteados na tupla são: ", end="")
for n in num:
    print(f"\033[3;33m{n}\033[m", end=" ")
print(f"\nO maior valor sorteado foi: {max(num)}")
print(f"O menor valor sorteado foi: {min(num)}")