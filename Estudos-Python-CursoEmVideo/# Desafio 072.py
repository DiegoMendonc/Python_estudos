print("="*30)
print("CONVERSOR DE NÚMEROS EXTENSOS")
print("="*30)
print("\n\033[3mBEM-VINDO(A) AO NOSSO CONVERSOR DE 0 À 20!\n")
exten = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", 
         "CINCO", "SEIS", "SETE", "OITO", "NOVE",
         "DEZ", "ONZE", "DOZE", "TREZE", "CATORZE",
         "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO",
         "DEZENOVE", "VINTE")
while True:
    num = int(input("\033[3mDIGITE UM NÚMERO ENTRE 0 À 20: "))
    if 0 <= num <= 20:
        break
    print("\033[3;31mNÚMERO INVÁLIDO!\033[m", end=" ")
print(f"\n\033[3;34mVOCÊ DIGITOU O NÚMERO: {exten[num]}\033[m\n")
print("="*30)