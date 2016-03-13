# Clase Lista con nodos enlazados
# Observación: ver en.. https://repl.it/Bvho
# Autor: Javier Rivera (UNEFA Mérida)

# Clase Nodo
class Nodo:
    def __init__(self, val = None):
        self.__valor = val
        self.__sig =  None
        
    def valor(self):
        return self.__valor
        
    def sig(self):
        return self.__sig
        
    def act_sig(self, nodo):
        self.__sig = nodo
        
    def __str__(self):
        return str(self.__valor)
        
# Clase Lista
class Lista:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__actual = None
    
    def insertar(self, valor = None):
        
        nodo = Nodo(valor)
        if (self.__primero == None):
            self.__primero = nodo
            self.__ultimo = nodo
        else:
            self.__ultimo.act_sig(nodo)
            self.__ultimo = nodo
        
    def __str__(self):
        
        salida = ""
        nodo = self.__primero
        while (nodo != None):
            #print nodo
            if (salida != ""):
                salida = salida + ","
            salida = salida + str(nodo.valor())
            nodo = nodo.sig()    
            
        return salida

# PRINCIPAL
            
lista = Lista()

lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)
lista.insertar("Hola")
lista.insertar(7.2)
lista.insertar([1,3])

print lista
