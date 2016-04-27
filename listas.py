# Clase Lista con nodos enlazados
# Observación: 
# Autor: Javier Rivera (UNEFA Mérida)

# Clase Nodo
class Nodo:
	def __init__(self,info):
		self.Info = info
		self.sig = None
		
# Clase Lista	
class Lista:
	def __init__(self, *elem):
		self.__primero = None
		self.__ultimo = None
		self.ant_actual = None
		
		for i in elem:
			self.insertar_ultimo(i)
			
	def insertar_inicio(self, *elem):
		for i in elem:
			nodo = Nodo(i)
			if (self.__primero != None):
				nodo.sig = self.__primero
			else:
				self.__ultimo = nodo
				
			self.__primero = nodo
			
	def insertar_ultimo(self, *elem):
		for i in elem:
			nodo = Nodo(i)
			if (self.__ultimo != None):
				self.__ultimo.sig = nodo
				self.__ant_actual = self.__ultimo
			else:
				self.__primero = nodo
					
			self.__ultimo = nodo
			
	def elimina_primero():
		if (self.__primero == None):
			return
			
		nodo = self.__primero
		self.__primero = nodo.sig
		del nodo
			
	def __add__(self,list2):
		list3 = Lista()
		
		nodo = self.__primero
		while (nodo != None):
			list3.insertar_ultimo(nodo.Info)
			nodo = nodo.sig
		
		nodo = list2.__primero
		while (nodo != None):
			list3.insertar_ultimo(nodo.Info)
			nodo = nodo.sig
			
		return list3
    
	def eliminar_elem (self,elem):
		while (self.__primero != None and self.__primero.Info == elem):
			temp = self.__primero
			self.__primero = temp.sig
			del temp

		nodo=self.__primero
		while (nodo != None):
			while (nodo.sig != None and nodo.sig.Info == elem):
				temp = nodo.sig
				if (temp == self.__ultimo):
					self.__ultimo = nodo
				nodo.sig = temp.sig
				del temp
			nodo=nodo.sig

	def sig (self):
		if (self.__primero == None):
			return
		if (self.__ant_actual == None):
			self.__ant_actual = self.__primero
			return
		actual = self.__ant_actual.sig
		if (actual.sig != None):
			self.__ant_actual = actual

	def elimina_actual(self):
		if (self.__primero == None):
			return
		if (self.__ant_actual == None):
			temp = self.__primero
			self.__primero = temp.sig
			del temp
		else:
			temp = self.__ant_actual.sig
			self.__ant_actual.sig = temp.sig
			del temp

	def cons (self):
		if (self.__primero == None):
			return
		if (self.__ant_actual==None):
			return self.__primero.Info
		return self.__ant_actual.sig.Info

	def inicio(self):
		self.__ant_actual = None
		
	def actual_es_ultimo(self):
		if (self.__ant_actual != None):
			if (self.__ant_actual.sig == self.__ultimo):
				return True
		return False
			
	def mostrar(self):
		nodo = self.__primero
		while (nodo != None):
			print nodo.Info,
			nodo = nodo.sig
		print


# PRINCIPAL
			
l1 = Lista(3,3,4,3,6,3,5,4,3,2,1,4,3)
l1.mostrar()
l1.eliminar_elem(3)
l1.mostrar()

elem = 4
l1.inicio()
while (not l1.actual_es_ultimo()):
	if (l1.cons() == elem):
		l1.elimina_actual()
	else:
		l1.sig()
		
if (l1.cons() ==  elem):
	l1.elimina_actual()
	
l1.mostrar()
