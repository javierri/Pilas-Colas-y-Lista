from ListaD import *

class Cola(ListaD):
	
	def Meter(self, elem):
		self.actual_finlista()
		self.insertar(elem)
	
	def Sacar(self):
		if (self.primero != None):
			self.actual_primero()
			elem = self.Actual.info
			self.eliminar()
			return elem
	
	def Primero(self):
		if (self.primero != None):
			return self.primero.info
			
