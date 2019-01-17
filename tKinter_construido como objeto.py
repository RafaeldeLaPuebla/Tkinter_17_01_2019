#Vamos a ver cómo funciona tkinter

from tkinter import * #impórtame todo
from tkinter import ttk

class mainApp(Tk): #mainApp, hereda de Tk.
    size = "1024x768"
    
    def __init__(self):
        Tk.__init__(self) #hereda la instancia. He conseguido que no sea una pantalla con objetos dentro, sino que sea       
#        self.root = Tk() #creo un objeto de tipo tkinter, que es una ventana
        self.geometry(self.size) #ahora self se refiere a tk, ya no hace falta poner self.root.geometry
        self.title("Mi ventana")
        self.configure(bg = "blue")
    
    def start(self):
        self.root.mainloop()

#empieza a funcionar, por favor:
if __name__ == '__main__':
    app = mainApp()
    app.start()
    
