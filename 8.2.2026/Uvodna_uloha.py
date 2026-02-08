import tkinter as tk

# Načítanie súboru
file_path = 'usecky_2.txt'

# Načítanie úsečiek zo súboru
usecky = []
with open(file_path, 'r') as f:
    for line in f:
        coords = list(map(int, line.strip().split()))
        if len(coords) == 4:
            usecky.append(coords)

# Vytvorenie okna
root = tk.Tk()
root.title("Dešifrovanie správy z úsečiek")

# Nájdenie rozsahu súradníc pre správne nastavenie veľkosti plátna
all_coords = []
for x1, y1, x2, y2 in usecky:
    all_coords.extend([x1, x2])
    all_coords.extend([y1, y2])

min_x = min(all_coords[::2]) if all_coords else 0
max_x = max(all_coords[::2]) if all_coords else 500
min_y = min(all_coords[1::2]) if all_coords else 0
max_y = max(all_coords[1::2]) if all_coords else 500

# Pridanie okrajov
padding = 20
canvas_width = max_x - min_x + 2 * padding
canvas_height = max_y - min_y + 2 * padding

# Vytvorenie plátna
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Kreslenie úsečiek
for x1, y1, x2, y2 in usecky:
    # Posun súradníc kvôli okrajom
    x1_shifted = x1 - min_x + padding
    y1_shifted = y1 - min_y + padding
    x2_shifted = x2 - min_x + padding
    y2_shifted = y2 - min_y + padding

    # Nakreslenie čiary (5 px široká)
    canvas.create_line(x1_shifted, y1_shifted, x2_shifted, y2_shifted,
                       fill='blue', width=5)

    # Nakreslenie modrých krúžkov na koncoch (priemer 10 = polomer 5)
    radius = 5

    # Krúžok na začiatku
    canvas.create_oval(x1_shifted - radius, y1_shifted - radius,
                       x1_shifted + radius, y1_shifted + radius,
                       fill='blue', outline='blue')

    # Krúžok na konci
    canvas.create_oval(x2_shifted - radius, y2_shifted - radius,
                       x2_shifted + radius, y2_shifted + radius,
                       fill='blue', outline='blue')

root.mainloop()