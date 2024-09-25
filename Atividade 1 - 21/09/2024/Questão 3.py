import pandas as pd
import scipy
import scipy.stats as stts
import seaborn as sns
import matplotlib.pyplot as plt


# Qual a distribuição das espécies do banco de dados ?

# Podemos checar a normalidade dos conjuntos dados por meio do teste de Shapiro-Wilk, e com uma análise visual utilizando o histograma.

iris = pd.read_csv('Iris.csv')

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisVersicolor = iris[iris['Species'] == 'Iris-versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']


# Atribuindo as variáveis de cada espécie

irisSetosaPetalLength = irisSetosa['PetalLengthCm']
irisSetosaSepalLength = irisSetosa['SepalLengthCm']
irisSetosaPetalWidth = irisSetosa['PetalWidthCm']
irisSetosaSepalWidth = irisSetosa['SepalWidthCm']


irisVersicolorPetalLength = irisVersicolor['PetalLengthCm']
irisVersicolorSepalLength = irisVersicolor['SepalLengthCm']
irisVersicolorPetalWidth = irisVersicolor['PetalWidthCm']
irisVersicolorSepalWidth = irisVersicolor['SepalWidthCm']


irisVirginicaPetalLength = irisVirginica['PetalLengthCm']
irisVirginicaSepalLength = irisVirginica['SepalLengthCm']
irisVirginicaPetalWidth = irisVirginica['PetalWidthCm']
irisVirginicaSepalWidth = irisVirginica['SepalWidthCm']


# Análise da normalidade de cada conjunto de dados por meio do teste de shapiro

pvalueList = []
stat, p = scipy.stats.shapiro(irisSetosaPetalLength)
print(f"p-valor: {round(p,3)}")

pvalueList.append()
print(pvalueList)
# stat, p = scipy.stats.shapiro(irisSetosaPetalLength)