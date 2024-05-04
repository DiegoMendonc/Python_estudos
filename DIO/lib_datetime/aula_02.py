from datetime import timedelta, datetime, date

def linha_espaco():
    print("~"*40)
    print()
    
def cabecalho(x):
    print("~"*40)
    print(f"{x:^40}")
    print("~"*40)

def espaco():
    print()
    
    
cabecalho("Olá, bem-vindo!")

while True:
    tipo_carro = str(input("Qual o tipo do carro? [P, M ou G] ")).upper()[0]  #P, M ou G
    tempo_pequeno = 1
    tempo_medio = 2
    tempo_grande = 3
    data_atual = datetime.now()
    
    if tipo_carro in "Pp":
        linha_espaco()
        data_estimada = data_atual + timedelta(days=tempo_pequeno)
        print(f"O carro chegou: \033[3;34m{data_atual}\033[m\n\nE ficará pronto às \033[3;35m{data_estimada}\033[m\n")
        break

    elif tipo_carro in "Mm":
        linha_espaco()
        data_estimada = data_atual + timedelta(days=tempo_medio)
        print(f"O carro chegou: \033[3;34m{data_atual}\033[m\n\nE ficará pronto às \033[3;35m{data_estimada}\033[m\n")
        break

    elif tipo_carro in "Gg":
        linha_espaco()
        data_estimada = data_atual + timedelta(days=tempo_grande)
        print(f"O carro chegou: \033[3;34m{data_atual}\033[m\n\nE ficará pronto às \033[3;35m{data_estimada}\033[m\n")
        break

    else:
        linha_espaco()
        print("\033[3;31mFavor, digite o tipo de carro correto [P, M ou G]...\033[m")

# Segunda Operação

print(date.today() - timedelta(days=1))

espaco()

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

espaco()

print(datetime.now().date())