from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt = "" #voy a ir apuntando el valor justo antes de que el usuario teclee un nuevo valor.
    
    def __init__(self): #las cualidades de mi ventana.
        Tk.__init__(self) #hereda la instancia.
        self.title("Termómetro")
        self.geometry("210x150")
        self.configure(bg="#ECECEC")
        self.resizable(0,0) #para evitar la redimensión del cuadro por el usuario.
    
#vamos a utizar variables de control, que tiene tkinter. Deja en Slack un enlace a variables de control de tkinter
        self.temperatura = StringVar(value="")#Me inicializas temperatura a cero. temperatura es una instancia de StringVar
        self.temperatura.trace("w", self.validateTemperature) #utilizamos el método trace de temperatura (de StringVar), que va a servir para validar. w deja escribir.
        self.tipoUnidad = StringVar(value="C")  #Me inicializas tipoUnidad a "C".
    
        self.createLayout()

    
    def createLayout(self): #lo que voy a poner en mi ventana.
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10) #variable es una variable de control.
        
        self.lbUnidad = ttk.Label(self, text="Grados:").place(x=10, y=50) #etiqueta "Grados"
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20, y=70)#creamos un radio button. Cuando hago clic, la variable asociada es tipoUnidad y el valor que debe meter es F.
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20, y=95)#creamos otro radio button. Cuando hago clic, la variable asociada es tipoUnidad y el valor que debe meter es C.
        #con command=selected, le digo que llame a esta función, selected, programación con funciones de nivel superior.
        
    def start(self):
        self.mainloop()
    #Esquema que es habitual cuando quiero comprobar una cosa. Guardo el valor anterior.    
    def validateTemperature(self, *args):#es una restricción que nos impone trace. Es una restricción de la programación funcional. Trace está mandando parámetros. Los parámetros con asterisco son una lista que pueden permanecer vacío. 
        nuevoValor = self.temperatura.get() #guardo en esta variable el valor metido, con un método get.
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnt)
            
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())
        
        if toUnidad == 'F': #si voy a convertir a F
            resultado = grados * 9/5 +32
        elif toUnidad == 'C':
            resultado = (grados - 32) *5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)
        
     
        
if __name__ == '__main__':
    app = mainApp()
    app.start()
    