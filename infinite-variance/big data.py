import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\\Users\\2023\\Desktop\\Methods.csv')

data['Difference'] = data['Method_A'] - data['Method_B']

t_stat, p_value = stats.ttest_rel(data['Method_A'], data['Method_B'])

alpha = 0.05

if p_value < alpha:
    print("There is a statistically significant difference between the methods (p < 0.05).")
else:
    print("No statistically significant difference found (p > 0.05).")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=data[['Method_A', 'Method_B']], palette="pastel")
plt.title("Method_A vs Method_B")
plt.ylabel("Measurement Value")

plt.subplot(1, 2, 2)
sns.histplot(data['Difference'], kde=True, color='skyblue')
plt.title("Distribution of Differences (A - B)")
plt.xlabel("Difference")
plt.axvline(x=data['Difference'].mean(), color='red', linestyle='--',
            label=f'Mean = {data["Difference"].mean():.2f}')
plt.legend()

plt.tight_layout()
plt.show()
