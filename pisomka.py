import tkinter as tk
win = tk.Tk()
win.title("Moje prve okno")

canvas = tk.Canvas(win, width=400, height=400, bg = "white")
canvas.pack()

#ciary
for i in range (0,201,20):
    canvas.create_line(0, 200, 0+i,0, fill = "lightblue", width = 2)
    canvas.create_line(200, 200, 200-i,0, fill = "lightblue", width = 2)

#kocky
for i in range (0,201,20):
        x = 0
        while x < 200:
            canvas.create_rectangle(x, 200+i , x+20 ,220+i, outline= "lightblue", width = 2)
            x += 20

#kruznice
for i in range (0,201,20):
    canvas.create_oval(200+i, 0+i, 400-i,200-i,  outline= "lightblue", width = 2)

#schody
for i in range (0,201,20):
    canvas.create_rectangle(200+i, 200+i, 220+i, 220+i, fill = "lightblue")
    canvas.create_rectangle(400-i, 200+i, 380-i, 220+i, fill = "hotpink")
win.mainloop()