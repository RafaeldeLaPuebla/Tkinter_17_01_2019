class Objeto():
    __atributoPrivado = None
    atributoPublico = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPublico = "me lo ha pedido Jorge"
    
    def getAtributoPrivado(self): #Es un getter.
        return self.__atributoPrivado
    
    def setAtributoPrivado(self, valor): #Es un setter.
        self.__atributoPrivado = valor
 
 #Podemos juntar el getter y el setter en una estructura sola, de forma más elegante y con un solo método:  
    def atributoPrivado(self, valor = None):
        if valor == None:
            return self.__atributoPrivado
        else:
            self.__atributoPrivado = valor
    
    
        