import pandas as pd
import numpy as np
import scipy.stats as stats
from math import comb, factorial

# Carica i dati
df = pd.read_excel("dati_esempio.xlsx")

print("\n=== TEOREMA DELLA PROBABILITÀ ===")

# Probabilità semplice: sesso = F
p_femminile = (df['Sesso'] == 'F').mean()
print(f"Probabilità che un soggetto sia femmina: {p_femminile:.2f}")

# Probabilità congiunta: femmina e laurea
p_fem_laurea = ((df['Sesso'] == 'F') & (df['Educazione'] == 'Laurea')).mean()
print(f"Probabilità che un soggetto sia femmina e laureata: {p_fem_laurea:.2f}")

# Probabilità condizionata: laureata dato che è femmina
p_laurea_dato_f = p_fem_laurea / p_femminile if p_femminile > 0 else 0
print(f"Probabilità di essere laureata dato che è femmina: {p_laurea_dato_f:.2f}")

print("\n=== CALCOLO COMBINATORIO ===")

# In quanti modi posso scegliere 2 soggetti dal campione?
n = len(df)
k = 2
combinazioni = comb(n, k)
print(f"Numero di combinazioni di {k} soggetti su {n}: {combinazioni}")

print("\n=== DISTRIBUZIONE BINOMIALE ===")

# Probabilità che esattamente 16 su 30 siano femmine, se p=0.5
p = 0.5
x = 16
binomiale = stats.binom.pmf(x, n, p)
print(f"Probabilità di osservare esattamente {x} femmine su {n} (p=0.5): {binomiale:.4f}")

print("\n=== INTERVALLI DI FIDUCIA ===")

variabili = ['Età', 'Stress_Pre', 'Stress_Post', 'Ansia', 'Empatia']
z = 1.96  # livello di confidenza 95%

for var in variabili:
    media = df[var].mean()
    std = df[var].std()
    n = df[var].count()
    errore_std = std / np.sqrt(n)
    inf = media - z * errore_std
    sup = media + z * errore_std

    print(f"\nIntervallo di confidenza al 95% per {var}:")
    print(f"Media = {media:.2f}, IC95% = ({inf:.2f}, {sup:.2f})")
