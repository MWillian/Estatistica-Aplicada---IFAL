import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6])
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2])

#Boxplot

#Apresenta o centro, dispersão, desvio padrão da simetria e outliers.
# sns.boxplot(sync)

# Para plotar dois conjuntos no mesmo gráfico usar: 
sns.boxplot([sync,asyncr])

# Alteração do nome dos dois gráficos

#plt.xticks([numeração do gráfico plotado],["nome desejado"])

plt.xticks([0,1],["Sync","Asyncr"])

#Alteração da legenda do eixo x
plt.xlabel("Worktype")

# # #alteração da legenda do eixo y
plt.ylabel("Hours")
plt.show()