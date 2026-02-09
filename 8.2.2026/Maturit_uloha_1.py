import tkinter as tk


root = tk.Tk()
root.title("spajanie bodov")
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

c=1
first_point=[]
def on_click_l(event):
    global first_point
    global c
    point = [round(event.x), round(event.y)]
    first_point.append(point)
    # Nakreslíme krúžok
    radius = 3
    canvas.create_oval(event.x - radius, event.y - radius,
                       event.x + radius, event.y + radius,
                       fill='black')
    canvas.create_text(event.x+5, event.y+5, text=c, fill="black", font=('Aerial 11'))
    c=c+1


def on_click_r(event):
    for i in range (c-2):
        x = first_point[i][0]
        y = first_point[i][1]
        x2 = first_point[i+1][0]
        y2 = first_point[i+1][1]
        canvas.create_line(x,y,x2,y2,fill='black')



# Naviazanie funkcie na kliknutie myšou
canvas.bind('<Button-1>', on_click_l)
canvas.bind('<Button-3>', on_click_r)




root.mainloop()