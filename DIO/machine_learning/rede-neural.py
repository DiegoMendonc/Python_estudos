import numpy as np
import torch
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
from time import time
from torchvision import datasets, transforms
from torch import nn, optim

transform = transforms.ToTensor()  # -> Definindo a conversão de imagem para tensor

trainset = datasets.MNIST('./MNIST_data/', download=True, train=True, transform=transform) # -> Carrega a parte de treino do dataset
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True) # -> Cria o buffer para pegar os dados por partes

valset = datasets.MNIST('./MNIST_data/', download=True, train=False, transform=transform) # -> Carrega parte da validação do dataset
valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True) # -> Cria um buffer para pegar os dados por partes 

class Modelo(nn.Module):
    def __init__(self):
        super(Modelo, self).__init__()
        self.linear1 = nn.Linear(28*28, 128) # -> Camada de entrada, 784 neurônios que se ligam a 128
        self.linear2 = nn.Linear(128, 64) # -> Camada interna 1, 128 neurônios que se ligam a 64
        self.linear3 = nn.Linear(64, 10) # -> Cama interna 2, 64 neurônios que se ligam a 10
        
        # PARA A CAMADA DE SAIDA NÃO É NECESSÁRIO DEFINIR NADA, POIS SÓ PRECISAMOS PEGAR O OUTPUT DE CAMADA INTERNA 2 
        
    def forward(self, X):
        X = F.relu(self.linear1(X)) # -> Função de ativação da camada de entrada para a camada interna 1 
        X = F.relu(self.linear2(X)) # -> Função de ativação da camada interna 1 para a camada interna 2
        X = self.linear3(X) # -> Função de ativação da camada interna 2 para a camada de saída, nesse caso f(X) = x 
        return F.log_softmax(X, dim=1) # -> Dados utilizados para calcular a perda

def treino(modelo, trainloader, device):
    
    otimizador = optim.SGD(modelo.parameters(), lr=0.01, momentum=0.5) # -> Define a politica de atualização dos pesos e da bias
    inicio = time() # -> timer para sabermos quanto tempo levou o treino
    
    criterio = nn.NLLLoss() # -> definindo o critério para calcular a perda
    EPOCHS = 10 # -> número de epochs que o algoritmo rodará
    modelo.train() # -> Ativando o modo de treinamento do modelo
    
    for epoch in range(EPOCHS):
        
        perda_calculada = 0 # -> inicialização da perda acumulada de epoch em questão
        
        for imagens, etiquetas in trainloader:
            
            imagens = imagens.view(imagens.shape[0], -1) # -> Convertendo as  imagens para "vetores" de 28*28 casas para ficarem compatíveis com a 
            otimizador.zero_grad() # -> Zerando os gradientes por conta do ciclo anterior
            
            output = modelo(imagens.to(device)) # -> Colocando os dados no modelo 
            perda_instatanea = criterio(output, etiquetas.to(device)) # -> Calculando a perda da epoch em questão
            
            perda_instatanea.backward() # -> back propagation a partir da perda
            
            otimizador.step() # -> Atualizando os pesos e as bias 
            
            perda_calculada += perda_instatanea.item() # -> Atualização da perda acumulada
        
        else:
            print(f"Epoch {(epoch + 1)} - Perda Resultante: {(perda_calculada / len(trainloader))}")

    print("\nTempo de treino (em minutos) = ", (time() - (inicio /60)))
 
def validacao(modelo, valloader, device):
    contas_corretas, conta_todas = 0, 0
    for imagens, etiquetas in valloader:
        for i in range(len(etiquetas)):
            img = imagens[i].view(1, 784)
            # DESATIVAR O AUTOGRAD PARA ACELERAR A VALIDAÇÃO. GRAFOS COMPUTACIONAIS DINÂMICOS TEM UM CUSTO ALTO DE PROCESSAMENTO
            with torch.no_grad():
                logps = modelo(img.to(device)) # -> Output do modelo em escala logaritmica
                
            ps = torch.exp(logps) # -> Converte output para escala normal (lembrando que é um tensor)
            probab = list(ps.cpu().numpy()[0])
            etiqueta_pred = probab.index(max(probab)) # -> Converte o tensor em um número, no caso, o número que o modelo previu como correto
            etiqueta_certa = etiquetas.numpy()[i]
            if (etiqueta_certa == etiqueta_pred): # -> Compara a previsão com o valor correto
                contas_corretas += 1
            conta_todas += 1
    print(f"Total de imagens testadas = {conta_todas}")
    print(f"\nPrecisão do modelo = {(contas_corretas * 100 / conta_todas)}%")
     

modelo = Modelo() # -> Inicializa o modelo

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Modelo rodará na GPU se possível
print(modelo.to(device))

treino(modelo, trainloader, device)
validacao(modelo, valloader, device)

dataiter = iter(trainloader)

for imagens, etiquetas in dataiter:
    plt.imshow(imagens[0].numpy().squeeze(), cmap='gray_r')
    plt.show()
    print(imagens[0].shape) # -> Para verificar as dimensões do tensor de cada imagem
    print(etiquetas[0].shape)# -> Para verificar as dimensões do tensor de cada etiqueta
    break