import numpy as np
import scipy.stats
import scipy

test_team=np.array([6.2, 7.1, 1.5, 2,3 , 2, 1.5, 6.1, 2.4, 2.3, 12.4, 1.8, 5.3, 3.1, 9.4, 2.3, 4.1])
developer_team=np.array([2.3, 2.1, 1.4, 2.0, 8.7, 2.2, 3.1, 4.2, 3.6, 2.5, 3.1, 6.2, 12.1, 3.9, 2.2, 1.2 ,3.4])

# normalidade

stat,p = scipy.stats.shapiro(test_team)
print(f"Valor p para normalidade do Test team: {p}")
stat,p = scipy.stats.shapiro(developer_team)
print(f"Valor p para normalidade do Developer_team: {p}")

# ambas distribuições tiveram valor p < 0.05, são anormais

# variancia

test_stat_var, p_value_var = scipy.stats.levene(test_team,developer_team)
print(f"Valor p do teste de Levene para a comparação das variâncias do Sync e Asyncr:  {p_value_var}")

# valor 0.54, a variancia se enquadra como iguais

# teste de man Whitney

stat,p = scipy.stats.mannwhitneyu(test_team,developer_team, alternative = "two-sided") # Man WhitneyU é o não paramétrico
print(f"Valor p do teste de Man Whitney: {p}")

# H0: médias iguais
# H1: médias diferentes

# resultado 0.82, assumimos H0, valores de médias iguais das amostras, refletindo na população.



