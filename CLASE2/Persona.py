class Persona:
    def __init__(self,nombre,edad): #METODO CONSTRUCTOR UTILIZANDO SELF REPRESENTA CON METODOS DE INSTABNCIA, primero la instancia y luego los argumentos
        self.nombre = nombre
        self._edad = edad
        self._cuentaBancaria =123456
            

    def mostrarInformacion(self):
        return f"Nombre: {self.nombre} Edad:{self._edad}"
   
    def _mostrarCuenta(self):
        return f"Cuenta bancaria: {self._cuentaBancaria}"
    
    def mostrarInformacionCompleta(self):
        return self._mostrarCuenta()

persona1=Persona("Luis Guillermo", 49)

print(persona1.nombre)
print(persona1._edad)

print(persona1.mostrarInformacion())

print(persona1.mostrarInformacionCompleta())
