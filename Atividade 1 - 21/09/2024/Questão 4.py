import pandas as pd
import scipy
import scipy.stats as stts
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt

# Quais características têm a maior variabilidade dentro de cada espécie ?

iris = pd.read_csv('Atividade 1 - 21/09/2024/Iris.csv')

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisVersicolor = iris[iris['Species'] == 'Iris-versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']


# Atribuindo as variáveis de cada espécie

irisSetosaPetalLength = irisSetosa['PetalLengthCm']
print(irisSetosa)
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

sns.boxplot(data = iris, x = 'Species', y = 'SepalLengthCm')
plt.show()
sns.boxplot(data = iris, x = 'Species', y = 'SepalWidthCm')
plt.show()
sns.boxplot(data = iris, x = 'Species', y = 'PetalLengthCm')
plt.show()
sns.boxplot(data = iris, x = 'Species', y = 'PetalWidthCm')
plt.show()