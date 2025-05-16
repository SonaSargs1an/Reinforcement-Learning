import pandas as pd
from scipy.stats import f_oneway

data = pd.read_csv(r'C:\Users\2023\Desktop\Advertising.csv')

columns_to_compare = ['TV', 'radio', 'newspaper']
values = [data[col] for col in columns_to_compare]

f_stat, p_value = f_oneway(*values)

print("ANOVA արդյունքներ՝")
print(f"F-ստատիստիկա: {f_stat:.2f}")
print(f"p-արժեք: {p_value:.5e}")

def interpret_anova(p_val, alpha=0.05):
    if p_val < alpha:
        return "3 սյունակների միջինները էականորեն տարբեր են։"
    else:
        return "3 սյունակների միջինները էական տարբերություն չունեն։"

print(interpret_anova(p_value))


