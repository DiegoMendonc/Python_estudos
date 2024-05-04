import pytz
from datetime import datetime, timezone, timedelta

def espaco():
    print()
    
def cabecalho(x):
    print("~"*30)
    print(f"{x:^30}")
    print("~"*30)

cabecalho("Utilizando PYTZ:")

data = datetime.now(pytz.timezone("Europe/Oslo"))
data_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

espaco()
print(data)
espaco()
print(data_2)
espaco()

#Utilizando TimeZone sem Pytz:
cabecalho("Utilizando Timezone:")
espaco()

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
espaco()
print(data_sp)
espaco()