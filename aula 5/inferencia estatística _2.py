import numpy as np
import math

# A inferência estatística é focada em tirar conclusões acerca de um ou mais parâmetros de uma população, a partir de uma amostra.

# De início, precisamos entender que a letra x(x barra) se compreende para os valores de média amostral. E "M" compreende a média populacional.
# A intenção aqui é RELACIONAR os dois valores de média.

# ^p = x/n compreende a proporção amostral, e "p" compreende a proporção populacional.
# Para o caso acima, x = valor hipotético, n = valor total.

# Exemplo: 1000 pessoas viram um anúncio, e 300 clicaram nesse anúncio, logo temos: 300/1000 = 0,3. Esse resutado corresponde ao valor de CONVERSÃO.


# Formas de cálcular os intervalos de erro de uma análise:

# Fórmula do Erro Padrão
# EP(x) = S/sqrt(n)


Conjunto1 = np.array([41.60,41.48,42.34,41.95,41.86,42.18,41.72,42.26,41.81,42.04])
Conjunto2 = np.array([24.1514,27.4145,20.4000,22.5151,28.5152,28.5611,21.2489,20.9983,24.9840,22.6245])

# Cálculo do erro padrão utilizando a fórmula base
erroPadrão = Conjunto1.std(ddof=1)/math.sqrt(len(Conjunto1))
print(f"Valor do erro padrão do conjunto 1 utilizando a fórmula base: {erroPadrão}")
print(f"Desvio padrão do conjunto 1 utilizando a fórmula base: {Conjunto1.std(ddof=1)}")

# Média do conjunto 1
media = Conjunto1.mean()
print(f"Média do conjunto da amostral: {media}")
print(f"Intervalo para média populacional: {media - (3*erroPadrão)} --- {media + (3*erroPadrão)}\n")


# Podemos inserir a média populacional dentro do resultado obtido:
# A média populacional = 41.924, deve estar dentro do intervalo de 41.65 até 42.193.
# Em outras palavras, podemos concluir que a média populacional "M" vai estar dentro do intervalo, variando de 41.65 até 42.193.


# Utilização do gráfico de Boostrap para calcular a média populacional

# Teste com amostra aleatória
Boostsample = np.random.choice(Conjunto1, size = 10, replace = True)

Lista = []
# "for" para gerar conjuntos aleatório baseados no conjunto1, e adicionar o valor da média desses conjuntos em uma lista
for n in range (0,200):
    Boostsample = np.random.choice(Conjunto1, size = 10, replace = True)
    Lista.append(Boostsample.mean())

mediaLista = np.mean(Lista)
print(f"Valor médio da lista com médias de conjuntos aleatórios: {mediaLista}")
bootmean_std = np.std(Lista)
print(f"Desvio padrão da lista {bootmean_std}\n")


# Calculo para o conjunto 2 (Conjunto com maior variação de valores):

print(f"Cálculo utilizando a fórmula padrão: \n")
erroPadrão2 = Conjunto2.std(ddof=1)/math.sqrt(len(Conjunto2))
print(f"Erro padrão do conjunto 2: {erroPadrão2}")
print(f"Desvio padrão do conjunto 2: {Conjunto2.std(ddof=1)}")

media = Conjunto2.mean()
print(f"Média do conjunto 2 : {media}")
print(f"Intervalo para média populacional do conjunto 2: {media - (3*erroPadrão2)} --- {media + (3*erroPadrão2)}\n\n")

print(f"Cálculo utilizando boostrap: \n")
Lista2 = []
for n in range (0,200):
    Boostsample = np.random.choice(Conjunto2, size = 10, replace = True)
    Lista2.append(Boostsample.mean())
mediaLista2 = np.mean(Lista2)
print(f"Média do conjunto 2 seguindo o cálculo de boostrap: {mediaLista2}")
stdLista2 = np.std(Lista2)
print(f"Intervalo utilizando o cálculo de boostrap: {mediaLista2 - (3*erroPadrão2)} --- {mediaLista2 + (3*erroPadrão2)}")
