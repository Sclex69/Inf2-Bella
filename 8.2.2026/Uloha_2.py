import tkinter as tk
import random as rd
import math

# Vytvorenie okna
root = tk.Tk()
root.title("Mestá")
canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack()
x2 = rd.randint(150, 230)
y2 = rd.randint(150, 230)
canvas.create_oval(y2, x2, y2 + 20, x2 + 20, fill='red')
hix = (y2 + y2 + 20) / 2
hiy = (x2 + x2 + 20) / 2
global g
# Funkcia na výpočet vzdialenosti
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
def clear_lines():
    canvas.delete('lines')
def longest_line():
    l={}
    for i, j in positions:
        x=distance(i, j, hix, hiy)
        l[x] = i, j
    for i , j in positions2:
        x=distance(i, j, hix, hiy)
        l[x] = i, j
    max_key = max(l.keys())
    i,j=l.get(max_key)
    canvas.create_line(hix, hiy, i, j,tags="lines")
    number = round(math.sqrt((i - hix) ** 2 + (i - hiy) ** 2))
    canvas.create_text(i+5, j+5, text=number, tags="lines")
def shortest_line():
    l={}
    for i, j in positions:
        x=distance(i, j, hix, hiy)
        l[x] = i, j
    for i , j in positions2:
        x=distance(i, j, hix, hiy)
        l[x] = i, j
    min_key = min(l.keys())
    i,j=l.get(min_key)
    canvas.create_line(hix, hiy, i, j,tags="lines")
    number = round(math.sqrt((i - hix) ** 2 + (i - hiy) ** 2))
    canvas.create_text(i+5, j+5, text=number, tags="lines")


def on_click(event):
    clicked_items = canvas.find_overlapping(event.x - 5, event.y - 5,
                                            event.x + 5, event.y + 5)
    if len(clicked_items) == 0:
        print("Neklikol si na nič")
    else:
        coords = canvas.coords(clicked_items[0])
        i=coords[0]
        j=coords[1]
        canvas.create_line(hix, hiy, i, j, tags="lines")
        number = round(math.sqrt((i - hix) ** 2 + (i - hiy) ** 2))
        canvas.create_text(i + 5, j + 5, text=number, tags="lines")

positions=[]
for i in range(3):
    # Generovanie pozície s kontrolou vzdialenosti
    while True:
        x = rd.randint(0, 480)
        y = rd.randint(0, 480)

        # Kontrola vzdialenosti od červeného bodu (+ 10 pre stred kruhu)
        if distance(x + 7, y + 7, x2 + 10, y2 + 10) >= 40:
            break

    canvas.create_oval(y, x, y + 14, x + 14, fill='blue')
    f = "M" + str(i + 1)
    ix = (y + y+14) / 2
    iy = (x + x+14) / 2
    positions.append([ix, iy])
    canvas.create_text(y - 5, x - 5, text=f,)

positions2 = []
for i in range(5):
    # Generovanie pozície s kontrolou vzdialenosti
    x = rd.randint(0, 480)
    y = rd.randint(0, 480)

    canvas.create_oval(y, x, y + 8, x + 8, fill='green')
    f = "D" + str(i + 1)
    ix = (y + y+8) / 2
    iy = (x + x+8) / 2
    positions2.append([ix, iy])
    canvas.create_text(y - 5, x - 5, text=f,)

for i, j in positions:
    canvas.create_line(hix, hiy, i, j,tags="lines")
    number = round(math.sqrt((i - hix) ** 2 + (i - hiy) ** 2))
    canvas.create_text(i+5, j+5, text=number,tags="lines")
for i, j in positions2:
    canvas.create_line(hix, hiy, i, j,tags="lines")
    number = round(math.sqrt((i - hix) ** 2 + (i - hiy) ** 2))
    canvas.create_text(i+5, j+5, text=number, tags="lines")



button_frame = tk.Frame(root)
button_frame.pack()




btn_clear = tk.Button(button_frame, text="Vymazať úsečky", command=clear_lines)
btn_clear.pack(side=tk.LEFT, padx=5, pady=5)
btn_min = tk.Button(button_frame, text="nakratsia", command=shortest_line)
btn_min.pack(side=tk.LEFT, padx=5, pady=5)
btn_max = tk.Button(button_frame, text="najdlhsia", command=longest_line)
btn_max.pack(side=tk.LEFT, padx=5, pady=5)
canvas.bind('<Button-1>', on_click)
root.mainloop()