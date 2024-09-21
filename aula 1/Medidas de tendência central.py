import numpy as np
import statistics as static

# A biblioteca Numpy(Numerical Python) faz o manejo de matrizes, cálculo e fornece um grande conjunto de funções e operações numéricas.
# A biblioteca statistics é uma biblioteca Python integrada que fornece funções para calcular estatísticas matemáticas de dados numéricos.
 
# Duas bases de dados que serão utilizadas para realizar as análises estatísticas

sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6]) # Conjunto síncrono
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2]) # Conjunto assíncrono

print("Medidas de tendência central")
print()


#CÁLCULO DE MÉDIA DOS CONJUNTOS

MeanSync = sync.mean()
print(f"Média sync: {MeanSync}")

MeanAsyncr = asyncr.mean()
print(f"Média asyncr: {MeanAsyncr}")
print()


#CÁLCULO DE MÉDIANA DOS CONJUNTOS

MedianSync = np.median(sync)
print(f"Mediana sync: {MedianSync}")

MedianAsyncr = np.median(asyncr)
print(f"Mediana asyncr: {MedianAsyncr}")
print()

#CÁLCULO DE MODA DOS CONJUNTOS

modaSync = static.mode([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6])
print(f"Moda do conjunto síncrono: {modaSync}")
print()

modaAsyncr = static.mode([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2,78.2])
print(f"Moda do conjunto assíncrono: {modaAsyncr}")
print()

# No caso de haver mais de um valor de moda:

modaSync = static.multimode([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6,80.6])
print(f"Moda do conjunto síncrono: {modaSync}")

modaAsyncr = static.multimode([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2,78.2])
print(f"Moda do conjunto assíncrono: {modaAsyncr}")
print()


#CÁLCULO DE PERCENTIL

#Os percentis são divididos 10 em 10%, indo de P1(10%) até P9(90).

#Para encontrar os quartis do conjunto síncrono (Os Quartis vão de Q1 até Q3, de 25 em 25%).

#A funcão len() retorna o tamanho da lista, com isso é possível encontrar a posição dos quartis.

#1º Quartil
Q1Sync = np.percentile(sync,25)
print(f"Primeiro quartil do conjunto síncrono: {Q1Sync}")
print()

#3º Quartil

Q3Sync = np.percentile(sync,75)
print(f"Terceiro quartil do conjunto síncrono: {Q3Sync}")
print()

#Para o conjunto assíncrono

#1º Quartil
Q1Asyncr = np.percentile(asyncr,25)
print(f"Primeiro quartil do conjunto assíncrono: {Q1Asyncr}")
print()

#3º Quartil
Q3Asyncr = np.percentile(asyncr,75)
print(f"Terceiro quartil do conjunto assíncrono: {Q3Asyncr}")
print()