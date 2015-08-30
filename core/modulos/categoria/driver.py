#version 0.01
from ..driver_generic import DriverGeneric
'Se importan los driver genericos'

class DriverCategory(DriverGeneric):
	'''Clase funciona para dar funcionalidad al modulo ereda de DriverGeneric 
	todas las opciones'''	
	
	def __init__(self, values):
		'Se sobrecarga metodo init para colocar tabla afecta'
		super().__init__(values)
		self.tb = "categoria"