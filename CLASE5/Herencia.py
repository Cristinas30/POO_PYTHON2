class Vehiculo:
    def __init__(self,marca,modelo):#inicializo y le coloco los atributos
        self.marca=marca
        self.modelo= modelo
        
    def descripcion(self):
        return f"El vehiculo es de marca {self.marca},modelo {self.modelo}"
    
#ahora creamos la clase Auto que va a heredar de la clase vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo,puertas):
        super().__init__(marca, modelo)
        self.puertas=puertas
    def descripcion(self):
        return f"El vehiculo es de marca {self.marca} de modelo {self.modelo} tiene {self.puertas} puertas"
    
mi_auto=Auto("chervolet","Sedan",4)
print(mi_auto.descripcion())
        