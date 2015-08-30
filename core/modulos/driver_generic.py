#version 0.01
class DriverGeneric:
	actions = {}
	
	def __init__(self, values):
		DriverGeneric.actions = {'1': self.insert, '2': self.update, '3': self.delete, '4': self.search}	
		self.validate_values(values)

	def validate_values(self, values):
		self.error = ""
		self.acc = values.get('acc')
		self.values = values.get('values')
		if not(self.acc):
			self.error += "Error en accion"

		if not(self.values):
			self.error += "Error en valores"
		
	def execute_action(self):
		action = self.actions.get(self.acc)
		if action:
			self.obj_table.assign_values(self.values)
			action()
		else:
			self.error += "No existe Opcion"


	def insert(self):
		self.answer = self.obj_table.insert()
		if not(self.answer):
			self.error += self.obj_table.error
	def update(self):
		print("update")
	def delete(self):
		print("delete")
	def search(self):
		print("search")