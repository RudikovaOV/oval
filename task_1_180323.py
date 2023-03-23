import random
from tkinter import *
from tkmacosx import *
from random import *
speed = 10

colors = ['white', 'black', 'gray', 'brown', 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'navy', 'magenta', 'purple', 'violet', 'pink']

color_oval = "#c91a8c"
def up():
    current_coords = canvas.coords(oval) # получили текущие координаты овала
    if current_coords[1] - speed > 0:
        current_coords[1] = current_coords[1] - speed # изменили
        current_coords[3] = current_coords[3] - speed # изменили
        canvas.coords(oval, current_coords) # обновили текущие координаты овала

def down():
    current_coords = canvas.coords(oval) # получили текущие координаты овала
    if current_coords[3] + speed <500:
        current_coords[1] = current_coords[1] + speed # изменили
        current_coords[3] = current_coords[3] + speed # изменили
        canvas.coords(oval, current_coords) # обновили текущие координаты овала

def left():
    current_coords = canvas.coords(oval) # получили текущие координаты овала
    if current_coords[0] - speed > 90:
        current_coords[0] = current_coords[0] -speed # изменили
        current_coords[2] = current_coords[2] - speed # изменили
        canvas.coords(oval, current_coords) # обновили текущие координаты овала


def right():
    current_coords = canvas.coords(oval) # получили текущие координаты овала
    if current_coords[2] + speed < 500:
        current_coords[0] = current_coords[0] + speed # изменили
        current_coords[2] = current_coords[2] + speed # изменили
        canvas.coords(oval, current_coords) # обновили текущие координаты овала

def size():
    current_coords = canvas.coords(oval) # получили текущие координаты овала
    if current_coords[0] - speed > 90 and current_coords[1] + speed > 0:
        current_coords[0] = current_coords[0] - speed  # изменили
        current_coords[1] = current_coords[1] - speed
        current_coords[2] = current_coords[2] + speed
        current_coords[3] = current_coords[3] + speed  # изменили
        canvas.coords(oval, current_coords) # обновили текущие координаты овала

def color():
    canvas.itemconfig(oval, fill=choice(colors))


main_window = Tk()
main_window.geometry("500x500")
canvas = Canvas(main_window, width=500, height=500)
canvas.pack()
btn_up = Button(text="UP", command = up)
btn_up.place(x=30,y=20)

btn_down = Button(text="DOWN", command = down)
btn_down.place(x=20, y=100)
btn_color = Button(text="COLOR", command = color)
btn_color.place(x=20, y=150)
btn_size = Button(text="SIZE", command = size)
btn_size.place(x=20, y=200)
btn_left = Button(text="LEFT", command = left)
btn_left.place(x=0, y=60)
btn_right = Button(text="RIGHT", command = right)
btn_right.place(x=90, y=60)

oval = canvas.create_oval(200, 30,  300, 150, width='4', fill = color_oval)

main_window.mainloop()