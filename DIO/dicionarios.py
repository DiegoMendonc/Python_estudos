def menu(x):
    print("-"*50)
    print(x.center(50))
    print("-"*50)
    print()

def esp():
    print()

menu("DICIONÁRIOS")

pessoa = {"nome": "Guilherme", "idade": 18}
print(pessoa)
esp()
print(type(pessoa))
esp()
print("ACRESCENTANDO DADOS\n")
pessoa ["telefone"] = "3333-1234"
print(pessoa)
esp()

pessoa1 = dict(nome="guilherme", idade=18)
print(pessoa1)
esp()
print(type(pessoa1))
esp()

menu("DICIONÁRIOS ANINHADOS")

while True:
    cadastro = {
        str(input("Favor digite o email para cadastro: ")): {"Nome": str(input("Nome: ")), "Telefone": input("Telefone: ")}
                                                                        
    }
    choice = str(input("Deseja finalizar o cadastro? [S/N]")).strip().upper()[0]
    esp()
    if choice in "Ss":
        break
    else:
       cadastro += cadastro
       continue
       
esp()
print(cadastro)
esp()
for chave, valor in cadastro.items():
    print(chave, valor)
    esp()

menu("Método KEYS")

novo_dic = {
    "guilher@gmail.com": {"nome": "Guilerme", "telefone": "3333-124"}
}

print(novo_dic)
esp()
print(novo_dic.keys())