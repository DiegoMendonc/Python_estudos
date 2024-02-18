from emoji import emojize
print("="*30)
print("\033[33mDETECTOR DE PALÍNDROMOS 📝\033[m")
print("="*30)
frase = str(input("\nFavor digite um frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print("\n\033[36mO inverso da frase digitada é:\033[m\033[32m {}\033[m\n".format(inverso))
if inverso == junto:
    print("\n\033[33mTEMOS UM PALÍNDROMO\033[m\n")
else:
    print("\n\033[31mA FRASE NÃO É UM PALÍNDROMO\033[m\n")
print("="*30)
print(emojize("\033[2mMUITO OBRIGADO POR UTILIZAR O APLICATIVO ✅\033[m"))
print("="*30)