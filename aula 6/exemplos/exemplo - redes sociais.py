import numpy as np
import scipy.stats
import scipy

youtube = np.array([1913, 1879, 1939, 2146, 2040, 2127, 2122, 2156, 2036, 1974, 1956, 2146, 2151, 1943, 2125])
instagram = np.array([2305., 2355., 2203., 2231., 2185., 2420., 2386., 2410., 2340., 2349., 2241., 2396., 2244., 2267., 2281.])
facebook = np.array([2133., 2522., 2124., 2551., 2293., 2367., 2460., 2311., 2178., 2113., 2048., 2443., 2265., 2095., 2528.])

stat,p = scipy.stats.shapiro(youtube)
print(f"Normalidade do conjunto Youtube: {p} ") # assimétrico
stat,p = scipy.stats.shapiro(instagram)
print(f"Normalidade do conjunto Youtube: {p} ") # normal
stat,p = scipy.stats.shapiro(facebook)
print(f"Normalidade do conjunto Youtube: {p} ") # normal

# variancia

test_stat_var, p_value_var = scipy.stats.levene(youtube,instagram,facebook)
print(f"Valor p do teste de Levene para a comparação das variâncias do conjunto Youtube, instagram, Facebook:  {p_value_var}")

# variancia diferente, aplicamos o teste não paramétrico de Kruskal-Wallis

f, p = scipy.stats.kruskal(youtube,instagram,facebook)
print(f"Valor p da anova de Kruskal Wallis: {p}")
# valor < 0.05, rejeita H0, consideramos que pelo menos 1 média será diferente.

# aplicando posthocs sendo Man whitney

stat,p = scipy.stats.mannwhitney(youtube,instagram,facebook)# Man Whitney é o não paramétrico. (não consegui importar o scikit)
print(f"Valor p do teste de Man Whitney: {p}")


