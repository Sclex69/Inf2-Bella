import tkinter as tk
import random as rd
import math

# Vytvorenie okna
root = tk.Tk()
root.title("Mapa")
canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack()


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

def middle(x1, y1, x2, y2):
    return round((x1 + x2) / 2), round((y1+y2)/2)
def hadik():
    for i in range (len(positions2)-1):
        x = positions2[i][0]
        y = positions2[i][1]
        x2 = positions2[i+1][0]
        y2 = positions2[i+1][1]
        canvas.create_line(x,y,x2,y2,fill='white')
        l=distance(x,y,x2,y2)
        c=middle(x,y,x2,y2)
        x=c[0]
        y=c[1]
        canvas.create_text(x, y, text=l, fill="white")






positions2 = []
for i in range(10):
    # Generovanie pozície s kontrolou vzdialenosti
    x = rd.randint(0, 480)
    y = rd.randint(0, 480)

    canvas.create_oval(y, x, y + 8, x + 8, fill='blue')
    f = "D" + str(i + 1)
    ix = (y + y+8) / 2
    iy = (x + x+8) / 2
    positions2.append([ix, iy])
    canvas.create_text(y - 5, x - 5, text=f,)

distances=[]
for i,j in positions2:
    c=rd.randint(2,4)
    c=rd.randint(0,c)
    c = rd.randint(0, c)
    for l in range(c):
        x=positions2[c]
        y=x[1]
        x=x[0]
        canvas.create_line(i, j, x, y, fill="white")
        l=distance(x,y,i,j)
        t=middle(x,y,i,j)
        x=t[0]
        y=t[1]
        canvas.create_text(x, y, text=l, fill="white")


hadik()
rd.shuffle(positions2)




root.mainloop()