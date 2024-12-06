class CuentaBancaria:
    def __init__(self,titular,saldo,clave):
        
        self.titular=titular
        self._saldo = saldo # es_ protejida
        self.__clave = clave # es __doble es privada
        pass
    def depositar(self,cantidadDeposito):
    
        self._saldo += cantidadDeposito
        return f"Deposito exitoso. Saldo actual{self._saldo}"
    
    def retirar(self,cantidadRetiro):
        if cantidadRetiro> self._saldo:
            return "Fondos Insuficientes"
        self._saldo-=cantidadRetiro
        return f"Retiro exitoso.El saldo actual es {self._saldo}"
            
        pass
    
    def modificarClave(self,nuevaClave):
        self.__clave = nuevaClave
        return f"Clave modifidcada de forma exitosa.La nueva clave es: {self.__clave}"
    
CuentaBancaria1= CuentaBancaria("Luis Guilllermo",1000000,1234)#creando ell objeto
print(CuentaBancaria1.titular)
print(CuentaBancaria1._saldo)

print(CuentaBancaria1.depositar(500000))# con esto estoy diceindo que se retira 500000
print(CuentaBancaria1.depositar(500000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.retirar(100000))
print(CuentaBancaria1.modificarClave(55555))# se modifica la clave
