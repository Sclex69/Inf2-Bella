import pandas as pd
import numpy as np

w = pd.read_csv("filtrovanie_maraton.csv")

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