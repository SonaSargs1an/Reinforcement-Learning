import pandas as pd
from scipy.stats import shapiro as shp, levene as lvn
from scipy import stats as st

dataframe = pd.read_csv("methods.csv")

stat_A, p_A = shp(dataframe["Method_A"])
print(f"Shapiro-W (A) = {stat_A}")
print(f"P-Value (A) = {p_A}")
print("Method_A:", "Normal" if p_A > 0.05 else "Not normal")

stat_B, p_B = shp(dataframe["Method_B"])
print(f"Shapiro-W (B) = {stat_B}")
print(f"P-Value (B) = {p_B}")
print("Method_B:", "Normal" if p_B > 0.05 else "Not normal")

w_lev, p_lev = lvn(dataframe["Method_A"], dataframe["Method_B"])
print(f"\nLevene-W = {w_lev}")
print(f"Levene P = {p_lev}")
print("Variance:", "Equal" if p_lev > 0.05 else "Not equal")

t_stat, p_t = st.ttest_rel(dataframe["Method_A"], dataframe["Method_B"])
print(f"\nT-Stat = {t_stat}")
print(f"T P = {p_t}")

if abs(t_stat) < 1e-8:
    print("Result: Methods are the same")
elif abs(t_stat) >= 2.5:
    print("Result: Methods are different")
else:
    print("Result: Methods are similar")