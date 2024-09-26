import pandas as pd
import scipy
import scipy.stats as stts
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt


# Qual a distribuição das espécies do banco de dados ?

# Podemos checar a normalidade dos conjuntos dados por meio do teste de Shapiro-Wilk, e com uma análise visual utilizando o histograma.

iris = pd.read_csv('Atividade 1 - 21/09/2024/Iris.csv')

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

print("P-valores para a espécie Iris-Setosa\n")

stat, p = scipy.stats.shapiro(irisSetosaPetalLength) # NORMAL (p-valor 0.055)
print(f"Comprimento da pétala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisSetosaSepalLength) # NORMAL (p-valor 0.46)
print(f"Comprimento da sépala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisSetosaPetalWidth) # ANORMAL (p-valor 1.85255^-06)
print(f"Largura da pétala: {p}") 

stat, p = scipy.stats.shapiro(irisSetosaSepalWidth)# NORMAL (p-valor 0.204)
print(f"Largura da sépala: {p}\n")




print("P-valores para a espécie Iris-Versicolor\n")

stat, p = scipy.stats.shapiro(irisVersicolorPetalLength) # NORMAL (p-valor 0.158)
print(f"Comprimento da pétala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisVersicolorSepalLength) # NORMAL (p-valor 0.465)
print(f"Comprimento da sépala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisVersicolorPetalWidth) # ANORMAL (p-valor 0.027)
print(f"Largura da pétala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisVersicolorSepalWidth) # NORMAL (p-valor 0.338)
print(f"Largura da sépala: {round(p,3)}\n")




print("P-valores para a espécie Iris-Virginica\n")

stat, p = scipy.stats.shapiro(irisVirginicaPetalLength) # NORMAL (p-valor 0.11)
print(f"Comprimento da pétala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisVirginicaSepalLength) # NORMAL (p-valor 0.258)
print(f"Comprimento da sépala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisVirginicaPetalWidth) # NORMAL (p-valor 0.087)
print(f"Largura da pétala: {round(p,3)}")

stat, p = scipy.stats.shapiro(irisVirginicaSepalWidth) # NORMAL (p-valor 0.181)
print(f"Largura da sépala: {round(p,3)}\n")


# Com os resultados obtidos, podemos inferir que de todos os conjuntos de dados analisados, os conjuntos que possuem um resultado condizente com a hipótese nula (valor de p < 0.05)
# são a largura da pétala da espécie Iris-Setosa (1.85255^06) e a largura da pétala da espécie Iris-Versicolor (0.027).

# Para melhor visualização das informações obtidas, podemos utilizar o gráfico histograma para cada conjunto.

# Para os conjuntos com distribuição anormal, utilizaremos o teste de assimetria, para inferir a forma do gráfico.
# Já para os conjuntos com distribuição normal, analisaremos a curtose do gráfico desse conjunto.


# Teste de assimetria 

# Assimetria da largura da pétala da Setosa

assimetricSetosaPetalWidth = scipy.stats.skew(irisSetosaPetalWidth)
print(f"Resultado do teste de assimetria para o conjunto de dados da largura da pétala da espécie Iris-Setosa: {assimetricSetosaPetalWidth}") 
# resultado do teste: 1.1610221. Valor > 0 indicando cauda a direita.

# Gráfico de histograma confirmando a cauda para a direita.

plt.hist(irisSetosaPetalWidth,6) # 0.1 e 0.6 são respectivamente os valores mínimo e máximo do conjunto.
plt.xlabel("Largura da pétala da Iris-Setosa")
plt.show()


# Assimetria da largura da pétala da Virginica

assimetricVersicolorPetalWidth = scipy.stats.skew(irisVersicolorPetalWidth)
print(f"Resultado do teste de assimetria para o conjunto de dados da largura da pétala da espécie Iris-Versicolor: {assimetricVersicolorPetalWidth}") # resultado do teste: -0.03023630. Valor < 0 indicando simetria com uma leve cauda a esquerda.

# Gráfico de histograma confirmando a cauda a esquerda. Aqui existe uma dificuldade em visualizar a cauda a esquerda devido ao valor do teste de assimetria ser muito próximo de 0, o que pode gerar confunsão entre as definições.

print(f"max {irisVersicolorPetalWidth.max()}, min {irisVersicolorPetalWidth.min()}")
plt.hist(irisVersicolorPetalWidth) # 1.8 e 1.8 são respectivamente os valores mínimo e máximo do conjunto.
plt.xlabel("Largura da pétala da Iris-Versicolor")
plt.show()


# Teste para calcular a curtose do conjunto

print("Resultados do teste de Curtose para a espécie Iris-Setosa \n")

kurtosisSetosaPetalLength = scipy.stats.kurtosis(irisSetosaPetalLength)
print(f"Curtose do comprimento da pétala: {kurtosisSetosaPetalLength} ")
# Valor de curtose 0.81

# Histograma representando o comprimento da pétala da Setosa.
plt.hist(irisSetosaPetalLength, 9,(1.0,1.9)) 
# 1.0 e 1.9 são respectivamente os valores mínimo e máximo do conjunto.
plt.xlabel("Comprimento da pétala da Setosa")
plt.show()

kurtosisSetosaSepalLength = scipy.stats.kurtosis(irisSetosaSepalLength)
print(f"Curtose do comprimento da sépala: {kurtosisSetosaSepalLength} ")
# Valor de curtose -0.34


# Histograma representando o comprimento da sépala da Setosa.
plt.hist(irisSetosaSepalLength,6, (4.3,5.8)) 
# 4.3 e 5.8 são respectivamente os valores mínimos e máximos do conjunto.
plt.xlabel("Comprimento da sépala da Setosa.")
plt.show()

kurtosisSetosaSepalWidth = scipy.stats.kurtosis(irisSetosaSepalWidth)
print(f"Curtose da largura da sépala: {kurtosisSetosaSepalWidth}\n")
# Valor de curtose 0.68

plt.hist(irisSetosaSepalWidth,5)
plt.xlabel("Largura da sépala da Setosa.")
plt.show()



print("Resultados do teste de Curtose para espécie Iris-Versicolor \n")

kurtosisVersicolorPetalLength = scipy.stats.kurtosis(irisVersicolorPetalLength)
print(f"Curtose do comprimento da pétala: {kurtosisVersicolorPetalLength} ")
# # Valor de curtose -0.074

plt.hist(irisVersicolorPetalLength,10)
plt.xlabel("Comprimento da pétala da Versicolor.")
plt.show()


kurtosisVersicolorSepalWidth = scipy.stats.kurtosis(irisVersicolorSepalWidth)
print(f"Curtose da largura da sépala: {kurtosisVersicolorSepalWidth} ")
# Valor de curtose -0.44

plt.hist(irisVersicolorPetalWidth,9)
plt.xlabel("Largura da sépala da Versicolor.")
plt.show()


kurtosisVersicolorSepalLength = scipy.stats.kurtosis(irisVersicolorSepalLength)
print(f"Curtose do comprimento da sépala: {kurtosisVersicolorSepalLength}\n ")
# Valor de curtose 0.59

plt.hist(irisVersicolorSepalWidth,6)
plt.xlabel("Largura da sépala da Versicolor.")
plt.show()



print("Resultados do teste de Curtose para espécie Iris-Virginica \n")

kurtosisVirginicaPetalLength = scipy.stats.kurtosis(irisVirginicaPetalLength)
print(f"Curtose do comprimento da pétala: {kurtosisVirginicaPetalLength} ")
# Valor de curtose -0.25

plt.hist(irisVirginicaPetalLength) 
plt.xlabel("Comprimento da pétala da Virginica.")
plt.show()

kurtosisVirginicaPetalWidth = scipy.stats.kurtosis(irisVirginicaPetalWidth)
print(f"Curtose da largura da pétala: {kurtosisVirginicaPetalWidth}")
# Valor de curtose -0.66

plt.hist(irisVirginicaPetalWidth, 10)
plt.xlabel("Largura da pétala da Virginica")
plt.show()

kurtosisVirginicaSepalLength = scipy.stats.kurtosis(irisVirginicaSepalLength)
print(f"Curtose do comprimento da sépala: {kurtosisVirginicaSepalLength}")
# Valor de curtose -0.87

plt.hist(irisVirginicaSepalLength,8)
plt.xlabel("Comprimento da sépala da Virginica.")
plt.show()

kurtosisVirginicaSepalWidth = scipy.stats.kurtosis(irisVirginicaSepalWidth)
print(f"Curtose da largura da sépala: {kurtosisVirginicaSepalWidth}\n")
# Valor de curtose 0.51

plt.hist(irisVirginicaSepalWidth)
plt.xlabel("Largura da sépala da Virginica.")
plt.show()
