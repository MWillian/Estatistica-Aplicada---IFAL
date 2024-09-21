import pandas as pd
import seaborn as sns
import scipy

#Qual das espéccies tem a maior média de comprimento de pétala ?

iris = pd.read_csv('Atividade estatística\Iris.csv')

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisVersicolor = iris[iris['Species'] == 'Iris-versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']

comprimentoPetalaSetosa = irisSetosa['PetalLengthCm']
comprimentoPetalaVersicolor = irisVersicolor['PetalLengthCm']
comprimentoPetalaVirginica = irisVirginica['PetalLengthCm']

print(f"Média do comprimento de pétala da espécie Iris Setosa: {round(comprimentoPetalaSetosa.mean(),2)} cm\n")
print(f"Média do comprimento de pétala da espécie Iris Versicolor: {round(comprimentoPetalaVersicolor.mean(),2)} cm\n")
print(f"Média do comprimento de pétala da espécie Iris Virginica: {round(comprimentoPetalaVirginica.mean(),2)} cm\n")
