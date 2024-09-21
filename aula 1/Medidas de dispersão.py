import numpy as np

# A biblioteca Numpy(Numerical Python) faz o manejo de matrizes, cálculo e fornece um grande conjunto de funções e operações numéricas.
# A biblioteca statistics é uma biblioteca Python integrada que fornece funções para calcular estatísticas matemáticas de dados numéricos.
 
# Duas bases de dados que serão utilizadas para realizar as análises estatísticas

sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6]) # Conjunto síncrono
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2]) # Conjunto assíncrono

#Quartis dos conjunto síncrono

#1º Quartil
Q1Sync = np.percentile(sync,25)
print(f"Primeiro quartil do conjunto síncrono: {Q1Sync}")
print()

#3º Quartil

Q3Sync = np.percentile(sync,75)
print(f"Terceiro quartil do conjunto síncrono: {Q3Sync}")
print()

#Quartis dos conjunto síncrono

#1º Quartil
Q1Asyncr = np.percentile(asyncr,25)
print(f"Primeiro quartil do conjunto assíncrono: {Q1Asyncr}")
print()

#3º Quartil
Q3Asyncr = np.percentile(asyncr,75)
print(f"Terceiro quartil do conjunto assíncrono: {Q3Asyncr}")
print()

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------



# Amplitude (é dada por R = Xmáx - Xmin)

print(f"Amplitude sync: {sync.ptp()}")
print(f"Amplitude async: {asyncr.ptp()}")
print()

#Amplitude interquartil (dada pela diferença: Q3-Q1)

print(f"Intervalo interquartil do conjunto sync: {Q3Sync-Q1Sync}")
print(f"Intervalo interquartil do conjunto asyncr: {Q3Asyncr-Q1Asyncr}")
print()


#Variância

#A diferença para o cálcula das variâncias está na característica do conjunto, onde para população, usamos ddof=0 como parâmetro e para amostra usamos ddof=1.

variânciaSync = sync.var(ddof= 1)
print(f"Variância da amostra do conjunto síncrono: {variânciaSync}")

variânciaAsyncr = asyncr.var(ddof=1)
print(f"Variância da amostra do conjunto assíncrono: {variânciaAsyncr}")

#Desvio padrão

#O desvio padrão da amostra é dado por: desvio1 = sync.std(ddof=1)

desvioSync = sync.std(ddof=1)
print(f"Desvio padrão da amostra sync: {desvioSync}")

desvioAsyncr = asyncr.std(ddof=1)
print(f"Desvio padrão da amostra asyncr: {desvioAsyncr}")