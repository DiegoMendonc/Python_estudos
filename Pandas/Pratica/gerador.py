import pandas as pd
from datetime import datetime, timedelta
import random

# Definir SKUs e datas
skus = ['SKU1', 'SKU2', 'SKU3', 'SKU4']
start_date = datetime.now() - timedelta(days=90)  # Data de início: 3 meses atrás
end_date = datetime.now()  # Data de término: hoje

# Gerar dados fictícios
data = []
for sku in skus:
    for _ in range(30):  # 30 registros por SKU
        date = start_date + (end_date - start_date) * random.random()
        quantidade = random.randint(1, 100)
        data.append([sku, quantidade, date.strftime('%Y-%m-%d')])

# Criar DataFrame
df = pd.DataFrame(data, columns=['SKU', 'Quantidade Vendida', 'Data Vendida'])

# Salvar em um arquivo Excel
df.to_excel('vendas_ficticias.xlsx', index=False)

print("Arquivo Excel 'vendas_ficticias.xlsx' gerado com sucesso!")
