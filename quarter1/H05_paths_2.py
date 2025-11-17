import os
from datetime import datetime, timedelta
import random

# 1. Priečinok data
if not os.path.exists("data"):
    os.makedirs("data")
dates_folder = "data/dates"

#checks if the folder (directory) specified by dates_folder exists
if not os.path.exists(dates_folder):
    os.makedirs(dates_folder)


# 3. Funkcia pre hod kockou
def hod_kockou():
    return random.randint(1, 6)


# 4. Vytvorenie 10 súborov s dátumami
dnes = datetime.today()

for i in range(10):
    datum = dnes + timedelta(days=i)
    nazov_suboru = datum.strftime("%Y-%m-%d") + ".txt"
    cesta = os.path.join(dates_folder, nazov_suboru)

    with open(cesta, "w") as f:
        for _ in range(10):
            f.write(str(hod_kockou()) + "\n")

# 5. Súbor s aktuálnym časom
current_time_path = "data/current_time.txt"
with open(current_time_path, "w") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
