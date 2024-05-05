# Escrevendo arquivos txt:

arquivo = open("./DIO/leitura_docs_py/lorem_ipsum.txt", "w")

arquivo.write("Escrevendo dado em um novo arquivo.")

arquivo.writelines(["\n", "Escrevendo ", " um ", " novo ", " texto ", "\n"])

arquivo.write("\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras et viverra lacus. Quisque nec euismod erat. Quisque vitae nisi ac risus dignissim laoreet. Donec tempor dui vel felis tempor dictum. Praesent massa neque, varius nec diam at, lacinia volutpat nibh. Sed vel tempus quam. Phasellus tincidunt dui quis ipsum auctor imperdiet. Quisque varius ultrices orci. Praesent luctus porta mauris, vel blandit nibh. Vivamus volutpat tincidunt rhoncus. Curabitur ac convallis ipsum. Sed iaculis vehicula felis et dictum. Nulla volutpat eget nibh vitae auctor.Nulla eu dolor non risus dignissim congue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras\n")

arquivo.write("\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras et viverra lacus. Quisque nec euismod erat. Quisque vitae nisi ac risus dignissim laoreet. Donec tempor dui vel felis tempor dictum. Praesent massa neque, varius nec diam at, lacinia volutpat nibh. Sed vel tempus quam. Phasellus tincidunt dui quis ipsum auctor imperdiet. Quisque varius ultrices orci. Praesent luctus porta mauris, vel blandit nibh. Vivamus volutpat tincidunt rhoncus. Curabitur ac convallis ipsum. Sed iaculis vehicula felis et dictum. Nulla volutpat eget nibh vitae auctor.Nulla eu dolor non risus dignissim congue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras Praesent luctus porta mauris, vel blandit nibh. Vivamus volutpat tincidunt rhoncus. Curabitur ac convallis ipsum. Sed iaculis vehicula felis et dictum. Nulla volutpat eget nibh vitae auctor.Nulla eu dolor non risus dignissim congue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras Praesent luctus porta mauris, vel blandit nibh. Vivamus volutpat tincidunt rhoncus. Curabitur ac convallis ipsum. Sed iaculis vehicula felis et dictum. Nulla volutpat eget nibh vitae auctor.Nulla eu dolor non risus dignissim congue. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras\n")

arquivo.close()