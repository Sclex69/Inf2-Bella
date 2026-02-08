import tkinter as tk
import math

# Vytvorenie okna
root = tk.Tk()
root.title("Kreslenie")
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()
subor = open('udaje.txt', 'w')  # w  =  write  –  vymazanie  a  naplnenie  obsahom    odznova
subor.close()


def on_click_l(event):
    global first_point
    first_point = (round(event.x), round(event.y))
    # Nakreslíme krúžok
    radius = 5
    canvas.create_oval(event.x - radius, event.y - radius,
                       event.x + radius, event.y + radius,
                       fill='green')


def on_click_r(event):
    second_point = (round(event.x), round(event.y))
    # Nakreslíme krúžok
    radius = 5
    canvas.create_oval(event.x - radius, event.y - radius,
                       event.x + radius, event.y + radius,
                       fill='red')
    x1 = first_point[0]
    y1 = first_point[1]
    x2 = second_point[0]
    y2 = second_point[1]
    canvas.create_line(x1, y1, x2, y2)
    number = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    ix = (x2 + x1) / 2
    iy = (y2 + y1) / 2
    canvas.create_text(ix, iy, text=number, fill="black", font=('Aerial 11'))

    # Zápis do súboru
    subor = open('udaje.txt', 'a')
    subor.write(f"{x1} {y1} {x2} {y2}\n")
    subor.close()


# Naviazanie funkcie na kliknutie myšou
canvas.bind('<Button-1>', on_click_l)
canvas.bind('<Button-3>', on_click_r)
root.mainloop()