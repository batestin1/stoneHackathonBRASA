
import pandas as pd
import numpy as np
import seaborn as sns
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
import joblib


data_movimento = pd.read_parquet(r'C:\Users\Bates\Documents\Repositorios\sistema_recomendacao\dataset\hackathon_stone_brasa_banking_data.parquet')
data_vendas = pd.read_parquet(r'C:\Users\Bates\Documents\Repositorios\sistema_recomendacao\dataset\hackathon_stone_brasa_sales_data.parquet')
mcc = pd.read_parquet(r'C:\Users\Bates\Documents\Repositorios\sistema_recomendacao\dataset\mcc.parquet')

data_vendas = data_vendas[['date_time', 'value',	'type',	'mcc', 'state']]
df = pd.merge(data_vendas, mcc, on='mcc', how='left')
df['description'] = df['edited_description']
df = df[['date_time', 'value', 'type', 'state', 'description']]

df.to_csv(r'C:\Users\Bates\Documents\Repositorios\sistema_recomendacao\dataset\dados_consolidados.csv')

encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df[['description', 'state']])
model = NearestNeighbors(n_neighbors=10, algorithm='auto').fit(encoded_features)

def recomendar_estabelecimento(df, estabelecimento_atual, estado_atual):
    # Verificar se o estabelecimento existe no DataFrame
    if not df[(df['description'] == estabelecimento_atual) & (df['state'] == estado_atual)].empty:
        # Localize o índice do estabelecimento atual
        index = df[(df['description'] == estabelecimento_atual) & (df['state'] == estado_atual)].index[0]

        # Obtenha a linha codificada correspondente e ajuste a dimensão
        encoded_row = encoded_features[index].toarray().reshape(1, -1)

        # Encontre os estabelecimentos mais semelhantes
        distances, indices = model.kneighbors(encoded_row, n_neighbors=10)

        # Filtrar a recomendação para evitar repetição do mesmo estabelecimento
        recomendacoes = df.iloc[indices[0]][['state', 'description']].values

        # Se todas as recomendações forem o mesmo estabelecimento, realiza novo filtro
        if all(rec[1] == estabelecimento_atual for rec in recomendacoes):
            recomendacoes = df[['state', 'description']].drop_duplicates().values

        return recomendacoes if len(recomendacoes) > 0 else None
    else:
        return None



def salvar_modelo(modelo, encoder, nome_arquivo_modelo='modelo_recomendacao.pkl', nome_arquivo_encoder='encoder_recomendacao.pkl'):
    """
    Salva o modelo de recomendação e o encoder em arquivos.

    :param modelo: O modelo de recomendação treinado (e.g., NearestNeighbors)
    :param encoder: O encoder utilizado para codificação das características (e.g., OneHotEncoder)
    :param nome_arquivo_modelo: Nome do arquivo para salvar o modelo
    :param nome_arquivo_encoder: Nome do arquivo para salvar o encoder
    """
    # Salvar o modelo
    joblib.dump(modelo, nome_arquivo_modelo)
    print(f"Modelo salvo em {nome_arquivo_modelo}")

    # Salvar o encoder
    joblib.dump(encoder, nome_arquivo_encoder)
    print(f"Encoder salvo em {nome_arquivo_encoder}")



salvar_modelo(model, encoder)

