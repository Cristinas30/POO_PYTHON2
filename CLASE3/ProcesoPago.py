#interface s en Python se utiliza none

from abc import ABC,abstractmethod

class ProcesoPago(ABC):
    @abstractmethod ## tiene abstractas pero no constructores porque daria u error 
    
    def procesoPago(self,cantidad:float) ->None: ## none sirve para no retornar valores
        
        pass
    
    @abstractmethod
    
    def reembolsoPago(self,transaccionId:str)-> None:
        pass
    
class Paypal(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de $ {cantidad} por Paypal")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando Id transaccion numerp $ {transaccionId} por Paypal")
        
class Stripe(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print(f"Procesando pago de $ {cantidad} por Stripe")
        
    def reembolsoPago(self, transaccionId: str) -> None:
        print (f"Reemboldando Id Transaccion numero ${transaccionId}por Stripe")
        
    
## name Nombre del modulo es el mismo lugar donde yo lo estoy tratando de ejecutar es el m,etodo principal de 
## ahora creamos la instancia 
    
if __name__=="__main__": 
  ProcesoPaypal=Paypal()
  ProcesoStripe = Stripe()
  
  ProcesoPaypal.procesoPago(500.0)
  ProcesoPaypal.reembolsoPago("FDCS1254XE987")
  
  ProcesoStripe.procesoPago( 1000.0)
  ProcesoStripe.reembolsoPago("FDS1258655XE987")