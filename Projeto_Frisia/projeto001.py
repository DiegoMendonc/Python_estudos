Importação do banco de dados e usabilidade do PANDAS:

 

from sqlalchemy import create_engine

import pandas as pd

 

# Configuração da conexão (exemplo para MySQL)

engine = create_engine('mysql+pymysql://usuario:senha@host:porta/nome_do_banco')

 

# Carregar dados de uma tabela específica

df = pd.read_sql('SELECT * FROM sua_tabela', con=engine)

 

 

Processamento de dados:


ESTUDAR

 

 

Calcular similaridade:

 

from sklearn.metrics.pairwise import cosine_similarity

 

# Supondo que 'features' seja uma matriz de características extraídas dos dados

similarity_matrix = cosine_similarity(df)

 

 

 

 

Exemplo para automatizar em funções o processo de conexão, carregamento e pré-processamento juntamente com o cálculo:

 

def load_data_from_db(connection_string, query):

    engine = create_engine(connection_string)

    return pd.read_sql(query, con=engine).dropna()

 

def calculate_similarity(data):

    return cosine_similarity(data)

 

def main():

    connection_string = 'mysql+pymysql://usuario:senha@host:porta/nome_do_banco'

    query = 'SELECT * FROM sua_tabela'

    data = load_data_from_db(connection_string, query)

    similarity = calculate_similarity(data)

    print(similarity)

 

if __name__ == "__main__":

    main()

 

 

 

Para cálculo de similaridade com NLP:

 

Para calcular a similaridade em porcentagem com base na descrição do produto, você pode usar técnicas de processamento de linguagem natural (NLP) para transformar as descrições em vetores e, em seguida, calcular a similaridade entre esses vetores. Aqui está um exemplo de como fazer isso utilizando TF-IDF e cosine similarity:

 

Instalar as bibliotecas necessárias:
pandas para manipulação de dados.
scikit-learn para algoritmos de machine learning e NLP.
 

Carregar os dados do banco de dados:
Utilize SQLAlchemy para conectar ao banco de dados e pandas para carregar os dados.
 

from sqlalchemy import create_engine

import pandas as pd

 

# Configuração da conexão (exemplo para MySQL)

engine = create_engine('mysql+pymysql://usuario:senha@host:porta/nome_do_banco')

 

# Carregar dados de uma tabela específica

df = pd.read_sql('SELECT * FROM sua_tabela', con=engine)

 

Pré-processamento das descrições:
Limpe e prepare as descrições dos produtos
 

df['descricao'] = df['descricao'].fillna('')  # Substituir valores nulos por strings vazias

Transformar descrições em vetores:
Utilize TfidfVectorizer para transformar as descrições em vetores TF-IDF.
 

from sklearn.feature_extraction.text import TfidfVectorizer

 

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(df['descricao'])

 

5. Calcular a similaridade:

Utilize cosine similarity para calcular a similaridade entre as descrições.
 

from sklearn.metrics.pairwise import cosine_similarity

 

similarity_matrix = cosine_similarity(tfidf_matrix)

 

6. Converter a similaridade para porcentagem:

Multiplique os valores de similaridade por 100 para obter a porcentagem.
similarity_percentage = similarity_matrix * 100

 

 

Automatizar o processo:

Crie funções para automatizar o processo de conexão, carregamento, pré-processamento, transformação e cálculo de similaridade.
 

def load_data_from_db(connection_string, query):

    engine = create_engine(connection_string)

    return pd.read_sql(query, con=engine).fillna('')

 

def calculate_similarity_percentage(data, column):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(data[column])

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix * 100

 

def main():

    connection_string = 'mysql+pymysql://usuario:senha@host:porta/nome_do_banco'

    query = 'SELECT * FROM sua_tabela'

    data = load_data_from_db(connection_string, query)

    similarity_percentage = calculate_similarity_percentage(data, 'descricao')

    print(similarity_percentage)

 

if __name__ == "__main__":

    main()

 

 

Para salvar os resultados basta seguir:

 

similarity_df = pd.DataFrame(similarity_percentage)

similarity_df.to_sql('similarity_results', con=engine, if_exists='replace', index=False)

 