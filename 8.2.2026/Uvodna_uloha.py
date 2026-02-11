import tkinter

# Nastavenie plátna (formát podľa druhého kódu)
platno = tkinter.Canvas(width=600, height=500, bg='white')
platno.pack()

# Otvorenie súboru
w = open('usecky_2.txt', 'r')

for line in w.readlines():
    # Rozdelenie riadku na súradnice
    riadok = line.split()
    if len(riadok) == 4:
        x1 = int(riadok[0])
        y1 = int(riadok[1])
        x2 = int(riadok[2])
        y2 = int(riadok[3])

        # Kreslenie úsečky (šírka 5 podľa prvého kódu)
        platno.create_line(x1, y1, x2, y2, fill='blue', width=5)

        # Kreslenie krúžkov na koncoch (polomer 5)
        r = 5
        platno.create_oval(x1-r, y1-r, x1+r, y1+r, fill='blue', outline='blue')
        platno.create_oval(x2-r, y2-r, x2+r, y2+r, fill='blue', outline='blue')

w.close()
platno.mainloop()
