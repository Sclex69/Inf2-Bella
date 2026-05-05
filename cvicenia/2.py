import tkinter as tk
steps=50
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
def start():
    for i in range(0,800,100):
        for x in range(0, 600, steps):
            if( i/steps + x/ steps) % 2 == 0:
                color1= "white"
                color2= "black"
            else:
                color1= "black"
                color2= "white"
            canvas.create_rectangle(i, x, i + steps, x + steps, fill=color1)
            canvas.create_rectangle(i + steps, x, i + (steps * 2), x + steps, fill=color2)

def dot(event):
    x, y = round(event.x/steps), round(event.y/steps)
    x=x*steps
    y=y*steps
    canvas.create_oval(x - 2, y - 2, x +2, y + 2, fill="red")


def clear():
    canvas.delete(tk.ALL)
    start()
start()
button = tk.Button(root, text="reset", command= clear)
button.pack()
canvas.bind("<Button-1>", dot)
root.mainloop()
