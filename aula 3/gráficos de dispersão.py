import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import scipy.stats as stts

# GRÁFICOS TEMPORAIS

# Os gráficos temporais analisam a variabilidade de uma grandeza de acordo com o tempo

# Atribuindo os dados do arquivo csv para a variável 'stock' 
stock = pd.read_csv('aula 3\stock_data.csv')


# Alterando o formato de apresentação do eixo x para DATE_TIME internacional no modelo ano/mês/dia (esse passo é importante para melhor visualização dos dados do conjunto de dados)
# stock['Date'] = pd.to_datetime(stock['Date'])
# print(stock.head())

# # Plotando os dois gráficos sobrepostos para avaliar a variabilidade das duas medidas
# sns.lineplot(data=stock,x='Date',y='High')
# sns.lineplot(data=stock,x='Date',y='Low')
# plt.show()


#GRÁFICOS DE DISPERSÃO

# #Representam a dispersão entre duas grandezas definidas

# Atribuindo os dados do arquivo csv para a variável 'iris' 
iris = pd.read_csv('aula 3\Iris.csv')

# Atribuição dos dados das colunas "Comprimento da sépala" e "Largura da sépala" para variáveis.
x_SepalLength = iris['SepalLengthCm']
y_SepalWidth = iris['SepalWidthCm']



# Teste não paramétrico de Spearman, pode ser utilizado para todos tipos de distribuição.

# Esse teste não exige a suposição de que a relação entre as variáveis é linear, nem composta de dados quantitativos.
# Pode ser utilizado para verificar relação entre variáveis medidas no nível ordinal.

# print(stts.spearmanr(x_SepalLength,y_SepalWidth)) #coeficiente de correlação


# Teste paramétrico de Pearson, deve ser utilizado somente para os conjuntos de distribuição normal.

# É possível verificar o valor-p e o coeficiente de correlação de Pearson.
# Esse coeficiente exprime o grau de correlação entre -1 e 1.
# Quando o coeficiente se aproxima de 1, nota-se uma relação linear positiva entre as variáveis (quando uma aumenta, a outra também aumentará)
# Quando o coeficiente se aproxima de -1, também é possível dizer que as variáveis são correlacionadas, mas nesse caso quando o valor de uma variável aumenta o da outra diminui. 
# Um coeficiente próximo de 0 indica que não há relação entre as duas variáveis.

print(stts.pearsonr(x_SepalLength,y_SepalWidth)) #coeficiente de correlação



# Plotagem do gráfico Scatterplot, para análisar a correlação entre duas variáveis e sua dispersão
# sns.scatterplot(data=iris,x = iris['SepalLengthCm'],y = iris['SepalWidthCm']) # Aqui é analisado o comprimeito da sépala e largura da sépala em todas as espécies de plantas.
# plt.show()


# Na plotagem, temos uma correlação forte positiva quando o coeficiente de correlação for próximo de 1, e forte negativa quando for próximo de -1.
# Também há as correlações fracas positivas, quando o coeficiente está mais próximo de 0 do que de 1, e fraca negativa quando o coeficiente está mais próximo de 0 do que de -1.
# Para um coeficiente neutro temos um valor próximo de 0.


# Plotando o gráfico boxplot das 2 colunas
# Em resumo, o gráfico boxplot é muito utilizado para verificar a dispersão do conjunto de dados, a presença de outliers e a localização dos quartis na distribuição.
# sns.boxplot([x_SepalLength,y_SepalWidth])
# plt.show()


#Filtragem do nome de espécie 

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisSetosa = irisSetosa.drop(columns=['Id','Species'])# aqui é retirado do data frame da espécie Iris Setosa as colunas que possuem dados não numéricos para fazer a matrix de correlação.

irisVersicolor = iris[iris['Species'] == 'Iris-Versicolor']
irisVersicolor = irisVersicolor.drop(columns=['Id','Species'])

irisVirginica = iris[iris['Species'] == 'Iris-virginica']
irisVirginica = irisVirginica.drop(columns=['Id','Species'])


#Definindo variáveis para espécie Setosa

setosaSepalLength = irisSetosa['SepalLengthCm']
setosaSepalWidth = irisSetosa['SepalWidthCm']
setosaPetalLength = irisSetosa['PetalLengthCm']
setosaPetalWidth = irisSetosa['PetalWidthCm']

# Definindo variáveis para espécie Versicolor

versicolorSepalLength = irisVersicolor['SepalLengthCm']
versicolorSepalWidth = irisVersicolor['SepalWidthCm']
versicolorPetalLength = irisVersicolor['PetalLengthCm']
versicolorPetalWidth = irisVersicolor['PetalWidthCm']

# Definindo variáveis para espécie Versicolor

virginicaSepalLength = irisVirginica['SepalLengthCm']
virginicaSepalWidth = irisVirginica['SepalWidthCm']
virginicaPetalLength = irisVirginica['PetalLengthCm']
virginicaPetalWidth = irisVirginica['PetalWidthCm']

# Plot do gráfico scatterplot para a espécie Iris Setosa

sns.scatterplot(data=irisSetosa,x=setosaSepalLength,y=setosaSepalWidth)
sns.scatterplot(data=irisVersicolor,x=versicolorSepalLength,y=versicolorSepalWidth)
sns.scatterplot(data=irisVirginica,x=virginicaSepalLength,y=virginicaSepalWidth)
plt.show()


sns.scatterplot(data=irisSetosa,x=setosaSepalLength,y=setosaPetalWidth)
sns.scatterplot(data=irisSetosa,x=setosaPetalLength,y=setosaPetalWidth)
sns.scatterplot(data=irisSetosa,x=setosaPetalLength,y=setosaSepalWidth)


# Matriz de correlação para a espécie Setosa

corrmatrixSetosa = irisSetosa.corr()# essa matriz de correlação está usando como conjunto de dados todas as colunas numéricas da espécie Iris Setosa. Para uma melhor análise, também é importante verificar correlação entre cada coluna, isoladamente .
print(corrmatrixSetosa)


# Gráfico Heatmap para melhor visualização da correlação entre as variáveis. 
sns.heatmap(corrmatrixSetosa,annot=True)# O atributo 'annot=true' imprime dentro de cada unidade do gráfico um coeficiente. 
plt.show()


#plot do gráfico para iris da espécie versicolor

sns.scatterplot(data=irisVersicolor,x=versicolorSepalLength,y=versicolorSepalWidth)
sns.scatterplot(data=irisVersicolor,x=versicolorSepalLength,y=versicolorPetalLength)
sns.scatterplot(data=irisVersicolor,x=versicolorPetalLength,y=versicolorPetalWidth)
sns.scatterplot(data=irisVersicolor,x=versicolorPetalLength,y=versicolorSepalWidth)


#matrix de correlação e heatmap para a espécie Versicolor
corrmatrixVersicolor = irisVersicolor.corr()
print(corrmatrixVersicolor)

sns.heatmap(corrmatrixVersicolor)
plt.show()


#matrix de correlação e heatmap para a espécie Virginica

corrmatrixVirginica = irisVirginica.corr()
print(corrmatrixVirginica)

sns.heatmap(corrmatrixVirginica)
plt.show()