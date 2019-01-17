#Vamos a ver cómo funciona tkinter

from tkinter import * #impórtame todo
from tkinter import ttk

root = Tk() #creo un objeto de tipo tkinter, que es una ventana

root.geometry("640x480") #geometry es un método propio de tkinter
root.title("Mi ventana")
root.configure(bg = "blue")

#empieza a funcionar, por favor:
root.mainloop()
