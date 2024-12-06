
## IMPLEMENTANDO HERENCIA Y POLIMORFISMO DE LA CLASE MADRE DE aNIMAL EN SUNCLASES DE PERRO Y GATO APLICAMOS HERENCIA Y POLIMOFIRMO Y CAMBIAMOS EL COMPORTAMIENTO DEL METODO HABLAR
class Animal:
    # es importante crear siempre los metodos para saber los comportamientos que tiene esa clase 
    
    def __init__(self):
        pass
    
    def hablar(self):# este metodo se define en la clase madre Animal  y se aplica el polimorfismo en perro y gato porque en cada subclase hace otra cosas diferentes
        pass
class Perro (Animal):## perro viene de animal como herencia
    
    def __init__(self):
      ##  super().__init__()
        pass
      
    def hablar(self): # siempre el los metodos ()
          return f"el perro hace guau guau"
      
      
class Gato(Animal):
    def __init__(self):
        pass
    
    def hablar(self):
        return f"El gato hace miaw"
    
    ## creo el  objeto Y LE ENVIO UN METODO VACIO
    
animales = [Perro(),
              Gato(),
              Perro(),
              Gato()
]

## hago un ciclo for para que recorra las listas PERRO Y GATO

for animal in animales:
    print(animal.hablar()) ## imprimo lo que hay en animal y llMO EL METODO HABLAR
        
    
      
      
    
    