import tkinter as tk
win = tk.Tk()
win.title("Moje prve okno")

canvas = tk.Canvas(win, width=800, height=800, bg = "peachpuff")
canvas.pack()
counter = 0

def click():
    global counter
    print(f"akcia {counter}")
    counter += 1
    farba = canvas.itemcget(obj2, "fill")
    farba2 = canvas.itemcget(obj3, "fill")
    print (farba)
    print (farba2)

    if farba == "lightblue":
        canvas.itemconfig(obj2, fill = "lightpink", outline = "lightpink")
    else:
        canvas.itemconfig(obj2, fill = "lightblue", outline = "lightblue")
    if farba2 == "peachpuff":
        canvas.itemconfig(obj3, fill = "lightyellow", outline = "lightyellow")
    else:
        canvas.itemconfig(obj3, fill = "peachpuff", outline = "peachpuff")

button = tk.Button(win, text="click me", bg="hotpink", width = 100, height=5, command=click)
button.pack()

obj1 = canvas.create_line(0, 0, 800, 800, fill = "lightblue", width = 5)
obj2 = canvas.create_rectangle(100,100,700,700, fill = "lightblue", outline = "lightblue")
obj3 = canvas.create_oval(200,200,600,600, fill = "peachpuff", outline = "peachpuff")

win.mainloop()