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

# --- 1. PIE CHART (Top 5 Nationalities) ---
plt.figure(figsize=(8, 8))
top_nations = df['Nár.'].value_counts().head(5)
plt.pie(top_nations, labels=top_nations.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Podiel 5 najčastejších národností')
plt.savefig('Pie_Bella.png', bbox_inches='tight')
plt.show()


# --- 2. HISTOGRAM (Distribution of Finish Times) ---
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Čas_hodiny'], bins=20, kde=True, color='skyblue')
plt.title('Distribúcia cieľových časov (v hodinách)')
plt.xlabel('Čas (hodiny)')
plt.ylabel('Počet bežcov')
plt.savefig('Histogram_Bella.png', bbox_inches='tight')
plt.show()
# --- 2.1 HISTOGRAM (Szekely)
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Čas_hodiny'], bins=20, kde=True, color='skyblue')
plt.title('Distribúcia cieľových časov (v hodinách)')
plt.xlabel('Čas (hodiny)')
plt.ylabel('Počet bežcov')
# Use axvline to draw a vertical line at the person's time
plt.axvline(person_time, color='red', linestyle='--', linewidth=2, label=f'{person_name} ({person_data["Čas"]})')
plt.text(person_time + 0.1, plt.ylim()[1]*0.9, f"Tu je {person_name}", color='red', fontweight='bold')

plt.title(f'Distribúcia časov s vyznačením bežca: {person_name}')
plt.xlabel('Čas (hodiny)')
plt.ylabel('Počet bežcov')
plt.legend()
plt.savefig('histogram_highlighted_Bella.png')

plt.show()



# --- 3. BAR CHART (Runners per Category) ---
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Kategórie', palette='viridis', order=df['Kategórie'].value_counts().index)
plt.title('Počet účastníkov v jednotlivých kategóriách')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Počet')
plt.show()
plt.savefig('Bar_Bella.png', bbox_inches='tight')

# --- 4. BOX PLOT & VIOLIN PLOT (Side by Side Comparison) ---
# This allows for direct visual comparison as requested
fig, axes = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Box Plot
sns.boxplot(ax=axes[0], x='Kategórie', y='Čas_hodiny', data=df_clean, palette='Set3')
axes[0].set_title('Porovnanie časov: Box Plot')
axes[0].set_ylabel('Čas (hodiny)')

# Violin Plot
sns.violinplot(ax=axes[1], x='Kategórie', y='Čas_hodiny', data=df_clean, palette='Set3', inner="quartile")
axes[1].set_title('Porovnanie časov: Violin Plot (Hustota)')
axes[1].set_ylabel('Čas (hodiny)')


plt.xticks(rotation=45, ha='right')
plt.savefig('Comparison_Bella.png', bbox_inches='tight')
plt.tight_layout()
plt.show()