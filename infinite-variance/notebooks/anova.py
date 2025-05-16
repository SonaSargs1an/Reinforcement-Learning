import pandas as pd
from scipy.stats import f_oneway

# Տվյալների ներբեռնում
data = pd.read_csv(r'C:\Users\2023\Desktop\Advertising.csv')

# Ստեղծում ենք ցուցակ տվյալների համար
columns_to_compare = ['TV', 'radio', 'newspaper']
values = [data[col] for col in columns_to_compare]

# Կատարում ենք ANOVA վերլուծություն
f_stat, p_value = f_oneway(*values)

# Արդյունքների տպում
print("ANOVA արդյունքներ՝")
print(f"F-ստատիստիկա: {f_stat:.2f}")
print(f"p-արժեք: {p_value:.5e}")

# Գնահատման ֆունկցիա
def interpret_anova(p_val, alpha=0.05):
    if p_val < alpha:
        return "Երեք սյունակների միջ"

