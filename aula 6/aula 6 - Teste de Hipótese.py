# TESTES DE HIPÓTESE
import numpy as np
import scipy.stats
import scipy


only_breast=np.array([794.1, 716.9, 993. , 724.7, 760.9, 908.2, 659.3 , 690.8, 768.7, 717.3 , 630.7, 729.5, 714.1, 810.3, 583.5, 679.9, 865.1])
only_formula=np.array([ 898.8, 881.2, 940.2, 966.2, 957.5, 1061.7, 1046.2, 980.4, 895.6, 919.7, 1074.1, 952.5, 796.3, 859.6, 871.1 , 1047.5, 919.1 , 1160.5, 996.9])
both=np.array([976.4, 656.4, 861.2, 706.8, 718.5, 717.1, 759.8, 894.6, 867.6, 805.6, 765.4, 800.3, 789.9, 875.3, 740. , 799.4, 790.3, 795.2 , 823.6, 818.7, 926.8, 791.7, 948.3])

test_team=np.array([6.2, 7.1, 1.5, 2,3 , 2, 1.5, 6.1, 2.4, 2.3, 12.4, 1.8, 5.3, 3.1, 9.4, 2.3, 4.1])
developer_team=np.array([2.3, 2.1, 1.4, 2.0, 8.7, 2.2, 3.1, 4.2, 3.6, 2.5, 3.1, 6.2, 12.1, 3.9, 2.2, 1.2 ,3.4])

youtube = np.array([1913, 1879, 1939, 2146, 2040, 2127, 2122, 2156, 2036, 1974, 1956, 2146, 2151, 1943, 2125])
instagram = np.array([2305., 2355., 2203., 2231., 2185., 2420., 2386., 2410., 2340., 2349., 2241., 2396., 2244., 2267., 2281.])
facebook = np.array([2133., 2522., 2124., 2551., 2293., 2367., 2460., 2311., 2178., 2113., 2048., 2443., 2265., 2095., 2528.])

before_diet=np.array([224, 235, 223, 253, 253, 224, 244, 225, 259, 220, 242, 240, 239, 229, 276, 254, 237, 227])
after_diet=np.array([198, 195, 213, 190, 246, 206, 225, 199, 214, 210, 188, 205, 200, 220, 190, 199, 191, 218])

piedpiper=np.array([4.57, 4.55, 5.47, 4.67, 5.41, 5.55, 5.53, 5.63, 3.86, 3.97, 5.44, 3.93, 5.31, 5.17, 4.39, 4.28, 5.25])
endframe = np.array([4.27, 3.93, 4.01, 4.07, 3.87, 4. , 4. , 3.72, 4.16, 4.1 , 3.9 , 3.97, 4.08, 3.96, 3.96, 3.77, 4.09])

sync = np.array([94,84.9,82.6,69.5,80.1,79.6,81.4,77.8,81.7,78.8,73.2,87.9,87.9,93.5,82.3,79.3,78.3,71.6,88.6,74.6,74.1,80.6]) # Conjunto síncrono
asyncr = np.array([77.1,71.7,91,72.2,74.8,85.1,67.6,69.9,75.3,71.7,65.7,72.6,71.5,78.2]) # Conjunto assíncrono


# Precisamos checar a normalidade:

stat,pValueSync = scipy.stats.shapiro(sync)# resultado: 0.6555
print(f"P valor sync: {pValueSync} ")

stat,pValueAsyncr = scipy.stats.shapiro(asyncr)# resultado: 0.08030
print(f"P valor sync: {pValueAsyncr}\n ")

# Ambos os conjuntos possuem distribuição NORMAL


# Após, precisamos checar a homogeneidade de Levene:

# H0: As variâncias são iguais
# H1: As variâncias são diferentes

test_stat_var, p_value_var = scipy.stats.levene(sync,asyncr)
print(f"Valor p do teste de Levene para a comparação das variâncias do Sync e Asyncr:  {p_value_var}")# resultado 0.8148

# Com valor p > 0.05, consideramos a H0, que afirma a igualdade das variâncias.

# Dado esse cenário, onde ambas as amostras são normais, e os seus valores de variabilidade são iguais, podemos aplicar o Teste T

# T-TESTE, teste paramétrico, vai analisar os valores das médias dos dois conjuntos, e definir se são estatísticamente iguais ou não.

# H0: as médias são iguais
# H1: as médias são diferentes

tteste, p_value_ttest = scipy.stats.ttest_ind(sync, asyncr)
print(f"Valor p de resultado do Teste T para os conjuntos syn e asyncr: {p_value_ttest/2}")# resultado: 0.007535. É preciso dividir o p valor por 2 para realizar o teste, pois é um teste one sided(analisa somente um lado da distribuição).

# Dessa forma, podemos afirmar que, de acordo com os testes estatísticos, as médias dos conjuntos são diferentes, pois tivemos o valor p < 0.05.


# roteiro para análise das médias:

#passo 1: analisar a normalidade do conjunto (p > 0.05 = normal, H0. p < 0.05 = assumir assimetria, H1)
#passo 2: checar a homogeneidade dos conjuntos por meio do teste de Levene (análise de variância. p > 0.05 = variâncias iguais, H0. p < 0.05 = variâncias distintas, H1)

# Distribuição normal, variâncias iguais:teste-t
#se ambos os conjuntos tiverem distribuição normal e valores de variância iguais, podemos utilizar o teste-t(teste paramétrico) para checar se as médias dos conjuntos são estatísticamente iguais.

# Distribuição assimétrica, variâncias iguais: Man-Whitney U
#se ambos os conjuntos tiverem distribuição assimétrica e valores de variância iguais, podemos utilizar o teste não paramétrico de ManWhitneyU (p > 0.05 = médias dos conjuntos estatisticamente iguais. p < 0.05 = médias dos conjuntos estatisticamente distintas)  

# 3 amostras independentes, distribuição normal, variâncias iguais: ANOVA
#se desejo analisar os valores da média entre 3 ou mais conjuntos independentes, posso utilizar o teste de ANOVA(análise de variância) desde que os conjuntos tenham distribuição normal o resultado do teste de Levene indique variâncias iguais. O teste ANOVA confirma se pelo menos 1 das médias é distinta das outras (p > 0.05 = média iguais, H0. p < 0.05 = média distintas, H1).
#para identificar qual das 3 é a diferente, utiliza-se um teste de post-hoc. Nesse caso, pode-se utilizar o teste-t com ajuste de bonferroni como parâmetro (maior precisão).
#testes post-hoc ajustam o nível de significância para evitar conclusões errôneas ao fazer múltiplas comparações. É como se o ANOVA dissesse que há algo interessante em um conjunto de dados, e os testes post-hoc ajudassem a descobrir exatamente onde essa diferença está.

# 3 amostras independentes, distribuições assimétrica(pelo menos 1), variância diferentes
# se desejo analisar os valores da média entre 3 ou mais conjuntos, sendo pelo menos 1 deles com distribuição assimétrica, é possível utilizar o teste não paramétrico de Kruskal-Wallis.
# o teste de kruskal-wallis pode ser executado se pelo menos 1 dos conjuntos tiver distribuição assimétrica e valores variâncias distintos (levene p < 0.05)
# 
# Distribuição normal, amostras pareadas: t-test para amostras pareadas
# aqui só é preciso realizar o teste t citado, e chegar os valores p.