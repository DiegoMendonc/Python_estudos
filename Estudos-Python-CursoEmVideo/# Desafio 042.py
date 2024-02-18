# Desafio 042 - Nomenclatura de Triângulos
import emoji
print("\033[44m- \033[m"*20)
print(emoji.emojize("\033[2;40mDesafio 042: Cálculo de Triângulos 📐\033[m"))
print("\033[44m- \033[m"*20)
x1 = float(input("\n\033[2mFavor digite o primeiro segmento: \033[m"))
x2 = float(input("\033[2mFavor digite o segundo sagmento: \033[m"))
x3 = float(input("\033[2mFavor digite o terceiro segmento: \033[m"))
if x1 < x2 + x3 and x2 < x1 + x3 and x3 < x1 + x2:
    print(emoji.emojize("\n\033[7;35;43mOs segmentos acima PODEM FORMAR UM TRIÂNGULO ✌\033[m\n"))
    if x1 == x2 == x3:
        print("\033[2mTRIÂNGULO EQUILÁTERO!\033[m")
    elif x1 != x2 != x3 != x1:
        print("\033[2mTRIÂNGULO ESCALENO!\033[m")
    else:
        print("\033[2mTRIÂNGULO ISÓCELES!\033[m")
else:
    print(emoji.emojize("\n\033[2;30;41mOs segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO 👎\033[m"))
print("\n\033[2mMUITO OBRIGADO POR UTILIZAR ESSE APLICATIVO! \033[m")