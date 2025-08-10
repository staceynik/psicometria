import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

# === Carica dati ===
df = pd.read_excel("dati_esempio.xlsx")

alpha = 0.05

print("\n=== MODULO 8 – MISURE DI ASSOCIAZIONE TRA VARIABILI ===")

# =============================
# 1) Correlazione (scala metrica)
print("\n--- Correlazione (Pearson e Spearman) ---")
x = df["Stress_Pre"]
y = df["Stress_Post"]

# Pearson
r_pearson, p_pearson = stats.pearsonr(x, y)
# Spearman
r_spearman, p_spearman = stats.spearmanr(x, y)

def interpreta_corr(r):
    r_abs = abs(r)
    if r_abs < 0.2:
        forza = "trascurabile"
    elif r_abs < 0.4:
        forza = "debole"
    elif r_abs < 0.6:
        forza = "moderata"
    elif r_abs < 0.8:
        forza = "forte"
    else:
        forza = "molto forte"
    segno = "positiva" if r > 0 else "negativa"
    return f"{forza}, {segno}"

print(f"Pearson r = {r_pearson:.4f}, p = {p_pearson:.4f} → {interpreta_corr(r_pearson)}")
print(f"Spearman ρ = {r_spearman:.4f}, p = {p_spearman:.4f} → {interpreta_corr(r_spearman)}")

# =============================
# 2) Analogia tra ANOVA e regressione
print("\n--- Analogia tra ANOVA e regressione ---")
# Esempio: Stress_Post come variabile dipendente, Sesso come fattore
model = smf.ols('Stress_Post ~ C(Sesso)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("\nANOVA:")
print(anova_table)

print("\nRegressione (stesso modello codificato):")
print(model.summary())

print("\nNota: L'F della riga 'C(Sesso)' in ANOVA coincide con l'F di regressione per il predittore 'Sesso'.")