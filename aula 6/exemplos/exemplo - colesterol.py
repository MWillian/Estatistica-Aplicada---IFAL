import numpy as np
import scipy.stats
import scipy

# Amostra pareada: o mesmo objeto participa das duas amostras

before_diet=np.array([224, 235, 223, 253, 253, 224, 244, 225, 259, 220, 242, 240, 239, 229, 276, 254, 237, 227])
after_diet=np.array([198, 195, 213, 190, 246, 206, 225, 199, 214, 210, 188, 205, 200, 220, 190, 199, 191, 218])

stat,p = scipy.stats.shapiro(before_diet)
print(f"P valor Antes da dieta: {p}")

stat,p = scipy.stats.shapiro(after_diet)
print(f"P valor Depois da dieta: {p}")

# teste para amostras pareadas

stat,p = scipy.stats.ttest_rel(before_diet,after_diet)
print(f"Valor p resultado do teste para amostras pareadas: {p}")

print(before_diet.mean())
print(after_diet.mean())

# p valor < 0.05, rejeitamos H0 e assumimos H1. Assumimos médias diferentes. 


