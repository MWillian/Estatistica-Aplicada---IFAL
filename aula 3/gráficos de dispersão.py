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
stock['Date'] = pd.to_datetime(stock['Date'])


# Plotando os dois gráficos sobrepostos para avaliar a variabilidade das duas medidas
sns.lineplot(data=stock,x='Date',y='High')
sns.lineplot(data=stock,x='Date',y='Low')



#GRÁFICOS DE DISPERSÃO

#Representam a dispersão entre duas grandezas definidas

# Atribuindo os dados do arquivo csv para a variável 'iris' 
iris = pd.read_csv('aula 3\Iris.csv')

# Atribuição dos dados das colunas "Comprimento da sépala" e "Largura da sépala" para variáveis.
x_SepalLength = iris['SepalLengthCm']
y_SepalWidth = iris['SepalWidthCm']



# Teste não paramétrico de Spearman, pode ser utilizado para todos tipos de distribuição.

# Esse teste não exige a suposição de que a relação entre as variáveis é linear, nem composta de dados quantitativos.
# Pode ser utilizado para verificar relação entre variáveis medidas no nível ordinal.

print(stts.spearmanr(x_SepalLength,y_SepalWidth)) #coeficiente de correlação


# Teste paramétrico de Pearson,deve ser utilizado somente para os conjuntos de distribuição normal.

# É possível verificar o valor-p e o coeficiente de correlação de Pearson.
# Esse coeficiente exprime o grau de correlação entre -1 e 1.
# Quando o coeficiente se aproxima de 1, nota-se uma relação linear positiva entre as variáveis (quando uma aumenta, a outra também aumentará)
# Quando o coeficiente se aproxima de -1, também é possível dizer que as variáveis são correlacionadas, mas nesse caso quando o valor de uma variável aumenta o da outra diminui. 
# Um coeficiente próximo de 0 indica que não há relação entre as duas variáveis.

print(stts.pearsonr(x_SepalLength,y_SepalWidth)) #coeficiente de correlação



# Plotagem do gráfico Scatterplot, para análisar a correlação entre duas variáveis e sua dispersão
sns.scatterplot(data=iris,x = iris['SepalLengthCm'],y = iris['SepalWidthCm']) # Aqui é analisado o comprimeito da sépala e largura da sépala em todas as espécies de plantas.


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