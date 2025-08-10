import pandas as pd
import numpy as np

# Carica i dati
df = pd.read_excel("dati_esempio.xlsx")

print("\n=== STATISTICA DESCRITTIVA ===\n")

# --- NOMINALE: Moda e frequenza ---
print("\n[SCALA NOMINALE] - Variabile: Sesso")
moda_sesso = df['Sesso'].mode()[0]
frequenza_sesso = df['Sesso'].value_counts()[moda_sesso]
print(f"Moda: {moda_sesso}, Frequenza: {frequenza_sesso}")

# --- ORDINALE: Moda, frequenze, cumulata ---
print("\n[SCALA ORDINALE] - Variabile: Educazione")
freq_ed = df['Educazione'].value_counts().reindex(["Licenza", "Diploma", "Laurea"])
cum_ed = freq_ed.cumsum()
print("Frequenze assolute:\n", freq_ed)
print("Frequenze cumulative:\n", cum_ed)

# --- METRICA: Media, Mediana, Moda, Varianza, Dev.St, Range, SSM ---
variabili_metriche = ['Età', 'Stress_Pre', 'Stress_Post', 'Ansia', 'Empatia']

for var in variabili_metriche:
    print(f"\n[SCALA METRICA] - Variabile: {var}")
    media = df[var].mean()
    mediana = df[var].median()
    moda = df[var].mode().iloc[0]
    varianza = df[var].var()
    deviazione_std = df[var].std()
    valore_min = df[var].min()
    valore_max = df[var].max()
    range_val = valore_max - valore_min
    ssm = np.mean(np.abs(df[var] - media))

    print(f"Media: {media:.2f}, Mediana: {mediana:.2f}, Moda: {moda}")
    print(f"Varianza: {varianza:.2f}, Deviazione standard: {deviazione_std:.2f}")
    print(f"Range: {range_val:.2f}, Scarto semplice medio (SSM): {ssm:.2f}")
