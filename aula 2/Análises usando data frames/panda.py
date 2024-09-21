import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#A biblioteca Pandas é amplamente utilizada em Python para análise e manipulação de dados.

sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6])
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2])


#Exibindo colunas de um dataframe (arquivos csv)

# Atribuindo os dados do arquivo csv para uma variável
iris = pd.read_csv('Iris.csv')

#plotando as primeiras 5 linhas do arquivo 'iris'
print(iris.head())

#plotando a coluna 'Open'
stock = pd.read_csv('stock_data.csv')
sns.boxplot(stock['Open'])
plt.show()

#atribuindo um alias para a coluna open
# open = stock['Open']

# x = open.mean()

#definindo o ponto de corte segundo os teoremas
#ponto de corte é o desvio padrão dos dados vezes 3

# ponto_corte = open.std(ddof=1) * 3

# inf = x - ponto_corte
# sup = x + ponto_corte
# outliers = open[(open < inf)|(open > sup)]
# print(outliers)

#------------------------------------------

#rodando utilizando a lista sincrona e assíncrona já definida

# x = asyncr.mean()

# ponto_corte = asyncr.std(ddof=1)*3

# inf = x - ponto_corte
# sup = x + ponto_corte
# outliers = asyncr[(asyncr < inf)|(asyncr > sup)]
# print(outliers)
