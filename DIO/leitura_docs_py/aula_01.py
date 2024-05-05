# Lendo arquivo txt em Python:

arquivo = open("./DIO/leitura_docs_py/lorem_ipsum.txt", "r")

# print(arquivo.read()) Leitura inteira

# print(arquivo.readline()) leitura por linha
# print(arquivo.readline())
# print(arquivo.readline())

#for linha in arquivo.readlines(): leitura em lista de arquivos
#    print(linha)

while len(linha := arquivo.readline()):    
    print(linha)
    
arquivo.close()