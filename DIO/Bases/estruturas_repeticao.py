def linha():
    print("-"*25)
    
linha()
print("FOR...")
linha()
print()    
texto = str(input("Informe uma palavra: "))
vogal = "AEIOU"
print()

for letra in texto:
    if letra.upper() in vogal:
        print(letra, end="")

print()

for numero in range (0, 11):
    print(numero, end=" ")

print()   

for cinco in range(0, 51, 5):
    print(cinco, end=" ")
