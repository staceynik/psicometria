import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import pi

# Carica i dati
file = "dati_esempio.xlsx"
df = pd.read_excel(file)

# Imposta lo stile dei grafici
sns.set(style="whitegrid")

# === RAPPRESENTAZIONE GRAFICA DEI DATI NOMINALI E ORDINALI ===

# 1. Grafico a barre - Distribuzione delle osservazioni per mese

ordine_mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno"]
df['Mese'].value_counts().reindex(ordine_mesi).plot(kind='bar')
plt.title("Distribuzione dei soggetti per mese di rilevazione")
plt.xlabel("Mese")
plt.ylabel("Frequenza")
plt.grid(True)
plt.tight_layout()
plt.show() 

# 2. Grafico a torta (distribuzione percentuale Educazione)
df['Educazione'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Distribuzione percentuale - Educazione")
plt.ylabel("")
plt.tight_layout()
plt.show()

# === RAPPRESENTAZIONE GRAFICA DELLE TABELLE DI CONTINGENZA ===

# 3. Barre affiancate (Sesso x Educazione)
tab_multipla = pd.crosstab(df['Sesso'], df['Educazione'])
tab_multipla.plot(kind='bar', stacked=False)
plt.title("Barre affiancate - Sesso e Educazione")
plt.xlabel("Sesso")
plt.ylabel("Frequenza")
plt.legend(title="Educazione")
plt.grid(True)
plt.tight_layout()
plt.show()

# === RAPPRESENTAZIONE GRAFICA DEI DATI METRICI ===

# 4. Istogramma (Età)
plt.figure()
sns.histplot(df['Età'], bins=7, kde=False)
plt.title("Istogramma dell'età")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.show()

# 5. Poligono di frequenza (Stress_Pre)
plt.figure()
conteggi = df['Stress_Pre'].round().value_counts().sort_index()
plt.plot(conteggi.index, conteggi.values, marker='o')
plt.title("Poligono di frequenza - Stress Pre")
plt.xlabel("Valori")
plt.ylabel("Frequenza")
plt.grid(True)
plt.show()

# 6. Ogiva (frequenze cumulative - Empatia)
plt.figure()
dati_ordinati = np.sort(df['Empatia'])
cumulata = np.arange(1, len(dati_ordinati)+1) / len(dati_ordinati)
plt.plot(dati_ordinati, cumulata, drawstyle='steps-post')
plt.title("Ogiva cumulativa - Empatia")
plt.xlabel("Empatia")
plt.ylabel("Frequenza cumulativa")
plt.grid(True)
plt.show()

# === ALTRI TIPI DI GRAFICI ===

# 7. Serie storica (Stress_Post medio per Mese)
plt.figure()
media_mensile = df.groupby("Mese")["Stress_Post"].mean().reindex(
    ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno"])
media_mensile.plot(marker='o')
plt.title("Serie storica - Stress Post medio per mese")
plt.xlabel("Mese")
plt.ylabel("Stress Post medio")
plt.grid(True)
plt.show()

# 8. Variabili circolari (Radar plot per variabili psicologiche, per Sesso)
variabili = ['Stress_Pre', 'Ansia', 'Empatia']
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

# 9. Funzione psicometrica (Stimolo vs Risposta media)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dati_esempio.xlsx", sheet_name="Sheet1")
colonne_soggetti = [col for col in df.columns if col.startswith("Soggetto")]
df['Media_Risposte'] = df[colonne_soggetti].mean(axis=1)
df = df.sort_values("Stimolo")

# Grafico: funzione psicometrica
plt.figure()
plt.plot(df['Stimolo'], df['Media_Risposte'], marker='o')
plt.title("Funzione psicometrica")
plt.xlabel("Intensità dello stimolo")
plt.ylabel("Probabilità di risposta 'sì'")
plt.grid(True)
plt.tight_layout()
plt.show()



