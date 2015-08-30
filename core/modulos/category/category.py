from ..table_generic import TableGeneric

class Category(TableGeneric):
	attributes = {'titulo':'', 'padre':'', 'estatus':''}
	table = 'categoria'