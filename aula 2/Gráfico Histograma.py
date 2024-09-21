import numpy as np
import matplotlib.pyplot as plt

# matplotlib.pyplot é uma interface baseada em estado para matplotlib. Ela fornece uma maneira implícitade plotar. 
#Ela também abre figuras na sua tela e atua como o gerenciador de GUI de figuras.

#pyplot é destinado principalmente para plotagens interativas e casos simples de geração de plotagens programáticas

sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6])
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2])


#Histograma

#Divide a faixa de dados em intervalos, chamados intervalos de classe

#No método usado para definir as faixas do histograma, o parâmetro 'bins' precisar conte um valor múltiplo do parâmetro 'range'. 
#Só assim é possível evitar lacunas vazias na plotagem do gráfico.

#plt.hist(conjunto,bins,(range))

plt.hist(sync, 5,(65,95)) #distribuição normal
plt.show() #plota as figuras
plt.hist(asyncr, 5, (65,95))#distribuição assimétrica
plt.show()