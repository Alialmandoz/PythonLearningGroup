import datetime
from empleado import Empleado
from sqlite_empleado import datahelper_empleado

class Main():

	def __init__(self):
		self.datos=datahelper_empleado()
		self.empleado=None
		self.empleados=[]
		self.sum_sueldos=0
		self.cant_empleados=0
		self.menu=True

	def menu_principal(self):
		'''Loop encargado de mantener el menu activo de ademas
		de poder elegir las opciones'''
		while self.menu:
			try:
				print("\n")
				self.menu_opciones()
				choice=int(raw_input("\nInserte opcion de menu: "))
				print("\n")
				if choice==1:
					self.cargar_empleado_db()
				elif choice==2:
					self.mostrar_lista_empleados()
				elif choice==3:	
					self.recuperar_empleado()
				elif choice==6:
					self.calcular_promedio_sueldo()
				elif choice==0:
					print "Gracias por usar el software"
					self.menu=False
				else:
					print "Puso una opcion no valida"
			except:
				print "Puso una opcion no valida"

	def menu_opciones(self):
		'''La interfaz grafica del menu'''
		print 30 * "-" , "MENU" , 30 * "-"
		print "1. Cargar nuevo empleado"
		print "2. Mostra lista resumida empleados"
		print "3. Mostrar un empleado"
		print "6. Calcular promedio sueldo"
		print "0. Salir"
		print 67 * "-"

	def recuperar_empleados_db(self):
		'''Se encarga de volver a tomar la lista de empleados de la base de datos
		y guardandolos en la lista self.empleados borrando previamente su contenido
		por si existe carga anterior'''
		empleados_db=self.datos.get_empleados()
		del self.empleados[:]
		for i in empleados_db:
			empleado = Empleado(i[1],i[2],i[3],i[4],i[5],i[6])
			self.empleados.append(empleado)

	def mostrar_lista_empleados(self):
		'''Muestra la lista de manera resumida.
		Para mostrar la correcta se llama a la funcion encargada de actualizar la lista'''
		self.recuperar_empleados_db()
		for i in self.empleados:
			print "Nombre y Apellido: {}, {} / Sueldo Neto: {}".format(i.nombre,i.apellido,i.sueldo())

	def suma_sueldos(self):
		'''Suma todos los sueldos de los empleados en la lista self.empleados'''
		for i in self.empleados:
			self.sum_sueldos+=i.sueldo()

	def get_cantidad_empleados(self):
		'''Actualiza la variable de cuantos empleados hay en la lista'''
		self.cant_empleados=len(self.empleados)

	def calcular_promedio_sueldo(self):
		'''Actualiza la lista, suma los sueldos, actualiza la cantidad de empleados
		y hace las funciones aritmetica para devolver el promedio'''
		self.recuperar_empleados_db()
		self.suma_sueldos()
		self.get_cantidad_empleados()
		if self.cant_empleados !=0 :
			print "Sueldo Promedio pagado: {}".format(self.sum_sueldos/self.cant_empleados)
		else:
			print "Sueldo Promedio pagado: {}".format(self.sum_sueldos)

	def recuperar_empleado(self):
		'''Insertandole por consola el nombre y apellido se encarga de devolver
		la primera concordancia con esos valores en el caso de existir,
		 aun no distingue entre personas del mismo nombre'''
		while True:
			nombre=raw_input("Nombre: ")
			if len(nombre)>=3: break
			else: print "Inserte nombre valido"
		while True:
			apellido=raw_input("Apellido: ")
			if len(apellido)>=3: break
			else: print "Inserte apellido valido"

		i=self.datos.get_empleado(nombre,apellido)

		if i != None:
			empleado= Empleado(i[0],i[1],i[2],i[3],i[4],i[5])
			self.empleado=empleado
			print self.empleado
		else:
			print "No se encontro ningun empleado con esos valores"

	def cargar_empleado_db(self):
		'''Realiza la carga de las variables a ser insertadas en el objeto empleado
		para luego cargarlos en la base de datos, validando sus ingresos
		Al ultimo imprime el __str__ del empleado'''
		while True:
			nombre=raw_input("Inserte nombre: ")
			if len(nombre)>3 and str(nombre): break
			else: print ("Nombre no invalido")
		while True:
			apellido=raw_input("Inserte Apellido: ")
			if len(apellido)>3 and str(apellido): break
			else: print ("Apellido no valido")
		while True:		
			try:
				sueldo=float(raw_input("Inserto sueldo(Minimo 900): "))
				if sueldo>900: break	
				else: print "Inserto un valor minimo al aceptable"
			except:
				print "Asegurese de estar insertando numeros"
		while True:
			try:
				afap=int(raw_input("Inserte Afap: "))
				if 0<afap<3: break
				else: print "Inserto un tipo no valido (1 o 2)"
			except:
				print "Inserto un valor no valido o incorrecto"

		while True:
			try:
				fec_ingreso=raw_input("Inserte Fecha de ingreso(dd/mm/yyyy): ")
				fec_ingreso==datetime.datetime.strptime(fec_ingreso,'%d/%m/%Y').date()
				break
			except:
				print "Formato Incorrecto"
		while True:
			try:
				cant_hijos=int(raw_input("Inserte cantidad de hijos: "))
				break
			except:
				print "Coloco un numero no valido"

		empleado = Empleado(nombre,apellido,sueldo,afap,fec_ingreso,cant_hijos)
		self.datos.insert_empleado(empleado)
		print empleado

if __name__ == '__main__':
	start = Main()
	start.menu_principal()
