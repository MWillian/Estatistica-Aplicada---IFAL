import scipy
import numpy as np
import scipy.stats

#Teste de hipótese

# Conjunto de dados definidos previamente:

sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6]) # Conjunto síncrono
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2]) # Conjunto assíncrono

# TESTE DE NORMALIDADE (Shapiro Wilk)

# Utilizado para determinar a normalidade de um conjunto.

#  Inicialmente definimos hipóteses. Temos a hipótese nula (H0), que indica normalidade na distribuição.
#  Também existe a hipótese alternativa (H1), que nos faz assumir que o conjunto de dados não possui uma distribuição normal.


# Obtemos o p-valor como resultado do teste de Shapiro.Importante para indicar um intervalo de confiança.
# Esse intervalo pode ser variado, mas é utilizado um valor de 95% na maioria dos casos, onde o p-valor será de 0,05(5%). Esse será seu limite (faixa de erro).

# Se o p-valor for menor que o limite (0,05), então a hipótese nula é rejeitada, o que implica em assumir a hipótese H1, onde a distribuição foge da normalidade.
# Se o p-valor for maior que o limite, então a hipótese nula não pode ser rejeitada.


#Teste de Shapiro-Wilk para o conjunto síncrono

stat, pvalueSync = scipy.stats.shapiro(sync)
print(f"P-value do conjunto síncrono {round(pvalueSync,3)}\n") # resultado: 0.656. Logo, com p > 0.05, não podemos negar a hipótese nula.

#Teste de Shapiro-Wilk para o conjunto assíncrono

stat, pvalueAsyncr = scipy.stats.shapiro(asyncr)
print(f"P-value do conjunto assíncrono {round(pvalueAsyncr,3)}\n") # resultado: 0.08. Logo, com p > 0.05, não podemos negar a hipótese nula.


#Se considerarmos a hipótese alternativa(H1, onde a distribuição é anormal), podemos utilizar o teste de assimetria para constatar com maior veracidade a normalidade da distribuição: 


# TESTE DE ASSIMETRIA

# Se o resultado do teste for:
# Igual ou muito próximo a 0, temos uma distribuição simétrica
# Maior do que 0, temos uma distribuição assimétrica com cauda a direita
# Menor do que de 0, temos uma distribuição assimétrica com cauda a esquerda

AssimetriaSync = scipy.stats.skew(sync)
print(f"Teste de assimetria do conjunto síncrono, com resultado: {round(AssimetriaSync,3)}") # resultado 0.31, logo, temos uma distribuição simétrica.
print()

AssimetriaAsyncr = scipy.stats.skew(asyncr)
print(f"Teste de assimetria do conjunto assíncrono, com resultado: {round(AssimetriaAsyncr,3)}") # resultado 1.157, logo, temos uma distribuição assimétrica.
print()

# Para distribuições simétricas, devemos analisar a curtose de seu gráfico 
# De forma resumida, a curtose representa a "elevação" do gráfico, com faixa definida por:
# Para valores maiores que 0 temos uma maior elevação do gráfico
# Para valores iguais a 0 temos uma elevação "intermediária"
# Para valores menores que 0 temos uma menor elevação do gráfico

kurtosisSync = scipy.stats.kurtosis(sync)
print(f"Curtose do gráfico do conjunto síncrono: {kurtosisSync}")# resultado = -0.42, logo, temos uma curtose intermediária
print()