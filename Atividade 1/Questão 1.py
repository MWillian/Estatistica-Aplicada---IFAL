import pandas as pd

# O Pandas será a biblioteca utilizada para fazer leitura do arquivo de extensão .csv. 

#Qual das espécies tem a maior média de comprimento de pétala ?

iris = pd.read_csv('Atividade 1/Iris.csv')

# Filtro das espécies, atribuindo à variável as colunas numéricas do data frame
irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisVersicolor = iris[iris['Species'] == 'Iris-versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']


# Atribuição dos dados da pétala de cada espécie
comprimentoPetalaSetosa = irisSetosa['PetalLengthCm']
comprimentoPetalaVersicolor = irisVersicolor['PetalLengthCm']
comprimentoPetalaVirginica = irisVirginica['PetalLengthCm']


# Exibição dos valores de média arredondados
print(f"Média do comprimento de pétala da espécie Iris Setosa: {round(comprimentoPetalaSetosa.mean(),2)} cm\n") 
print(f"Média do comprimento de pétala da espécie Iris Versicolor: {round(comprimentoPetalaVersicolor.mean(),2)} cm\n")
print(f"Média do comprimento de pétala da espécie Iris Virginica: {round(comprimentoPetalaVirginica.mean(),2)} cm\n")

# Como resultado, temos a pétala da espécie Iris Virginica com o maior de média: 5.55 cm.
# Também é importar notar a diferença entre as médias das pétalas, onde a maior delas com valor 5.55 (Iris Virginica) é 3.80 vezes maior do que a menor delas (Iris Setosa).