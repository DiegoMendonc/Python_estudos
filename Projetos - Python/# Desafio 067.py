from emoji import emojize
print("~"*25)
print(emojize("GERADOR DE TABUADA ✌ ✌ ✌"))
print("~"*25)
print(emojize("\033[2;31mOlá! Seja muito bem-vindo(a) na geradora de tabuadas! 🤙\033[m"))
nome = str(input(emojize("\nQual é o seu nome? 🤔 ")))
print(f"\nMuito prazer em te conhecer, {nome}!")
print("~"*25)
choice = str(input("VAMOS COMEÇAR? [S/N] ")).strip().upper()[0]
if choice in "Ss":
    print("~"*25)
    num = int(input("\033[2;33mFAVOR DIGITE UM NÚMERO PARA GERAR SUA TABUADA 🔥 -> \033[m"))
    while True:
        print("-"*30)
        print(f""" 
{num} X 0 = {num * 0}
{num} X 1 = {num * 1}
{num} X 2 = {num * 2}
{num} X 3 = {num * 3}
{num} X 4 = {num * 4}
{num} X 5 = {num * 5}
{num} X 6 = {num * 6}
{num} X 7 = {num * 7}
{num} X 8 = {num * 8}
{num} X 9 = {num * 9}
{num} X 10 = {num * 10}
              """)
        print("-"*30)
        num = int(input("\033[2;33mFAVOR DIGITE UM NÚMERO PARA GERAR SUA TABUADA 🔥 -> \033[m"))
        if num < 0:
            print("~"*25)
            print("\033[31mNÚMERO NEGATIVO INFORMADO, APLICAÇÃO SERÁ ENCERRADA!\033[m")
            break
elif choice in "Nn":
    print("~"*25)
    print(emojize("\n\033[2;33mTudo bem então! Estaremos finalizando o aplicativo.\033[m\n"))
else:
    print("\033[2;31mCOMANDO INVÁLIDO, FAVOR REINICAR A APLICAÇÃO!\033[m")
print("~"*25)
print(emojize("MUITO OBRIGADO POR UTILIZAR A APLICAÇÃO!\nTENHA UM BOM DIA/TARDE/NOITE! ☀🪐🌘"))
print("~"*25)