from datetime import datetime

def espaco():
    print()

data_atual = datetime.now()
data_hora_str = "2024-10-20 10:30"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

espaco()
print(data_atual.strftime(mascara_ptbr))
print(type(data_atual.strftime(mascara_ptbr)))
espaco()

print(datetime.strptime(data_hora_str, mascara_en))
print(type(datetime.strptime(data_hora_str, mascara_en)))
espaco()