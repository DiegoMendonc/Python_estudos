print("="*30)
print("{:^30}".format("BANCO DO DIEGUINHO"))
print("="*30)
valor = int(input("\033[mQUANTO DESEJA SACAR? R$\033[m"))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"\033[3mTOTAL DE {total_ced} CÉDULAS de R${ced}.\033[m")
        if ced == 50:
            ced = 20
            total_ced = 0
        elif ced == 20:
            ced = 10
            total_ced = 0
        elif ced == 10:
            ced = 1
            total_ced = 0
        if total == 0:
            break
print("="*25)
print("\033[3mMUITO OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS!\033[m")
print("="*25)