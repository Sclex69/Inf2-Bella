import random
import string



#Vytvorte funkciu, ktora simuluje hod kockou. 10 simulujte hod kockou (zavolajte funkciu) a zapíšte výsledok do zoznamu (listu).

def hod_kockou():
    """Vráti náhodné číslo od 1 do 6 ako hod kockou."""
    return random.randint(1, 6)

# 10 hodov kockou
vysledky = [hod_kockou() for _ in range(10)]

print("Výsledky 10 hodov:", vysledky)

#Vytvorte generator hesiel tak, aby dĺžku hesla vedel nastaviť užívateľ.

def generator_hesla(dlzka):
    """Vytvorí náhodné heslo danej dĺžky."""
    znaky = string.ascii_letters + string.digits + string.punctuation
    heslo = ''.join(random.choice(znaky) for _ in range(dlzka))
    return heslo

dlzka = int(input("Zadaj dĺžku hesla: "))
print("Vygenerované heslo:", generator_hesla(dlzka))











def random_gen_pismen(dlzka):
    letters = string.ascii_letters
    final = ''.join(random.choice(letters) for i in range(dlzka))
    return final

dlzka = int(input("Zadaj dĺžku hesla: "))
print("Vygenerované heslo:", random_gen_pismen(dlzka))




# Funkcia, ktorá vráti zoznam stringov
def zoznam_stringov(pocet, dlzka_stringu):
    vysledok = []
    for i in range(pocet):
        vysledok.append(random_gen_pismen(dlzka_stringu))
    return vysledok




# Funkcia, ktorá prenásobí každý prvok listu náhodným číslom (1–5)
def nasob_list_nahodnym_cislom(zoznam):
    novy_zoznam = []
    for prvok in zoznam:
        nahodne_cislo = random.randint(1, 5)
        novy_zoznam.append(prvok * nahodne_cislo)   # string * číslo → opakovanie
    return novy_zoznam

# Funkcia na výpis počtu znakov v každom stringu
def vypis_dlzky_stringov(zoznam):
    for i, s in enumerate(zoznam):
        print(f"String {i+1}: '{s}' má {len(s)} znakov")

dlzka = int(input("Zadaj dĺžku jedného stringu: "))
pocet = int(input("Zadaj počet stringov v zozname: "))

povodny = zoznam_stringov(pocet, dlzka)
print("Pôvodný zoznam:")
print(povodny)

vynasobeny = nasob_list_nahodnym_cislom(povodny)
print("Zoznam po prenásobení:")
print(vynasobeny)

print("Dĺžky stringov v novom zozname:")
vypis_dlzky_stringov(vynasobeny)


#2 uloha



# Funkcia na generovanie náhodneho slova z malých písmen
def random_slovo(dlzka):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(dlzka))

# Funkcia na vytvorenie zoznamu náhodných slov
def vytvor_zoznam_slov(pocet):
    zoznam = []
    for _ in range(pocet):
        dlzka = random.randint(3, 7)  # náhodná dĺžka slova
        zoznam.append(random_slovo(dlzka))
    return zoznam

# Funkcia na spočítanie počtu slov podľa dĺžok 3–7
def spocitaj_dlzky(zoznam):
    pocty = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0}  # vhodná štruktúra = slovník
    for slovo in zoznam:
        pocty[len(slovo)] += 1
    return pocty



slova = vytvor_zoznam_slov(30)

print("Pôvodný zoznam slov:")
print(slova)

# Spočítanie dĺžok
pocty = spocitaj_dlzky(slova)
print("Počty slov podľa dĺžky:")
for dlzka, pocet in pocty.items():
    print(f"Dĺžka {dlzka}: {pocet} slov")

# Zoradenie podľa abecedy
zoradene_abecedne = sorted(slova)
print("Zoradené podľa abecedy:")
print(zoradene_abecedne)

# Zoradenie podľa dĺžky
zoradene_dlzka = sorted(slova, key=len)
print("Zoradené podľa dĺžky:")
print(zoradene_dlzka)
