import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Načítanie
df = pd.read_csv('Data_Forms.csv')
df_filtered = df[~df['Pohlavie'].isin(['Žid', 'Non-binary'])].copy()

# Prevod rozsahov na čísla
hours_map = {
    '0': 0, '1-3': 2, '3-6': 4.5, '6-9': 7.5, '9-12': 10.5,
    '12-15': 13.5, '15-18': 16.5, '18-21': 19.5, '21-24': 22.5, '24+': 26
}
age_order = ['0-15', '15-20', '25-35', '35+'] # Logické poradie (skupina 20-25 odstránená nižšie)
age_map = {'0-15': 13, '15-20': 17.5, '20-25': 22.5, '25-35': 30, '35+': 40}

df_filtered['Hodiny_Numeric'] = df_filtered['Hodiny tyždenne'].map(hours_map)
df_filtered['Vek_Numeric'] = df_filtered['Vek'].map(age_map)

# filtrovanie
age_counts = df_filtered['Vek'].value_counts()
valid_ages = age_counts[age_counts > 1].index
df_filtered = df_filtered[df_filtered['Vek'].isin(valid_ages)]

# ZORADENIE osi X podľa veku
df_filtered['Vek'] = pd.Categorical(df_filtered['Vek'], categories=age_order, ordered=True)

# GRAF VIOLIN PLOT (Multivariate)
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_filtered, x='Vek', y='Hodiny_Numeric', hue='Pohlavie',
               split=True, palette="Pastel1", cut=0)
plt.title('Rozdelenie herného času podľa veku a pohlavia', fontsize=14)
plt.ylabel('Týždenné hodiny (odhad)')
plt.xlabel('Veková skupina')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('violin_improved.png')


# GRAF -HEATMAP (Hodiny vs Pohlavie)
hours_order = ['0', '1-3', '3-6', '6-9', '9-12', '12-15', '15-18', '18-21', '21-24', '24+']
pivot_df = df_filtered.pivot_table(index='Hodiny tyždenne', columns='Pohlavie', aggfunc='size', fill_value=0)
pivot_df = pivot_df.reindex([h for h in hours_order if h in pivot_df.index])
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap: Týždenné hodiny a Pohlavie')
plt.savefig('hours_vs_gender_heatmap.png')

# GRAF -TOP KOMPETITÍVNE HRY
plt.figure(figsize=(10, 6))
top_games = df_filtered[df_filtered['Aku "competitive" hru hráš (zatiaľ 1 potom sa dá vrátiť)'] != 'Žiadnu']['Aku "competitive" hru hráš (zatiaľ 1 potom sa dá vrátiť)'].value_counts().head(7)
sns.barplot(x=top_games.values, y=top_games.index, palette='viridis')
plt.title('Top 7 najpopulárnejších kompetitívnych hier')
plt.xlabel('Počet hráčov')
plt.savefig('top_games.png')

gender_counts = df_filtered['Pohlavie'].value_counts()
# Gender Distribution

plt.figure(figsize=(10, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))

plt.title('Gender Distribution (Filtered)')
plt.savefig('Gender Distribution')