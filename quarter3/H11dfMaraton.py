import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("filtrovanie_maraton.csv")

# --- 1. BASIC COUNTS ---
print("1. Koľko bežcov sa zúčastnilo maratónu?", len(df))

nedobehli = (df['Poradie'] == '---').sum()
print("2. Koľkí nedobehli / nedostali miesto?", nedobehli)

print("3. Koľko bežcov bolo z Kene (KEN)?", (df['Nár.'] == 'KEN').sum())
print("4. Koľko bežcov bolo z Českej republiky (CZE)?", (df['Nár.'] == 'CZE').sum())

# --- 2. CATEGORIES (Using np.unique) ---
kategorie = np.unique(df['Kategórie'].dropna())
print("5. Aké kategórie boli na maratóne:", ", ".join(kategorie))

# --- 3. SPECIFIC PLACEMENTS ---
# 73rd in Men's Main
res_m73 = df[(df['poradie v kategórii'] == 73) & (df['Kategórie'] == 'M hlavná kategória')]["Priezvisko"]
print("6. Kto bol 73. v kategórii M hlavná kategória:", res_m73.item() if not res_m73.empty else "Nenájdený")

# 73rd in Women's Main
res_z73 = df[(df['poradie v kategórii'] == 73) & (df['Kategórie'] == 'Ž hlavná kategória')]["Priezvisko"]
print("7. Kto bol 73. v kategórii Z hlavná kategória:", res_z73.item() if not res_z73.empty else "Nenájdená")

# --- 4. AGE & CLUB SEARCHES ---
# Oldest woman in Z 40-49 (Smallest birth year)
z40_49 = df[df['Kategórie'] == 'Z 40-49 rokov']
if not z40_49.empty:
    najstarsia = z40_49.sort_values('Roč.').iloc[0]
    print(f"8. Najstaršia žena v Z 40-49: {najstarsia['Meno']} {najstarsia['Priezvisko']} (Ročník {najstarsia['Roč.']})")

# Man born 1950 with a club
muz_1950 = df[(df['Roč.'] == 1950) & (df['Klub'].notna()) & (df['Klub'] != '---')]
if not muz_1950.empty:
    row = muz_1950.iloc[0]
    print(f"9. Muž narodený 1950 s klubom: {row['Meno']} {row['Priezvisko']} ({row['Klub']})")

print("10. Koľko ľudí sa narodilo v roku 1966?", (df["Roč."] == 1966).sum())

# Marathon Club Žitný Ostrov
zitny_ostrov = df[df['Klub'] == 'Marathon Club Žitný Ostrov']
if not zitny_ostrov.empty:
    # We take the first person found from that club
    print(f"11. Pani z klubu Žitný Ostrov ({zitny_ostrov.iloc[0]['Priezvisko']}) dobehla v kategórii na: {int(zitny_ostrov.iloc[0]['poradie v kategórii'])}. mieste")


# --- 5. EXERCISES: BASIC CHARTS ---
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Pie Chart: Nationalities (Top 5)
df['Nár.'].value_counts().head(5).plot.pie(ax=axes[0], autopct='%1.1f%%', startangle=90)
axes[0].set_title('Meaningful Pie Chart: Top 5 Nationalities')
axes[0].set_ylabel('')

# Histogram: Birth Years
sns.histplot(df['Roč.'].dropna(), bins=15, ax=axes[1], color='green', kde=True)
axes[1].set_title('Histogram: Distribution of Birth Years')
axes[1].set_xlabel('Year of Birth')

# Bar Plot: Categories
df['Kategórie'].value_counts().plot.bar(ax=axes[2], color='orange')
axes[2].set_title('Bar Plot: Runners per Category')
axes[2].set_xlabel('Category')
axes[2].set_ylabel('Number of Runners')

plt.tight_layout()
plt.show()