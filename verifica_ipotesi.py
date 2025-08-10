import pandas as pd
import numpy as np
from scipy import stats
from math import sqrt

# === Carica dati ===
df = pd.read_excel("dati_esempio.xlsx")

alpha = 0.05

print("\n=== IPOTESI NULLA E ALTERNATIVA ===")
print("H0: Il parametro della popolazione è uguale al valore atteso.")
print("H1: Il parametro della popolazione è diverso (bidirezionale) o maggiore/minore (monodirezionale).")
print(f"Livello di significatività α = {alpha}")

# === 1) Test binomiale ===
print("\n=== TEST BINOMIALE ===")
# esempio: proporzione di femmine vs 0.5
successi = (df['Sesso'] == 'F').sum()
n = len(df)
res = stats.binomtest(successi, n, p=0.5, alternative="two-sided")
print(f"Femmine: {successi}/{n} → p-value={res.pvalue:.4f}")
if res.pvalue < alpha:
    print("Rifiuto H0: la proporzione differisce da 0.5")
else:
    print("Non rifiuto H0: la proporzione non differisce da 0.5")

# === 2) Test χ² per un campione ===
print("\n=== TEST χ² PER UN CAMPIONE ===")
# esempio: distribuzione Educazione vs modello atteso
f_obs = df['Educazione'].value_counts().sort_index()
# modello atteso: equidistribuzione
k = len(f_obs)
f_exp = np.repeat(len(df)/k, k)
chi2, p = stats.chisquare(f_obs, f_exp)
print(f"F_obs={list(f_obs)}, F_exp={list(f_exp)}, χ²={chi2:.4f}, p-value={p:.4f}")
if p < alpha:
    print("Rifiuto H0: distribuzione diversa dal modello atteso")
else:
    print("Non rifiuto H0: distribuzione coerente con il modello atteso")

# === 3) Z-test per una media ===
print("\n=== TEST Z PER UNA MEDIA ===")
# esempio: Età vs μ₀=25, σ pop=5
mu0 = 25
sigma_pop = 5
x = df['Età'].dropna()
n = len(x)
mean = x.mean()
se = sigma_pop / sqrt(n)
z = (mean - mu0) / se
p = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"Media={mean:.2f}, z={z:.4f}, p-value={p:.4f}")
if p < alpha:
    print("Rifiuto H0: la media differisce da μ₀")
else:
    print("Non rifiuto H0: la media non differisce da μ₀")

# === 4) T-test per una media ===
print("\n=== TEST T PER UNA MEDIA ===")
# esempio: Ansia vs μ₀=15
mu0 = 15
x = df['Ansia'].dropna()
t_stat, p = stats.ttest_1samp(x, popmean=mu0)
print(f"Media={x.mean():.2f}, t={t_stat:.4f}, p-value={p:.4f}")
if p < alpha:
    print("Rifiuto H0: la media differisce da μ₀")
else:
    print("Non rifiuto H0: la media non differisce da μ₀")

# === 5) Test sulla varianza ===
print("\n=== TEST SULLA VARIANZA ===")
# esempio: Empatia vs σ₀²=9
sigma2_0 = 9
x = df['Empatia'].dropna()
n = len(x)
s2 = x.var(ddof=1)
chi2_stat = (n - 1) * s2 / sigma2_0
p = 2 * min(stats.chi2.cdf(chi2_stat, n-1), 1 - stats.chi2.cdf(chi2_stat, n-1))
print(f"Varianza campionaria={s2:.4f}, χ²={chi2_stat:.4f}, p-value={p:.4f}")
if p < alpha:
    print("Rifiuto H0: la varianza differisce da σ₀²")
else:
    print("Non rifiuto H0: la varianza non differisce da σ₀²")