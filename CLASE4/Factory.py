from abc import ABC, abstractmethod

# clase abstracta

class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass
    
    #creacion de subclases
    
    #con el polimorfismo le cambio la didactica a los metodos
class  ClaseA(Clases):
    def operacion(self):
        return "Esta es la clase A"
    
class  ClaseB(Clases):
    def operacion(self):
        return "Esta es la clase B"
    
    def impresion(self):
        pass
    
    def consulta(self):
        pass
    # Clase Factory: Factoria,fabrica
class FabricaClases:

    @staticmethod 
    def CreacionObjetos(tipoObjeto):
        if tipoObjeto=="A":
            return ClaseA()
        elif tipoObjeto =="B":
            return ClaseB()
        
        else :
            raise ValueError(f"la clase  {tipoObjeto} no existe")
        
#creo mi objeto
#objeto1= FabricaClases.CreacionObjetos("A")
objeto2=FabricaClases.CreacionObjetos("B")
#print(objeto1.operacion())
print(objeto2.operacion())
        