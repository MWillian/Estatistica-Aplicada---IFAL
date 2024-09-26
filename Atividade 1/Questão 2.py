import pandas as pd
import scipy
import scipy.stats as stts
import seaborn as sns
import matplotlib.pyplot as plt

# Há uma correlação significativa entre o comprimento da sépala e o comprimento da pétala ?


iris = pd.read_csv('Atividade 1/Iris.csv')

# Filtro das colunas das espéciespip sh

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

corr,p = stts.pearsonr(setosaSepalLength,setosaPetalLength)
print(f"Coeficiente de correlação para Iris-Setosa: {corr}")

corr,p = stts.pearsonr(versicolorSepalLength,versicolorPetalLength)
print(f"Coeficiente de correlação para Iris-Versicolor: {corr}")

corr,p = stts.pearsonr(virginicaSepalLength,virginicaPetalLength)
print(f"Coeficiente de correlação para Iris-Virginica: {corr}\n")


# Para confirmar a correlação, fazemos o plot do gráfico Scatterplot

# Gráfico de correlação para a espécie Setosa

sns.scatterplot(data=irisSetosa,x = irisSetosa['SepalLengthCm'],y = irisSetosa['PetalLengthCm'])
# indica uma correlação fraca positiva (0.26)
plt.show() 

# Gráfico de correlação para a espécie Versicolor
sns.scatterplot(data=irisVersicolor,x = irisVersicolor['SepalLengthCm'],y = irisVersicolor['PetalLengthCm'])
# indica uma correlação forte positiva (0.75)
plt.show()

# Gráfico de correlação para a espécie Virginica
sns.scatterplot(data=irisVirginica,x = irisVirginica['SepalLengthCm'],y = irisVirginica['PetalLengthCm'])
# indica uma correlação forte positiva (0.86)
plt.show()

# Também podemos utilizar a ferramenta HeatMap para uma melhor visualização dos índices de correlação das espécies.

# Drop para deixar somente as colunas para análise da correlação

irisSetosa = irisSetosa.drop(columns=['Id','Species','SepalWidthCm','PetalWidthCm'])

irisVersicolor = irisVersicolor.drop(columns=['Id','Species','SepalWidthCm','PetalWidthCm'])

irisVirginica = irisVirginica.drop(columns=['Id','Species','SepalWidthCm','PetalWidthCm'])

# Atribuição das variáveis para a matrix da correlação
corrSetosa = irisSetosa.corr()
corrVersicolor = irisVersicolor.corr()
corrVirginica = irisVirginica.corr()

sns.heatmap(corrSetosa,annot=True)
plt.show()
sns.heatmap(corrVersicolor,annot=True)
plt.show()
sns.heatmap(corrVirginica,annot=True)
plt.show()

# Após a realização das análises, podemos constatar que a correlação entre o comprimento da pétala e o comprimento da sépala da espécie Iris-Setosa é fraca, quase neutra.
# Já para as espécies Iris-Versicolo e Iris-Virginica, temos uma correlação forte, que indica a linearidade entre as duas grandezas, quando aumentamos os valores de um eixo (comprimento da pétala), o outro também tende a aumentar (comprimento da sépala)