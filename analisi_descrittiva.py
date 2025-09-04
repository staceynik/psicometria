
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, norm

# Caricamento dati
df = pd.read_excel("dati_esempio.xlsx")

print("\n=== STATISTICA DESCRITTIVA MODULO 3 ===\n")

# === MODA (nominale) ===
print("\n[MODA] - Variabile: Sesso (nominale)")
moda_sesso = df['Sesso'].mode()[0]
frequenza_sesso = df['Sesso'].value_counts()[moda_sesso]
print(f"Moda: {moda_sesso}, Frequenza: {frequenza_sesso}")

# === MEDIA (metrica) ===
print("\n[MEDIA] - Variabile: Età")
media_eta = df['Età'].mean()
print(f"Media: {media_eta:.2f}")

# === MEDIANA (metrica) ===
print("\n[MEDIANA] - Variabile: Età")
mediana_eta = df['Età'].median()
print(f"Mediana: {mediana_eta:.2f}")

# === MISURE DI VARIABILITÀ A LIVELLO NOMINALE ===
print("\n[MISURE DI VARIABILITÀ - NOMINALE] - Variabile: Sesso")
n = len(df['Sesso'])
variation_ratio = 1 - (frequenza_sesso / n)
proporzioni = df['Sesso'].value_counts(normalize=True)
index_diversity = 1 - np.sum(proporzioni**2)
k = df['Sesso'].nunique()
index_qual_var = index_diversity / (1 - 1/k)
print(f"Variation Ratio: {variation_ratio:.3f}")
print(f"Indice di Diversità: {index_diversity:.3f}")
print(f"Indice di Variazione Qualitativa: {index_qual_var:.3f}")

# === MISURE DI VARIABILITÀ A LIVELLO ORDINALE ===
print("\n[MISURE DI VARIABILITÀ - ORDINALE] - Variabile: Educazione")
livelli = ["Licenza", "Diploma", "Laurea"]
df["Educazione"] = pd.Categorical(df["Educazione"], categories=livelli, ordered=True)
livello_min = df["Educazione"].min()
livello_max = df["Educazione"].max()
print(f"Range ordinale: da {livello_min} a {livello_max}")
frequenze = df["Educazione"].value_counts().sort_index()
frequenze_cum = frequenze.cumsum()
N = frequenze_cum.max()
q1_pos = N * 0.25
q2_pos = N * 0.50
q3_pos = N * 0.75
q1 = frequenze_cum[frequenze_cum >= q1_pos].index[0]
q2 = frequenze_cum[frequenze_cum >= q2_pos].index[0]
q3 = frequenze_cum[frequenze_cum >= q3_pos].index[0]
print(f"Quantili stimati:")
print(f"  Q1 (25%)  = {q1}")
print(f"  Q2 (50%)  = {q2}")
print(f"  Q3 (75%)  = {q3}")

# === MISURE DI VARIABILITÀ A LIVELLO METRICO ===
print("\n[MISURE DI VARIABILITÀ - METRICA] - Variabile: Età")
ssm = np.mean(np.abs(df['Età'] - media_eta))
devianza = np.sum((df['Età'] - media_eta)**2)
varianza = df['Età'].var()
dev_std = df['Età'].std()
coeff_var = (dev_std / media_eta) * 100
print(f"Scostamento semplice medio (SSM): {ssm:.2f}")
print(f"Varianza: {varianza:.2f}")
print(f"Devianza: {devianza:.2f}")
print(f"Deviazione standard: {dev_std:.2f}")
print(f"Coefficiente di variazione: {coeff_var:.2f}%")

# === PUNTEGGI STANDARD E INDICI DI FORMA ===
età = df["Età"].dropna()
media = età.mean()
std = età.std()
plt.hist(età, bins=10, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Dati osservati')
xmin, xmax = età.min(), età.max()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, media, std)
plt.plot(x, p, 'r--', linewidth=2, label='Curva Normale Teorica')
plt.title("Distribuzione dell'Età con curva normale")
plt.xlabel("Età")
plt.ylabel("Densità")
plt.legend()
plt.grid(True)
plt.show()
