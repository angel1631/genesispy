#version 0.01
from ..driver_generic import DriverGeneric
from .category import Category
'Se importan los driver genericos'

class DriverCategory(DriverGeneric):
	'''Clase funciona para dar funcionalidad al modulo ereda de DriverGeneric 
	todas las opciones'''	
	table = "categoria"
	obj_table = Category()
	