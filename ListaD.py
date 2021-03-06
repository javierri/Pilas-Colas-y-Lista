class NodoD:
	 def __init__ (self,valor = None):
	 	self.info = valor
	 	self.sig = None
	 	self.ant = None
	 	
class ListaD:
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.Actual = None
		
	def insertar (self,valor):
		
		nodo=NodoD(valor)
		if (self.primero == None):
			self.primero = nodo
			self.ultimo = nodo
		elif (self.Actual != None):
			nodo.sig=self.Actual
			if (self.Actual != self.primero):
				nodo.ant = self.Actual.ant
				nodo.ant.sig = nodo
			else:
				self.primero = nodo
		
			self.Actual.ant = nodo
		else:
			nodo.ant=self.ultimo
			self.ultimo.sig = nodo
			self.ultimo = nodo
		
		self.Actual = nodo
		
	def eliminar(self):
		if (self.primero == None and self.Actual == None):
			return
			
		nodo = self.Actual 
		
		if (self.Actual == self.primero): 
			self.primero = nodo.sig
		else:
			self.Actual.ant.sig = nodo.sig
		
		if (self.Actual == self.ultimo): 
			self.ultimo = nodo.ant
		else:	
			self.Actual.sig.ant = nodo.ant
			
		self.Actual = nodo.sig
		del nodo
		
	def vaciar(self):
		while (self.primero != None):
			nodo = self.primero
			self.primero = nodo.sig
			del nodo
			
		self.actual = None
		self.ultimo = None
		
	def pos_actual(self):
		if (self.Actual == None):
			return None
		
		n = 0
		nodo = self.primero
		while (nodo != self.Actual):
			n = n + 1
			nodo = nodo.sig
		return n	
		
	def sig (self):
		if (self.Actual != None):
			self.Actual = self.Actual.sig
		
	def ant (self):
		if (self.Actual == self.primero):
			return 
		if (self.Actual != None):
			self.Actual = self.Actual.ant
		else:
			self.Actual = self.ultimo
			
	def mover(self, n):
		pos = 0
		if (n > 0):
			while (pos < n and self.Actual != None):
				self.sig()
				pos = pos + 1
		else:
			while (pos > n and self.Actual != None):
				self.ant()
				pos = pos - 1
			
	def actual_primero (self):
		self.Actual = self.primero
		
	def actual_finlista (self):
		self.Actual = None
		
	def actual_ultimo (self):
		self.Actual = self.ultimo
		
	def mostrar (self):
		nodo=self.primero
		while (nodo.sig != None):
			print nodo.info,
			nodo = nodo.sig
		print nodo.info





