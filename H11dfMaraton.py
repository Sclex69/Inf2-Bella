import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
w = pd.read_csv("filtrovanie_maraton.csv")
df = pd.read_csv("filtrovanie_maraton.csv")

print("Koľko bežcov sa zúčastnilo maratónu?", len(w))

# Count runners who didn't finish (have "---" in Place column)
nedobehli = (w['Poradie'] == '---').sum()

print("Koľkí nedobehli / nedostali miesto?", nedobehli)

x=(w['Nár.'] == 'KEN').sum()
print("Koľko bežcov bolo z Kene (KEN)?",x)

y=(w['Nár.'] == 'CZE').sum()
print("Koľko bežcov bolo z Českej republiky (CZE)?",y)


result = w[(w['poradie v kategórii'] == 73) & (w['Kategórie'] == 'M hlavná kategória')]

print("Kto bol 73. v kategórii:  M hlavná kategória",result["Priezvisko"])


g=(w["Roč."] ==1966).sum()
print("Koľko ľudí v zozname sa narodilo v roku 1966?",g)
print(w)



# 2. Helper function to convert HH:MM:SS to total hours
def time_to_hours(t_str):
    try:
        if t_str == '---' or pd.isna(t_str):
            return None
        h, m, s = map(int, t_str.split(':'))
        return h + m/60 + s/3600
    except:
        return None

# 3. Apply conversion and filter out invalid data
df['Čas_hodiny'] = df['Čas'].apply(time_to_hours)
df_plot = df.dropna(subset=['Čas_hodiny', 'Kategórie'])

# 4. Create the Box Plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Kategórie', y='Čas_hodiny', data=df_plot)

# 5. Add labels and formatting
plt.title('Distribution of Finish Times by Category')
plt.ylabel('Time (Hours)')
plt.xlabel('Category')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()



result = df[(df['Priezvisko'] == "SZÉKELY") & (df['Kategórie'] == 'M hlavná kategória')]
print(result["Čas"])



plt.show()