import random
import string



# Vytvorte funkciu, ktora simuluje hod kockou. 10 simulujte hod kockou (zavolajte funkciu)
# a zapíšte výsledok do zoznamu (listu).

def hod_kockou():
    """Vráti náhodné číslo od 1 do 6 ako hod kockou.

    Returns:
        int: Náhodný výsledok hodu kockou.
    """
    return random.randint(1, 6)

# 10 hodov kockou – list comprehension
vysledky = [hod_kockou() for _ in range(10)]
print("Výsledky 10 hodov:", vysledky)



# Vytvorte generator hesiel tak, aby dĺžku hesla vedel nastaviť užívateľ.

def generator_hesla(dlzka):
    """Vytvorí náhodné heslo danej dĺžky.

    Args:
        dlzka (int): Dĺžka generovaného hesla.

    Returns:
        str: Náhodne vygenerované heslo.
    """
    znaky = string.ascii_letters + string.digits + string.punctuation
    heslo = ''.join(random.choice(znaky) for _ in range(dlzka))
    return heslo

dlzka = int(input("Zadaj dĺžku hesla: "))
print("Vygenerované heslo:", generator_hesla(dlzka))





def random_gen_pismen(dlzka):
    """Vytvorí náhodný reťazec písmen danej dĺžky.

    Args:
        dlzka (int): Počet písmen v stringu.

    Returns:
        str: Náhodne vygenerovaný reťazec.
    """
    letters = string.ascii_letters
    final = ''.join(random.choice(letters) for i in range(dlzka))
    return final

dlzka = int(input("Zadaj dĺžku hesla: "))
print("Vygenerované heslo:", random_gen_pismen(dlzka))



# Funkcia, ktorá vráti zoznam stringov
def zoznam_stringov(pocet, dlzka_stringu):
    """Vytvorí zoznam náhodných stringov.

    Args:
        pocet (int): Počet stringov v zozname.
        dlzka_stringu (int): Dĺžka každého stringu.

    Returns:
        list: Zoznam náhodne vygenerovaných stringov.
    """
    vysledok = []
    for i in range(pocet):
        vysledok.append(random_gen_pismen(dlzka_stringu))
    return vysledok



# Funkcia, ktorá prenásobí každý prvok listu náhodným číslom (1–5)
def nasob_list_nahodnym_cislom(zoznam):
    """Prenásobí každý string v zozname náhodným číslom 1–5 (opakovanie stringu).

    Args:
        zoznam (list): Zoznam stringov.

    Returns:
        list: Nový zoznam so stringmi opakovanými 1–5 krát.
    """
    novy_zoznam = []
    for prvok in zoznam:
        nahodne_cislo = random.randint(1, 5)
        novy_zoznam.append(prvok * nahodne_cislo)  # string * číslo → opakovanie
    return novy_zoznam



# Funkcia na výpis počtu znakov v každom stringu
def vypis_dlzky_stringov(zoznam):
    """Vypíše dĺžku každého stringu v zozname.

    Args:
        zoznam (list): Zoznam stringov.

    Returns:
        None
    """
    for i, s in enumerate(zoznam):
        print(f"String {i+1}: '{s}' má {len(s)} znakov")

# Užívateľské vstupy
dlzka = int(input("Zadaj dĺžku jedného stringu: "))
pocet = int(input("Zadaj počet stringov v zozname: "))

# Generovanie pôvodného zoznamu
povodny = zoznam_stringov(pocet, dlzka)
print("Pôvodný zoznam:")
print(povodny)

# Násobenie stringov náhodnými číslami
vynasobeny = nasob_list_nahodnym_cislom(povodny)
print("Zoznam po prenásobení:")
print(vynasobeny)

# Výpis dĺžok
print("Dĺžky stringov v novom zozname:")
vypis_dlzky_stringov(vynasobeny)



# --------------------------------------------------------------------
# 2. ÚLOHA – GENEROVANIE SLOV A ŠTATISTIKA DĹŽOK
# --------------------------------------------------------------------


# Funkcia na generovanie náhodneho slova z malých písmen
def random_slovo(dlzka):
    """Vygeneruje náhodné slovo z malých písmen.

    Args:
        dlzka (int): Dĺžka slova.

    Returns:
        str: Náhodné slovo.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(dlzka))



# Funkcia na vytvorenie zoznamu náhodných slov
def vytvor_zoznam_slov(pocet):
    """Vytvorí zoznam náhodných slov dĺžky 3–7.

    Args:
        pocet (int): Počet generovaných slov.

    Returns:
        list: Zoznam náhodných slov.
    """
    zoznam = []
    for _ in range(pocet):
        dlzka = random.randint(3, 7)  # náhodná dĺžka slova
        zoznam.append(random_slovo(dlzka))
    return zoznam



# Funkcia na spočítanie počtu slov podľa dĺžok 3–7
def spocitaj_dlzky(zoznam):
    """Spočíta počet slov podľa ich dĺžky (3–7).

    Args:
        zoznam (list): Zoznam slov.

    Returns:
        dict: Počet slov s dĺžkou 3–7.
    """
    pocty = {3: 0, 4: 0, 5: 0, 6: 0, 7: 0}  # vhodná štruktúra = slovník
    for slovo in zoznam:
        pocty[len(slovo)] += 1
    return pocty



# Generovanie slov
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
