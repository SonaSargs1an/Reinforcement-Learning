import pandas as pd
from scipy import stats

data = pd.read_csv(r'C:\Users\2023\Desktop\Wage.csv')

industrial_wage = data[data['jobclass'] == '1. Industrial']['wage']
information_wage = data[data['jobclass'] == '2. Information']['wage']

t_stat, p_value = stats.ttest_ind(industrial_wage, information_wage, equal_var=False)

alpha = 0.01

print(f"t-statistic = {t_stat:.3f}")
print(f"p-value = {p_value:.5f}")

if p_value < alpha:
    print("There is a statistically significant difference between the wages (p < 0.01).")
else:
    print("No statistically significant difference found between the wages (p > 0.01).")
