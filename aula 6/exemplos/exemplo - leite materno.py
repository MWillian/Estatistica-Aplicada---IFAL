
import numpy as np
import scipy.stats
import scipy


only_breast=np.array([794.1, 716.9, 993. , 724.7, 760.9, 908.2, 659.3 , 690.8, 768.7, 717.3 , 630.7, 729.5, 714.1, 810.3, 583.5, 679.9, 865.1])
only_formula=np.array([ 898.8, 881.2, 940.2, 966.2, 957.5, 1061.7, 1046.2, 980.4, 895.6, 919.7, 1074.1, 952.5, 796.3, 859.6, 871.1 , 1047.5, 919.1 , 1160.5, 996.9])
both=np.array([976.4, 656.4, 861.2, 706.8, 718.5, 717.1, 759.8, 894.6, 867.6, 805.6, 765.4, 800.3, 789.9, 875.3, 740. , 799.4, 790.3, 795.2 , 823.6, 818.7, 926.8, 791.7, 948.3])

# teste de normalidade:

stat,pValueOnlyBreast = scipy.stats.shapiro(only_breast)# resultado:
print(f"P valor Only Breast: {pValueOnlyBreast} ")

stat,pValueOnlyFormula = scipy.stats.shapiro(only_formula)
print(f"P valor Only Formula: {pValueOnlyFormula} ")

stat,pValueBoth = scipy.stats.shapiro(both)
print(f"P valor Both: {pValueBoth} ")


test_stat_var, p_value_var = scipy.stats.levene(only_breast,only_formula,both)
print(f"Valor p do teste de Levene para a comparação das variâncias do Only Breast, Only Formula, Both:  {p_value_var}")

# print(only_breast.mean())
# print(only_formula.mean())
# print(both.mean())

# Aplicação do Teste de ANOVA (Análise de variância, teste paramétrico), que analisa as médias
# O teste de anova será sempre utilizado quando se quer comparar a média entre mais de 2 conjuntos.
# O teste analisa se pelo menos 1 das médias é DIFERENTE.

# H0: médias iguais
# H1: pelo menos uma das médias serão diferentes.

f,p_value = scipy.stats.f_oneway(only_breast, only_formula, both)
print(f"Valor p do teste ANOVA para os cojuntos citados: {p_value}") # resultado < 0.05, rejeitamos a hipótese nula, e assumimos H1.

# Pelo menos 1 das médias dos conjuntos é diferente.


# Agora, precisamos realizar um teste Posthocs com os 3 testes T para os conjuntos


tteste, p_value_ttest = scipy.stats.ttest_ind(only_breast,only_formula)
print(f"Valor p de resultado do Teste T para os conjuntos Only breast e Only formula: {p_value_ttest/2}")

tteste, p_value_ttest = scipy.stats.ttest_ind(only_breast,both)
print(f"Valor p de resultado do Teste T para os conjuntos Only breast e Both: {p_value_ttest/2} # valor desajustado devido ao parâmetro bonferroni")

tteste, p_value_ttest = scipy.stats.ttest_ind(only_formula,both)
print(f"Valor p de resultado do Teste T para os conjuntos Only formula e Both: {p_value_ttest/2}")



# !!!!!!!!!!!!!!

# Coclusão 1, alimentar os bebes com leite materno terá um aumento de peso.
# Conclusão 2, o aumento médio dp peso dos bebes que são alimentados com leite materno ou com ambos é o mesmo.