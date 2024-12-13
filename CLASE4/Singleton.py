#Patron de diseño Singleton
class SingletonCreacionInstancia:
    
# el singleton trae una srie de valores para configurar ese solo objeto y tamien me crea conexiones globales

    _instancia = None ## si esta esta fuera es una variable de la clase y si esta dentro del init es una variable de la instancia
    
    def __new__(cls,*args,**kwargs):# new es el constuctor del Singleton
        
        if not cls._instancia:
            cls._instancia= super(SingletonCreacionInstancia,cls).__new__(cls)
            
    
    ## hereda todas las clase y metoidos que pueda tener dentro de la clase Singleton Creacion  Instancia
 
        return cls._instancia