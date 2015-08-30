import mysql.connector
from mysql.connector import errorcode



class DataBase:
	CONFIG = {
	  'user': 'root',
	  'password': '',
	  'host': '127.0.0.1',
	  'database': 'genesispy',
	  'raise_on_warnings': True,
	}
	txt_insert = 'INSERT INTO {0} ({1}) VALUES({2})';
	error = ''	
	def __init__(self,table,attributes):
		self.table = table
		self.connect()
		self.generate_string(attributes)
	def connect(self):
		try:
			self.connection = mysql.connector.connect(**self.CONFIG)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
		else:
			print("All Ok")
			#return connection.cursor()
	def generate_string(self,attributes):
		encabezado, valores = '', ''
		for punter in attributes:
			encabezado += punter+', '
			valores += '%('+punter+')s, '
		encabezado, valores = encabezado[:-2], valores[:-2]
		self.txt_insert = self.txt_insert.format(self.table,encabezado,valores) 
	def insert(self,data):
		self.cursor = self.connection.cursor()
		try:
			self.cursor.execute(self.txt_insert, data)
		except mysql.connector.Error as err:
			self.error = err
			return None
		else:
			lastid = self.cursor.lastrowid 	
			self.connection.commit()
			self.disconnect();
			return lastid


	def disconnect(self):	
		self.cursor.close()
		self.connection.close()
	def start_transaction(self):
		pass
	def confirm_transaction(self):
		connection.commit()
		if connection.error != "":
			return "Erro: "+connection.error
	def rollbak_transaction(self):
		connection.rollback()
	def restrictions(dic_restriction):
		output = "WHERE "
		for restriction in dic_restriction:
			output += " "+restriction[0]+" "
			output += restriction[1]+" "
			output += restriction[2]+" "
			if restriction[3] == ".":
				output += restriction[3]
			elif restriction[3] == "":
				output += "NULL";
			else:
				output += "'"+restriction[3]+"'";
		return output
	def select(selection, restriction, tables):
		connet()
		sql = "SELECT "
		for column in selection:
			sql += column+", "
		sql = sql[0:-2]+" FROM"
		for table in tables:
			sql += table+", "
		sql = sql[0:-2]
		if len(restriction) > 0:
			restrictions(restriction)
		result = cursor.execute
		if connection.error:
			print(connection.error)
		else:
			for line in result:
				print (line['id'])	




