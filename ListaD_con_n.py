# Listas Doblemente Enlazadas
# Autor: Javier Rivera
# https://repl.it/Dfni/2

class NodoD:
	def __init__(self,valor):
		self.info = valor
		self.sig = None
		self.ant = None

class ListaD:
	def __init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0

	def insertar_primero (self, valor):
		nodo = NodoD(valor)
		
		nodo.sig = self.__primero
		nodo.ant = None 

		if (nodo.sig != None):
			nodo.sig.ant = nodo
		
		self.__n = self.__n + 1
		self.__actual = nodo
		self.__primero = nodo
		
		if (self.__ultimo == None):
			self.__ultimo = nodo
		

	def insertar_ultimo (self, valor):
		nodo = NodoD(valor)	
		
		nodo.sig = None 
		nodo.ant = self.__ultimo 
		
		nodo.ant.sig = nodo
		
		self.__n = self.__n + 1
		self.__actual = nodo
		self.__ultimo = nodo
		if (self.__primero == None):
			self.__primero = nodo
		
	def insertar (self, valor):
		if (self.__primero == None):
			self.insertar_primero(valor)
			return

		if (self.__actual == self.__ultimo):
			self.insertar_ultimo(valor)
			return

		nodo = NodoD(valor)
		
		nodo.sig = self.__actual.sig
		nodo.ant = self.__actual
		
		nodo.sig.ant = nodo
		nodo.ant.sig = nodo
		
		self.__n = self.__n + 1
		self.__actual = nodo

	def sig (self):
		if (self.__actual != None and self.__actual != self.__ultimo):
			self.__actual = self.__actual.sig

	def ant(self):
		if (self.__actual != None and self.__actual != self.__primero):
			self.__actual = self.__actual.ant
			
	def mostrar(self):
		nodo = self.__primero
		while (nodo != None):
			if (nodo == self.__actual):
				print "(", nodo.info, ")",
			else:
				print nodo.info,
			nodo = nodo.sig
		print
			
	def mostrar_inv(self):
		nodo = self.__ultimo
		while (nodo != None):
			if (nodo == self.__actual):
				print "(", nodo.info, ")",
			else:
				print nodo.info,
			nodo = nodo.ant
		print
