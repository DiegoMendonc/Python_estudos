import random
import csv
import os
from pathlib import Path
from time import sleep
import subprocess

ROOTH_PATH = Path(__file__).parent

def cabecalho(x):
    print("~"*50)
    print(f"{x:^50}")
    print("~"*50)

def linha():
    print("~"*50)
    
def espaco():
    print()
    
def abrir_excel_com_csv(arquivo_csv):
    if not os.path.exists(arquivo_csv):
        print(f'O arquivo "{arquivo_csv}" não foi encontrado...')
        return

    if not any(os.access(os.path.join(path, 'excel.exe'), os.X_OK) for path in os.environ["PATH"].split(os.pathsep)):
        print('O Microsoft Excel não está instalado neste computador.')
        return
    
    subprocess.Popen(['excel', arquivo_csv])

cabecalho("ROLETA RUSSA - GAME")
espaco()

number = random.randint(1,6)
roleta = int(input("Escolha um número entre 1 e 6: "))
espaco()
linha()

while True:
    espaco()
    choice = str(input("TEM CERTEZA QUE DESEJA JOGAR? [S/N] ")).upper().strip()[0]
    if choice in "Ss":
        print("\nCOMEÇAREMOS ENTÃO...\n")
        sleep(1.5)
        print("3\n")
        sleep(1)
        print("2\n")
        sleep(1)
        print("1\n")
        sleep(1.5)
        print("0\n")
        sleep(1)
        linha()
    
        if roleta == number:
            print("\033[3;34mVocê venceu, campeão!\033[m")
            break

        else:
            try:
                with open(ROOTH_PATH / "DERROTA.csv", "w") as arquivo:
                    escritor = csv.writer(arquivo)
                    escritor = csv.writer(arquivo)
                    escritor.writerow(["TÍTULO"])
                    escritor.writerow(["DE"])
                    escritor.writerow(["PERDEDOR"])
                    escritor.writerow(["HAHAHAHAHAHAHHAHAHAHA"])
                    arquivo_csv = "..\GitHub\Estudos_Python\Python_estudos\DIO\PASTA_DA_BRINCADEIRA\DERROTA.csv"
                    cabecalho("DESLIGANDO O SISTEMA OPERACIONAL EM...")
                    linha()
                    print("\n3...\n")
                    sleep(2)
                    print("2\n")
                    sleep(1.5)
                    print("1\n")
                    sleep(2)
                    print("0\n")
                    cabecalho("TCHAUZINHO!")
                    os.system('shutdown /s /t 0')
                    break
            except IOError as exc:
                print(f"ERRO AO ABRIR O ARQUIVO!\n\n- {exc}\n")
    elif choice in "Nn":
        espaco()
        cabecalho("MUITO OBRIGADO POR ENTRAR E ATÉ A PRÓXIMA!")
        break
    else:
        espaco()
        linha()
        print("\033[3;31mFAVOR RESPONDER CORRETAMENTE!\033[m")