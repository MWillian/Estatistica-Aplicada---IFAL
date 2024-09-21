import pandas as pd
import seaborn as sns
import scipy
import matplotlib.pyplot as plt

iris = pd.read_csv('Iris.csv')

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisVersicolor = iris[iris['Species'] == 'Iris-versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']

setosaSepalWidth = irisSetosa['SepalWidthCm']
versicolorSepalWidth = irisVersicolor['SepalWidthCm']
virginicaSepalWidth = irisVirginica['SepalWidthCm']

setosaPetalLength = irisSetosa['PetalLengthCm']
versicolorPetalLength = irisVersicolor['PetalLengthCm']
virginicaPetalLength = irisVirginica['PetalLengthCm']

setosaSepalLength = irisSetosa['SepalLengthCm']
setosaPetalLength = irisSetosa['PetalLengthCm']


#plot da correlação

#gráfico de correlação para a espécie Setosa
sns.scatterplot(data=irisSetosa,x = irisSetosa['SepalLengthCm'],y = irisSetosa['PetalLengthCm'])
plt.show()
#gráfico de correlação para a espécie Versicolor
sns.scatterplot(data=irisVersicolor,x = irisVersicolor['SepalLengthCm'],y = irisVersicolor['PetalLengthCm'])
plt.show()
#gráfico de correlação para a espécie Virginica
sns.scatterplot(data=irisVirginica,x = irisVirginica['SepalLengthCm'],y = irisVirginica['PetalLengthCm'])
plt.show()


#drop para deixar somente as colunas para análise da correlação

# irisSetosa = irisSetosa.drop(columns=['Id','Species','SepalWidthCm','PetalWidthCm'])

# irisVersicolor = irisVersicolor.drop(columns=['Id','Species','SepalWidthCm','PetalWidthCm'])

# irisVirginica = irisVirginica.drop(columns=['Id','Species','SepalWidthCm','PetalWidthCm'])

# #atribuição das variáveis para a matrix da correlação
# corrSetosa = irisSetosa.corr()
# corrVersicolor = irisVersicolor.corr()
# corrVirginica = irisVirginica.corr()

# sns.heatmap(corrSetosa,annot=True)
# plt.show()
# sns.heatmap(corrVersicolor,annot=True)
# plt.show()
# sns.heatmap(corrVirginica,annot=True)
# plt.show()
