import sqlite3

class datahelper_empleado():

	def __init__(self):
		self.con = None
		self.cursor=None
		self.create_database()

	def conect(self) :
		self.con=sqlite3.connect("test.db")
		self.cursor= self.con.cursor()

	def disconnect(self):
		self.con.close()

	def create_database(self):
		'''Crea la Tabla Empleados en el caso de no existir'''
		self.conect()
		self.cursor.execute(''' Create Table IF NOT EXISTS Empleados(
					id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
					nombre text,
					apellido text,
					sueldo int,
					afap int,
					fec_ing datetime,
					cant_hijos int
			)
			''')
		self.disconnect()

	def insert_empleado(self, e):
		'''Funcion que toma un objeto empleado y se encarga de cargarlo en la base de datos'''
		try:
			self.conect()
			self.cursor.execute("Insert Into Empleados(nombre,apellido,sueldo,afap,fec_ing,cant_hijos) "+ 
							"values('{}','{}',{},{},'{}',{})".format(e.nombre,e.apellido,e.sueldo_base,e.afap_tipo,e.fecha_ingreso,e.cantidad_hijos))
			self.con.commit()
		except:
			print "Error en la carga"

		finally:
			self.disconnect()

	def get_empleado(self, nombre,apellido):
		'''Devuelve un empleado en base de un nombre y apellido'''
		try:
			self.conect()
			registro = self.cursor.execute("select nombre, apellido, sueldo, afap, fec_ing, cant_hijos from empleados where nombre like '{}' and apellido like '{}'".format(nombre,apellido))
			return registro.fetchone()
		except:
			print "Error en la busqueda de empleado"
		finally:
			self.disconnect()

	def get_empleados(self):
		'''Devuelve la lista de empleados cargados'''
		try:
			self.conect()
			registros = list(self.cursor.execute("select * from empleados"))
			return registros
		except:
			print "Error en la busqueda de empleado"
		finally:
			self.disconnect()