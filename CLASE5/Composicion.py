class Vehiculo:
    def __init__(self,motor): # en python siempre se finaliza con : 
        self.motor=motor
        
    def encender (self):
        print ("Encender el vehiculo")
        self.motor.iniciar()
    
    # como motor tiene vbarios atributos, funcionalidades  y es referible llamarlo como una clase
    # en la composicion un vehiculo tiene un motor no como herencia sino como composicion
class Motor:
    # le podemos crear el constructor a cada uno 
    def __init_ (self):
        pass
    def iniciar(self):#" siempre que defina un metodo va con self"
        pass
class MotorGasolina(Motor):
    def __init__(self):
        pass
    def iniciar(self):
        print("Motor de  gasolina encendido..")
class MotorElectrico(Motor):
    def __init__(self):
        
        pass
        
    def iniciar(self):
        print("Motor electrico encendido..")

class Vehiculo:
    def __init__(self,motor):
        self.motor=motor
        
    def encender(self):
        print("Encendiendo ell vehiculo")
        
        self.motor.iniciar()
    
    
#para activar la composicion debo crear un objeto para que me defina

motor_gasolina=MotorGasolina# se deberia crear este objeto para que sea mas seguro y se instancia y  toma todas las propiedades del motor Gasolina en este caso
motor_electrico=MotorElectrico
auto_gasolina=Vehiculo(motor_gasolina)
auto_electrico=Vehiculo(motor_electrico)


