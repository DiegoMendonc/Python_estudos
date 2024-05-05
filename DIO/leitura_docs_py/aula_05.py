from pathlib import Path

def linha():
    print("~"*40)
    
ROOTH_PATH = Path(__file__).parent

try:  # Realizando verificação de erros se o arquivo vai ser lido com sucesso.
    
    with open(ROOTH_PATH / "123.txt", "r") as arquivo:     # Utilizando with vai deixar a linha de código segura.
        print(arquivo.read())

except IOError as exc:
    linha()
    print(f"\nNão foi possível abrir o erro:\n{exc}")
    linha()

try:
    with open(ROOTH_PATH / "arquivo_utf_8.txt", "w", encoding="UTF-8") as arquivo1:
        arquivo1.write("Aprendendo a manipular arquivos utilizando Python...")
        arquivo1.write("\n\nHELLO WORLD!\n")
except IOError as exc:
    print(f"\nErro ao abrir o arquivo:\n{exc}\n")
