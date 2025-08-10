import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carica i dati
file = "dati_esempio.xlsx"
df = pd.read_excel(file)

# Imposta lo stile dei grafici
sns.set(style="whitegrid")

# Istogramma: distribuzione di Età
plt.figure()
sns.histplot(df['Età'], bins=7, kde=False)
plt.title("Istogramma dell'età")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.show()

# Poligono di frequenza: Stress_Pre
plt.figure()
conteggi = df['Stress_Pre'].round().value_counts().sort_index()
plt.plot(conteggi.index, conteggi.values, marker='o')
plt.title("Poligono di frequenza - Stress Pre")
plt.xlabel("Valori")
plt.ylabel("Frequenza")
plt.grid(True)
plt.show()

# Ogiva (frequenze cumulative): Empatia
plt.figure()
dati_ordinati = np.sort(df['Empatia'])
cumulata = np.arange(1, len(dati_ordinati)+1) / len(dati_ordinati)
plt.plot(dati_ordinati, cumulata, drawstyle='steps-post')
plt.title("Ogiva cumulativa - Empatia")
plt.xlabel("Empatia")
plt.ylabel("Frequenza cumulativa")
plt.grid(True)
plt.show()

# Serie storica: media dello Stress_Post per mese
plt.figure()
media_mensile = df.groupby("Mese")["Stress_Post"].mean().reindex(
    ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno"])
media_mensile.plot(marker='o')
plt.title("Serie storica - Stress Post medio per mese")
plt.xlabel("Mese")
plt.ylabel("Stress Post medio")
plt.grid(True)
plt.show()

# Radar plot: media per variabili psicologiche (per sesso)
from math import pi
variabili = ['Stress_Post', 'Ansia', 'Empatia']

df_radar = df.groupby('Sesso')[variabili].mean()

categorie = list(df_radar.columns)
N = len(categorie)

for sesso in df_radar.index:
    valori = df_radar.loc[sesso].values.flatten().tolist()
    valori += valori[:1]
    angoli = [n / float(N) * 2 * pi for n in range(N)]
    angoli += angoli[:1]

    plt.figure()
    ax = plt.subplot(111, polar=True)
    plt.xticks(angoli[:-1], categorie)
    ax.plot(angoli, valori, linewidth=1, linestyle='solid', label=sesso)
    ax.fill(angoli, valori, alpha=0.3)
    plt.title(f"Radar plot - {sesso}")
    plt.legend(loc='upper right')
    plt.show()

# Funzione psicometrica: proporzione di risposte "sì" in funzione dello stimolo
plt.figure()
df_psico = df.groupby("Stimolo")["Risposta"].mean()
plt.plot(df_psico.index, df_psico.values, marker='o')
plt.title("Funzione psicometrica")
plt.xlabel("Intensità dello stimolo")
plt.ylabel("Probabilità di risposta 'sì'")
plt.grid(True)
plt.show()
