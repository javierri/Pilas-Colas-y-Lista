# LPIII_2016
# Autor: JAVIER RIVERA (UNEFA)
# Ver en : http://replit.com/DaSb/7

# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo que busca si un valor existe en la lista 
	def busca_valor (self, valor):
		
		nodo  = self.__primero
		p = 0
		while (nodo != None) :
			if (nodo.info == valor):
				return p 
			
			nodo = nodo.sig
			p = p + 1
			
		return -1
		
	# Metodo para eliminar el primer elemento de la lista
	def elimina_primero(self):
		
		if (self.__primero == None):
			return

		nodo = self.__primero
		self.__primero = nodo.sig
		del nodo 
		
		self.__n = self.__n - 1
		if (self.__n == 0):
			self.__ultimo = None

		if (self.__pos == 0):
			self.__actual = self.__primero
		else:
			self.__pos = self.__pos - 1


	# Metodo para ubicar en actual en la posicion "pos" (enviada por parametro)
	def pos_actual(self, pos):
		pass
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		
		nodo = self.__primero
		for i in range (self.__n):
			if (i == self.__pos):
				print "(",nodo.info,")", 
			else: 
				print nodo.info, 
			nodo=nodo.sig	
			
		print 
		
