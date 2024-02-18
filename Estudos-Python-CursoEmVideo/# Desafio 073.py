print("="*25)
print("\033[3;33mORDEM DOS TIMES\033[m")
print("="*25)
times = ("América-MG", "Athletico-PR", "Atlético-MG", "Bahia", "Botafogo", "Corinthians",
    "Coritiba", "Cruzeiro", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", 
    "Grêmio", "Internacional", "Palmeiras", "Bragantino", "Santos", "São Paulo",
    "Vasco da Gama")
print(type(times))
print(len(times))
print("\033[2;31m-\033[m"*30)
print("\033[3;33mTODOS OS TIMES SÃO:", times)
print("\033[2;31m-\033[m"*30)
print("\033[3;33mOS 5 PRIMEIROS TIMES SÃO:\033[m", times[0:5])
print("\033[2;31m-\033[m"*30)
print("\033[3;33mOS 4 ÚLTIMOS SÃO:\033[m", times[16:])
print("\033[2;31m-\033[m"*30)
print("\033[3;33mOS TIMES EM ORDEM ALFABÉTICA SÃO:\033[m", sorted(times))
print("\033[2;31m-\033[m"*30)
cont = enumerate(times)
choice = 0
while True:
    choice = int(input("\033[3;34mQUAL TIME DESEJA SELECIONAR? [0-19] \033[m"))
    if choice <= 19:
        choice == cont
        print(f"\n\033[3;33mO TIME SELECIONADO FOI: \033[3;34m{times[choice]}\033[m \033[3;33me está na \033[m\033[3;34m{(choice) + 1}ª posição\033[m")
        break
print("\033[2;31m-\033[m"*30)