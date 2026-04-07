import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("filtrovanie_maraton.csv")

# --- HELPER: Convert Time to Minutes for plotting ---
def time_to_minutes(time_str):
    if pd.isna(time_str) or time_str == '---':
        return np.nan
    try:
        h, m, s = map(int, str(time_str).split(':'))
        return h * 60 + m + s / 60
    except:
        return np.nan

df['TotalMinutes'] = df['Čas'].apply(time_to_minutes)

# --- 1. BASIC COUNTS ---
print("1. Koľko bežcov sa zúčastnilo maratónu?", len(df))

nedobehli = (df['Poradie'] == '---').sum()
print("2. Koľkí nedobehli / nedostali miesto?", nedobehli)

print("3. Koľko bežcov bolo z Kene (KEN)?", (df['Nár.'] == 'KEN').sum())
print("4. Koľko bežcov bolo z Českej republiky (CZE)?", (df['Nár.'] == 'CZE').sum())

# --- 2. CATEGORIES ---
kategorie = np.unique(df['Kategórie'].dropna())
print("5. Aké kategórie boli na maratóne:", ", ".join(kategorie))

# --- 3. SPECIFIC PLACEMENTS ---
res_m73 = df[(df['poradie v kategórii'] == 73) & (df['Kategórie'] == 'M hlavná kategória')]["Priezvisko"]
print("6. Kto bol 73. v kategórii M hlavná kategória:", res_m73.item() if not res_m73.empty else "Nenájdený")

res_z73 = df[(df['poradie v kategórii'] == 73) & (df['Kategórie'] == 'Ž hlavná kategória')]["Priezvisko"]
print("7. Kto bol 73. v kategórii Z hlavná kategória:", res_z73.item() if not res_z73.empty else "Nenájdená")

# --- 4. AGE & CLUB SEARCHES ---
z40_49 = df[df['Kategórie'] == 'Z 40-49 rokov']
if not z40_49.empty:
    najstarsia = z40_49.sort_values('Roč.').iloc[0]
    print(f"8. Najstaršia žena v Z 40-49: {najstarsia['Meno']} {najstarsia['Priezvisko']} (Ročník {najstarsia['Roč.']})")

muz_1950 = df[(df['Roč.'] == 1950) & (df['Klub'].notna()) & (df['Klub'] != '---')]
if not muz_1950.empty:
    row = muz_1950.iloc[0]
    print(f"9. Muž narodený 1950 s klubom: {row['Meno']} {row['Priezvisko']} ({row['Klub']})")

print("10. Koľko ľudí sa narodilo v roku 1966?", (df["Roč."] == 1966).sum())

zitny_ostrov = df[df['Klub'] == 'Marathon Club Žitný Ostrov']
if not zitny_ostrov.empty:
    print(f"11. Pani z klubu Žitný Ostrov ({zitny_ostrov.iloc[0]['Priezvisko']}) dobehla v kategórii na: {int(zitny_ostrov.iloc[0]['poradie v kategórii'])}. mieste")


# --- 5. VISUALIZATIONS ---

# Figure 1: Required Charts (Pie, Hist, Bar)
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

df['Nár.'].value_counts().head(5).plot.pie(ax=axes[0], autopct='%1.1f%%', startangle=90)
axes[0].set_title('Top 5 Nationalities')

sns.histplot(df['Roč.'].dropna(), bins=15, ax=axes[1], color='green', kde=True)
axes[1].set_title('Distribution of Birth Years')

df['Kategórie'].value_counts().plot.bar(ax=axes[2], color='orange')
axes[2].set_title('Runners per Category')
plt.tight_layout()
plt.show()

# Figure 2: Box Plot & Violin Plot (Total time in each category)
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='Kategórie', y='TotalMinutes', palette="Set2")
plt.xticks(rotation=45)
plt.title('Box Plot: Time per Category')

plt.subplot(1, 2, 2)
sns.violinplot(data=df, x='Kategórie', y='TotalMinutes', palette="Pastel1")
plt.xticks(rotation=45)
plt.title('Violin Plot: Time per Category')
plt.tight_layout()
plt.show()

# Figure 3: Comparison Diagram (Ondro vs Others)
# Assuming Ondrej is the name to look for
ondro = df[df['Meno'].str.contains('Ondrej', na=False)].iloc[0]
ondro_time = ondro['TotalMinutes']

plt.figure(figsize=(10, 6))
sns.kdeplot(df['TotalMinutes'].dropna(), fill=True, color="gray", label="All Runners")
plt.axvline(ondro_time, color='red', linestyle='--', linewidth=2, label=f"Ondro ({ondro['Priezvisko']})")
plt.annotate('Ondro', xy=(ondro_time, 0.002), xytext=(ondro_time + 50, 0.005),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Comparison: Ondro vs. Rest of the Field')
plt.xlabel('Finish Time (Minutes)')
plt.ylabel('Density')
plt.legend()
plt.show()