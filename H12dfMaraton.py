import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (using the uploaded file name)
df = pd.read_csv("filtrovanie_maraton.csv")

# --- DATA CLEANING ---
def time_to_hours(t_str):
    try:
        if str(t_str).strip() == '---' or pd.isna(t_str):
            return None
        parts = str(t_str).split(':')
        h, m, s = map(int, parts)
        return h + m/60 + s/3600
    except:
        return None

df['Čas_hodiny'] = df['Čas'].apply(time_to_hours)
df_clean = df.dropna(subset=['Čas_hodiny', 'Kategórie'])

person_name = "SZÉKELY"
person_data = df_clean[df_clean['Priezvisko'] == person_name].iloc[0]
person_time = person_data['Čas_hodiny']
person_cat = person_data['Kategórie']


# --- 5. KDE PLOT (Final Distribution by Category) ---
plt.figure(figsize=(12, 6))

sns.kdeplot(
    data=df_clean,
    x='Čas_hodiny',
    hue='Kategórie',
    fill=False,
    common_norm=False,
    palette='viridis',
    alpha=0.3
)

plt.axvline(person_time, color='red', linestyle='--', linewidth=2, label=f'{person_name}')


plt.legend(title='Kategórie', loc='upper left')

plt.title(f'Distribúcia časov: {person_name} vs Ostatní')
plt.xlabel('Čas (hodiny)')
plt.ylabel('Hustota (Density)')

plt.show()