from ..librerias.propias.py.base import DataBase

class TableGeneric:
	error = ''
	def __init__(self):
		self.db = DataBase(self.table, self.attributes)

	def assign_values(self, values):
		for valor in values:
			self.attributes[valor] = values[valor]
	def insert(self):
		self.answer_db = self.db.insert(self.attributes)
		if self.answer_db:
			return {'cod':'1','msj': self.answer_db}
		else:
			self.error = self.db.error
			return None 