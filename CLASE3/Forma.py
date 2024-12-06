from abc import ABC, abstractmethod ## importa la clase abstracta es la base del polimorfismo y solo la utilizamos si se utilizan enlas subclases 
                     ## y si agrego adicionales solo serian en las subclases 
                     ## en una interfaz no exiten constructores solo metodos

class Forma(ABC):# AQUI SIEMPRE SE DEBE LLAMAR A LA CLASE ABSTRACTA y solo esta seria la clase abstracta porque tiene los decoradores
    @abstractmethod  # ESTE ES MI DECORADOR ABSTRACT 
    def __init__(self) :
        pass
    
    @ abstractmethod
    
    def area(self):
        pass
    
class Circulo(Forma):## las clases siempre inician en en Mayuscula
    def __init__(self,radio):
        self.radio= radio
        
    def area(self): ## los metodos o comportamientos siempre en minucula
        return f"El area de un circulo es {3.14 * self.radio ** 2}" ## aqui coloco la formula del area
    
    def perimetro(self):
        return f"El perimetro de un circulo es {2* 3.14 * self.radio}"  # estwe comportamieto es unico para los circulos y no se declara 
    
class Rectangulo(Forma):
    def __init__(self,base,altura):
        
        self.base = base
        self.altura = altura
        
    def area(self): ## self utilizo metodos de instancia
        return f"El area  de un rectangulo es : {self.base *self.altura}"
    ## este perimetro no esta como abstracto porque es propio de esta subclase
    def perimetro(self): ## son metodos muy especificos del rectangulo por eso no esta como abstracta
        return f"El perimetro del rectangulo es: {2 * (self.base + self.altura)}"
    
class Cuadrado(Forma): 
    def __init__(self,lado):
        self.lado=lado
        
    def area(self):
        return f"El area del cuadrado es {self.lado**2}"
    
    ## creo el objeto para que aparezca en pantalla

formas = [Circulo(5),
         Rectangulo(2,10),
         Cuadrado(8),
         Rectangulo(10,20),
         Circulo(22)
         
    
]

## ahora imprimo

print ("Area de las formas")

for forma in formas:
    print (forma.area())
    
## para acceder de una clase que no esta como abstracta se debe crear un objeto e imprimir el metodo correspondiente
## por ejemplo el perimetro de circulo se debe crear un objeto circulo1

circulo1 = Circulo(5)## creamos el objeto y le pasamos el parametro
rectangulo1 = Rectangulo(2,10)

print (circulo1.perimetro())
print (rectangulo1.perimetro())
    
             
        
    
        