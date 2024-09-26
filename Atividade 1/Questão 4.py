import pandas as pd
import scipy
import scipy.stats as stts
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt

# Quais características têm a maior variabilidade dentro de cada espécie ?

iris = pd.read_csv('Atividade 1/Iris.csv')

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

# Cálculo da variância para a espécie Iris-Setosa

print(f"Variância do comprimento da sépala da Setosa: {irisSetosaSepalLength.var(ddof=1)}\n")
print(f"Variância da largura da sépala da Setosa: {irisSetosaSepalWidth.var(ddof=1)}\n")
print(f"Variância do comprimento da pétala da Setosa: {irisSetosaPetalLength.var(ddof=1)}\n")
print(f"Variância da largura da pétala da Setosa: {irisSetosaPetalWidth.var(ddof=1)}\n\n")

# Cálculo da variância para a espécie Iris-Versicolor

print(f"Variância do comprimento da sépala da Versicolor: {irisVersicolorSepalLength.var(ddof=1)}\n")
print(f"Variância da largura da sépala da Versicolor: {irisVersicolorSepalWidth.var(ddof=1)}\n")
print(f"Variância do comprimento da pétala da Versicolor: {irisVersicolorPetalLength.var(ddof=1)}\n")
print(f"Variância da largura da pétala da Versicolor: {irisVersicolorPetalWidth.var(ddof=1)}\n\n")

# Cálculo da variância para a espécie Iris-Virginica

print(f"Variância do comprimento da sépala da Virginica: {irisVirginicaSepalLength.var(ddof=1)}\n")
print(f"Variância da largura da sépala da Virginica: {irisVirginicaSepalWidth.var(ddof=1)}\n")
print(f"Variância do comprimento da pétala da Virginica: {irisVirginicaPetalLength.var(ddof=1)}\n")
print(f"Variância da largura da pétala da Virginica: {irisVirginicaPetalWidth.var(ddof=1)}\n\n")


# Gráfico boxplot de cada espécie

sns.boxplot(data = iris, x = 'Species', y = 'SepalLengthCm')
plt.show()
sns.boxplot(data = iris, x = 'Species', y = 'SepalWidthCm')
plt.show()
sns.boxplot(data = iris, x = 'Species', y = 'PetalLengthCm')
plt.show()
sns.boxplot(data = iris, x = 'Species', y = 'PetalWidthCm')
plt.show()