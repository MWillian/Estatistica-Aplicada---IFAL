import pandas as pd
import scipy.stats as stts
import seaborn as sns
import scipy
import matplotlib.pyplot as plt

# Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala ?


iris = pd.read_csv('Atividade 1 - 21/09/2024/Iris.csv')

# Filtro das colunas das espécies

irisSetosa = iris[iris['Species'] == 'Iris-setosa']
irisVersicolor = iris[iris['Species'] == 'Iris-versicolor']
irisVirginica = iris[iris['Species'] == 'Iris-virginica']


#Declaração e atribuição das variáveis do comprimento da sépala e pétala de cada espécie

setosaPetalLength = irisSetosa['PetalLengthCm']
versicolorPetalLength = irisVersicolor['PetalLengthCm']
virginicaPetalLength = irisVirginica['PetalLengthCm']

setosaSepalLength = irisSetosa['SepalLengthCm']
versicolorSepalLength = irisVersicolor['SepalLengthCm']
virginicaSepalLength = irisVirginica['SepalLengthCm']


# Checando a normalidade de cada conjunto de dados de cada espécie para decidir entre qual o melhor teste de coeficiente de correlação utilizar (Spearman ou Pearson)

print("P-valor para a espécie Iris-Setosa: ")
stat, p = scipy.stats.shapiro(setosaPetalLength)
print(f"Comprimento da pétala = {p}")
stat, p = scipy.stats.shapiro(setosaSepalLength)
print(f"Comprimento da Sépala = {p}\n") 

print("P-valor para a espécie Iris-Versicolor: ")
stat, p = scipy.stats.shapiro(versicolorPetalLength)
print(f"Comprimento da pétala = {p}")
stat, p = scipy.stats.shapiro(versicolorSepalLength)
print(f"Comprimento da sépala = {p}\n")

print("P-valor para a espécie Iris-Virginica: ")
stat, p = scipy.stats.shapiro(virginicaPetalLength)
print(f"Comprimento da pétala = {p}")
stat, p = scipy.stats.shapiro(virginicaSepalLength)
print(f"Comprimento da Sépala = {p}\n")

# Como todos os conjuntos apresentam p>0.05, não podemos rejeitar a hipótese nula, então consideramos os conjuntos com distribuição normal.
# Logo, para que possamos verificar o coeficiente de correlação entre esses conjuntos, utilizaremos o teste paramétrico de Pearson.

corr,p = stts.pearsonr(setosaPetalLength,setosaSepalLength)
print(f"Coeficiente de correlação para Iris-Setosa: {corr}")

corr,p = stts.pearsonr(versicolorPetalLength,versicolorSepalLength)
print(f"Coeficiente de correlação para Iris-Versicolor: {corr}")

corr,p = stts.pearsonr(virginicaPetalLength,virginicaSepalLength)
print(f"Coeficiente de correlação para Iris-Virginica: {corr}")


# Para confirmar a correlação

# Gráfico de correlação para a espécie Setosa

# sns.scatterplot(data=irisSetosa,x = irisSetosa['SepalLengthCm'],y = irisSetosa['PetalLengthCm'])
# plt.show()
# #gráfico de correlação para a espécie Versicolor
# sns.scatterplot(data=irisVersicolor,x = irisVersicolor['SepalLengthCm'],y = irisVersicolor['PetalLengthCm'])
# plt.show()
# #gráfico de correlação para a espécie Virginica
# sns.scatterplot(data=irisVirginica,x = irisVirginica['SepalLengthCm'],y = irisVirginica['PetalLengthCm'])
# plt.show()


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
