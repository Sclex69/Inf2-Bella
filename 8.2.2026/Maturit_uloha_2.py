import tkinter as tk

root = tk.Tk()
root.title("Kreslenie")
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

def house(x,y):
    canvas.create_rectangle(x,y+40,x+50,y+90,fill='cyan',outline= 'cyan')
    canvas.create_polygon(x,y+40,x+50,y+40,x+25,y,fill='red',outline= 'red')


def moon(x,y):
    canvas.create_oval(x, y, x+80, y+80, fill='yellow', outline='')


    canvas.create_oval(x+30, y, x+110, y+80, fill='white', outline='')
g=0
for x in range(20,600,150):
    for y in range(20,600,150):
            if (g%2)==0:
                house(x, y)
            else:
                moon(x, y)
            g = g + 1
    g = g + 1


root.mainloop()