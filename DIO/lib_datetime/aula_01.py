from datetime import date, datetime, time

def linha():
    print()
    print("~"*25)

linha()

#Data personalizada:
data = date(2024, 5, 1)
print(data)
linha()

#Data atual:
hoje = date.today()
print(hoje)
linha()

#Data-Hora personalizada:
data_hora = datetime(2024, 5, 1, 10, 30, 20) # Caso repassar horário sem info - retorna 00:00:00 #
print(data_hora)
linha()

#Data-Hora Atual:
print(datetime.today())
linha()

# Hora Personalizada:
hora = time(10, 20, 0)
print(hora)
linha()

