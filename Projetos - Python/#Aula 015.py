print("~"*30)
print("AULA 015: UTILIZAÇÃO DO BREAK")
print("~"*30)
print("\nSEJA MUITO BEM VINDO(A) EM NOSSO APLICATIVO!\n")
nome = str(input("OLÁ, QUAL O SEU NOME? "))
print(f"\n\033[2;30;43mPRAZER EM TE CONHECER, {nome}!\033[m\n")
choice = str(input("DESEJA COMEÇAR? [S/N] ").upper().strip()[0])
if choice in "Ss": 
    n = s = cont = 0
    while True:
        n = int(input("DIGITE UM NÚMERO: [999 P/CANCELAR] "))
        if n == 999:
            break
        cont += 1
        s += n
    print(f"\nA SOMA DOS VALORES INFORMADOS É DE: \033[31m{s}\033[m\n")
elif choice in "Nn":
    print(f"\nTUDO BEM ENTÃO, {nome}!")
else:
    while choice not in "Ss" and choice not in "Nn":
        choice = str(input("\nNÃO ENTENDI A RESPOSTA.. VOCÊ DESEJA EXECUTAR O PROGRAMA? [S/N] ").upper().strip()[0])
print("~"*30)
print(f"MUITO OBRIGADO POR UTILIZAR O PROGRAMA! {nome}")
print("~"*30)