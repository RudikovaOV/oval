from tkinter import *


main = Tk()
main.geometry("1000x500")
canvas = Canvas(main, width=1000, height=500, bg= 'black')
canvas.pack()

#rect = canvas.create_rectangle(200,100, 500, 500, fill="#34b1eb", width="4")
#rect = canvas.create_rectangle(400,400, 500, 500, fill="brown", width="4")
#triangle = canvas.create_polygon(150, 400, 150, 250, 300,100, 750,100, 850, 250, 850, 400, fill="#34eb5e")
oval = canvas.create_oval(400, 200, 500, 300, width='4', fill="#ebe834" )
oval1 = canvas.create_oval(200,200, 400, 300, width='4', fill="#dfe8e3" )
oval2 = canvas.create_oval(400,300, 500, 500, width='4', fill="#dfe8e3" )
oval3 = canvas.create_oval(400,0, 500, 200, width='4', fill="#dfe8e3" )
oval4 = canvas.create_oval(500,200, 700, 300, width='4', fill="#dfe8e3" )
oval5 = canvas.create_oval(200,0, 450, 250, width='4', fill="#dfe8e3" )
#line1 = canvas.create_line(200, 300, 300, 150, fill='green', width='5')

#line1 = canvas.create_line(0, 0, 200, 200, fill='green', width='5')
#oval = canvas.create_oval(100, 100, 200, 220, width='4', fill="#39C0A9" )
#rect = canvas.create_rectangle(200,150, 250, 180, fill="red", width="4")
#triangle = canvas.create_polygon(100, 10, 20, 90, 180, 90)
#triangle1 = canvas.create_polygon(100, 10, 20, 90, 180, 90, 120, 60, 300, 50)

main.mainloop()
