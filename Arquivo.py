import os
from datetime import datetime, timedelta
import pandas as pd

# Intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=15)

# Formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Curitiba'
key = ''

# URL de acesso aos dados meteorológicos
URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv'

# Carregando os dados
dados = pd.read_csv(URL)
print(dados.head(7))

# Criando o diretório para salvar os arquivos
file_path = f'{data_inicio}\\'
os.mkdir(file_path)

# Salvando os dados em CSV
dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
