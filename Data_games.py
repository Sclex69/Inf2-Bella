import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Data_Forms.csv')
sns.set_theme(style="whitegrid")

# --- DATA CLEANING ---
# Filter out specific gender categories as requested
df_filtered = df[~df['Pohlavie'].isin(['Žid', 'Non-binary'])]

# Clean 'Ročník' (Mapping teachers and grades)
def clean_rocnik(val):
    if pd.isna(val): return 'Unknown'
    val_str = str(val).strip().lower()
    return f'Ročník {val_str}' if val_str.isdigit() else 'Učiteľ'

df_filtered['Ročník_Cleaned'] = df_filtered['Ročník'].apply(clean_rocnik)

# Define standard orders for sorting
hours_order = ['0', '1-3', '3-6', '6-9', '9-12', '12-15', '15-18', '18-21', '21-24', '24+']
age_order = ['0-15', '15-20', '20-25', '25-35', '35+']

# --- VISUALIZATION 1: HEATMAP ---
plt.figure(figsize=(10, 6))
pivot_df = df_filtered.pivot_table(index='Hodiny tyždenne', columns='Pohlavie', aggfunc='size', fill_value=0)
# Sort and filter the pivot table
pivot_df = pivot_df.reindex([h for h in hours_order if h in pivot_df.index])
sns.heatmap(pivot_df, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap: Weekly Hours vs. Gender (Filtered)')
plt.savefig('hours_vs_gender_heatmap_filtered.png')

# --- VISUALIZATION 2: DASHBOARD ---
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gender Distribution
gender_counts = df_filtered['Pohlavie'].value_counts()
axes[0, 0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
axes[0, 0].set_title('Gender Distribution (Filtered)')

# Weekly Hours
sns.countplot(data=df_filtered, x='Hodiny tyždenne', order=[h for h in hours_order if h in df_filtered['Hodiny tyždenne'].unique()], ax=axes[0, 1], palette='viridis')
axes[0, 1].set_title('Weekly Gaming Hours Frequency')
axes[0, 1].tick_params(axis='x', rotation=45)

# Top Games
top_games = df_filtered[df_filtered['Aku "competitive" hru hráš (zatiaľ 1 potom sa dá vrátiť)'] != 'Žiadnu']['Aku "competitive" hru hráš (zatiaľ 1 potom sa dá vrátiť)'].value_counts().head(7)
sns.barplot(x=top_games.values, y=top_games.index, ax=axes[1, 0], palette='magma')
axes[1, 0].set_title('Top 7 Competitive Games')

# Age Distribution
sns.countplot(data=df_filtered, x='Vek', order=[a for a in age_order if a in df_filtered['Vek'].unique()], ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title('Age Group Distribution')

plt.tight_layout()
plt.savefig('gaming_stats_filtered.png')