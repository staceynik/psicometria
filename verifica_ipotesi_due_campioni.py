import pandas as pd
import numpy as np
from scipy import stats

# === Carica dati ===
df = pd.read_excel("dati_esempio.xlsx")

alpha = 0.05

print("\n=== MODULO 6 – VERIFICA IPOTESI DUE CAMPIONI ===")

# =============================
# 1) Campioni indipendenti - Scala ordinale (Mann-Whitney U)
# Esempio: Ansia tra Maschi e Femmine
print("\n--- Campioni indipendenti: Scala ordinale (Mann-Whitney U) ---")
maschi = df[df["Sesso"] == "M"]["Ansia"]
femmine = df[df["Sesso"] == "F"]["Ansia"]
u_stat, p_val = stats.mannwhitneyu(maschi, femmine, alternative="two-sided")
print(f"U = {u_stat:.4f}, p = {p_val:.4f}")
if p_val < alpha:
    print("Rifiuto H0: distribuzione dei ranghi diversa tra i gruppi")
else:
    print("Non rifiuto H0: distribuzione simile nei due gruppi")

# =============================
# 2) Campioni indipendenti - Scala metrica I (t-test pooled, varianze uguali)
print("\n--- Campioni indipendenti: Scala metrica I (t-test pooled) ---")
maschi_eta = df[df["Sesso"] == "M"]["Età"]
femmine_eta = df[df["Sesso"] == "F"]["Età"]
t_stat, p_val = stats.ttest_ind(maschi_eta, femmine_eta, equal_var=True)
print(f"t = {t_stat:.4f}, p = {p_val:.4f}")
if p_val < alpha:
    print("Rifiuto H0: medie significativamente diverse")
else:
    print("Non rifiuto H0: medie simili")

# =============================
# 3) Campioni indipendenti - Scala metrica II (t-test Welch, varianze diverse)
print("\n--- Campioni indipendenti: Scala metrica II (t-test Welch) ---")
t_stat, p_val = stats.ttest_ind(maschi_eta, femmine_eta, equal_var=False)
print(f"t (Welch) = {t_stat:.4f}, p = {p_val:.4f}")
if p_val < alpha:
    print("Rifiuto H0: medie significativamente diverse")
else:
    print("Non rifiuto H0: medie simili")

# =============================
# 4) Campioni indipendenti - Scala metrica III (non parametrico: Mann-Whitney)
print("\n--- Campioni indipendenti: Scala metrica III (Mann-Whitney) ---")
u_stat, p_val = stats.mannwhitneyu(maschi_eta, femmine_eta, alternative="two-sided")
print(f"U = {u_stat:.4f}, p = {p_val:.4f}")
if p_val < alpha:
    print("Rifiuto H0: distribuzione dei ranghi diversa")
else:
    print("Non rifiuto H0: distribuzione simile")

# =============================
# 5) Campioni dipendenti - Scala ordinale (Wilcoxon)
print("\n--- Campioni dipendenti: Scala ordinale (Wilcoxon) ---")
# Uso le stesse variabili Stress_Pre e Stress_Post ma trasformo in ranghi ordinali
wil_stat, p_val = stats.wilcoxon(df["Stress_Pre"], df["Stress_Post"])
print(f"W = {wil_stat:.4f}, p = {p_val:.4f}")
if p_val < alpha:
    print("Rifiuto H0: differenza significativa tra le due misure")
else:
    print("Non rifiuto H0: nessuna differenza significativa")

# =============================
# 6) Campioni dipendenti - Scala metrica (t-test appaiato)
print("\n--- Campioni dipendenti: Scala metrica (t-test appaiato) ---")
t_stat, p_val = stats.ttest_rel(df["Stress_Pre"], df["Stress_Post"])
print(f"t = {t_stat:.4f}, p = {p_val:.4f}")
if p_val < alpha:
    print("Rifiuto H0: differenza significativa tra le medie")
else:
    print("Non rifiuto H0: nessuna differenza significativa")
