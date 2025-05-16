import pandas as pd
from scipy.stats import shapiro, ttest_ind, levene

data = pd.read_csv('Wage.csv')
data['jobclass'] = data['jobclass'].str.strip()

industrial_wages = data[data['jobclass'] == '1. Industrial']['wage'].dropna()
information_wages = data[data['jobclass'] == '2. Information']['wage'].dropna()

shapiro_stat_industrial, p_value_industrial = shapiro(industrial_wages)
print('Industrial - W:', shapiro_stat_industrial)
print('Industrial - p:', p_value_industrial)

shapiro_stat_information, p_value_information = shapiro(information_wages)
print('Information - W:', shapiro_stat_information)
print('Information - p:', p_value_information)

levene_stat, levene_p = levene(industrial_wages, information_wages)
print('\nLevene - stat:', levene_stat)
print('Levene - p:', levene_p)

t_statistic, t_p_value = ttest_ind(industrial_wages, information_wages, equal_var=False)
print('\nT-test results:')
print('t:', t_statistic)
print('p:', t_p_value)

if t_p_value > 0.01:
    print("No significant difference between Industrial and Information wages (fail to reject H0)")
else:
    print("Significant difference between Industrial and Information wages (reject H0)")