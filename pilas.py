# Clase Pila implementada con la estructura lista de python 
# Observación: ver en.. https://repl.it/Bvhi/2
# Autor: Javier Rivera (UNEFA Mérida)

class Pila:
    def __init__(self):
        self.__datos = []
        
    def meter(self,valor):
        self.__datos.append(valor)
        
    def sacar(self):
        p_ult = len(self.__datos) - 1
        if (p_ult > 0):
            del self.__datos[p_ult]
            
    def numElem(self):
        return len(self.__datos)
        
    # Invierte los elementos de pila    
    def invertir(self):
        pass
    
    # Elimina todos los datos de la pila
    def vaciar(self):
        pass
    
    # Retorna los datos de la pila en una lista
    def listaPila(self):
        pass
            
    def __str__(self):
        return str(self.__datos)
        
# PRINCIPAL

p = Pila()

p.meter(2)
p.meter(4)
p.meter("Hola")
p.meter(3)

print p

p.sacar()
print p


        
    
