import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import scipy.stats as stts

#PLOTANDO GRÁFICOS TEMPORAIS(Time series)
#analisa a variabilidade de uma grandeza de acordo com o tempo

#atribuindo o arquivo csv para a variável 'stock' 
# stock = pd.read_csv('stock_data.csv')


# alterando o formato de apresentação do eixo x para DATE_TIME internacional no modelo ano/mês/dia
# stock['Date'] = pd.to_datetime(stock['Date'])
# print(stock.head())

# plotando os dois gráficos sobrepostos para avaliar a variabilidade das duas medidas
# sns.lineplot(data=stock,x='Date',y='High')
# sns.lineplot(data=stock,x='Date',y='Low')

#Gráficos de Dispersão
#representa a relação entre duas variáveis

iris = pd.read_csv('Iris.csv')

x_SepalLength = iris['SepalLengthCm']
y_SepalWidth = iris['SepalWidthCm']


# teste não paramétrico que vale para todos tipos de distribuição
# stts.spearmanr(x,y) #coeficiente de correlação


# teste paramétrico que vale somente para os distribuição normal
# stts.pearsonr(x,y) #coeficiente de correlação


# plotagem
# sns.scatterplot(data=iris,x = iris['SepalLengthCm'],y = iris['SepalWidthCm'])

#na plotagem, temos uma correlação forte positiva quando o coeficiente de correlação
#for próximo de 1. E forte negativa quando for próximo de -1

#para o fraco positivo, temos 0,5 de coeficiente, e -0,5 para o fraco negativo
#para a neutra, tems o coeficiente próximo de 0.

#Plotando o gráfico boxplot das 2 colunas
# sns.boxplot([x,y])
# plt.show()


#Filtragem do nome de espécie 

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisSetosa = irisSetosa.drop(columns=['Id','Species'])

irisVersicolor = iris[iris['Species'] == 'Iris-Versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']

#Definindo variáveis para espécie Setosa

setosaSepalLength = irisSetosa['SepalLengthCm']
setosaSepalWidth = irisSetosa['SepalWidthCm']
setosaPetalLength = irisSetosa['PetalLengthCm']
setosaPetalWidth = irisSetosa['PetalWidthCm']

#Definindo variáveis para espécie Versicolor

versicolorSepalLength = irisVersicolor['SepalLengthCm']
versicolorSepalWidth = irisVersicolor['SepalWidthCm']
versicolorPetalLength = irisVersicolor['PetalLengthCm']
versicolorPetalWidth = irisVersicolor['PetalWidthCm']

#Definindo variáveis para espécie Versicolor

virginicaSepalLength = irisVirginica['SepalLengthCm']
virginicaSepalWidth = irisVirginica['SepalWidthCm']
virginicaPetalLength = irisVirginica['PetalLengthCm']
virginicaPetalWidth = irisVirginica['PetalWidthCm']

#plot do gráfico para iris da espécie setosa
sns.scatterplot(data=irisSetosa,x=setosaSepalLength,y=setosaSepalWidth)
sns.scatterplot(data=irisSetosa,x=setosaSepalLength,y=setosaPetalWidth)
sns.scatterplot(data=irisSetosa,x=setosaPetalLength,y=setosaPetalWidth)
sns.scatterplot(data=irisSetosa,x=setosaPetalLength,y=setosaSepalWidth)

#matriz de correlação para a espécie Setosa

corrmatrixSetosa = irisSetosa.corr()
print(corrmatrixSetosa)

sns.heatmap(corrmatrixSetosa,annot=True)
plt.show()

#plot do gráfico para iris da espécie versicolor

sns.scatterplot(data=irisVersicolor,x=versicolorSepalLength,y=versicolorSepalWidth)
sns.scatterplot(data=irisVersicolor,x=versicolorSepalLength,y=versicolorPetalLength)
sns.scatterplot(data=irisVersicolor,x=versicolorPetalLength,y=versicolorPetalWidth)
sns.scatterplot(data=irisVersicolor,x=versicolorPetalLength,y=versicolorSepalWidth)

#matrix de correlação para a espéie Versicolor
corrmatrixVersicolor = irisVersicolor.corr()
print(corrmatrixVersicolor)

sns.heatmap(corrmatrixVersicolor)

# sns.scatterplot(data=irisSetosa,x=setosa,y=setosaPetalWidth)
# stts.pearsonr()