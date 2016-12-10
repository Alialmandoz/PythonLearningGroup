from calendar import monthrange
import datetime

class Empleado(object):

	def __init__(self,nombre,apellido,sueldo_base,afap,fecha_ingreso,cantidad_hijos):
		self.nombre=nombre
		self.apellido=apellido
		self.sueldo_base=sueldo_base
		self.afap_tipo=afap
		self.fecha_ingreso=fecha_ingreso
		self.cantidad_hijos=cantidad_hijos
			
	@property
	def nombre(self):
		return str(self._nombre)

	@nombre.setter
	def nombre(self, n):
		try:
			if (len(n)>=3): 
				self._nombre=n
		except Exception as e:
			print e

	@property
	def apellido(self):
		return str(self._apellido)

	@apellido.setter
	def apellido(self, a):
		try:
			if (len(a)>=3): 
				self._apellido=a
		except Exception as e:
			print e

	@property
	def sueldo_base(self):
		return float(self._sueldo_base)

	@sueldo_base.setter
	def sueldo_base(self, s):
		try:
			self._sueldo_base=float(s)
		except Exception as e:
			print e

	@property 
	def afap_tipo(self):
		return self._afap_tipo

	@afap_tipo.setter
	def afap_tipo(self, a):
		try:
			if 0<a<3:
				self._afap_tipo=a
		except Exception as e:
			print e


	@property
	def fecha_ingreso(self):
		return self._fecha_ingreso

	@fecha_ingreso.setter
	def fecha_ingreso(self, fi):
		try:
			format_valid=['%Y-%m-%d','%d/%m/%Y']
			for fv in format_valid:
				try:
					date=datetime.datetime.strptime(fi,fv).date()
					self._fecha_ingreso=date
				except:
					pass
			# date=datetime.datetime.strptime(fi,'%d/%m/%Y').date()
			self._fecha_ingreso=date
		except Exception as e:
			print e

	@property
	def cantidad_hijos(self):
		return int(self._cantidad_hijos)

	@cantidad_hijos.setter
	def cantidad_hijos(self, ch):
		try:
			self._cantidad_hijos=int(ch)
		except Exception as e:
			print e

	def calcular_meses(self,fec_ing):
		fecha_actual=datetime.datetime.now().date()
		meses = 0
		while True:
			mdays = monthrange(fec_ing.year, fec_ing.month)[1]
			fec_ing += datetime.timedelta(days=mdays)
			if fec_ing <= fecha_actual:
				meses += 1
			else:
				break
		return meses

	def base_imponible(self):
		meses_trabajados=self.calcular_meses(self.fecha_ingreso)
		bonificacion=0.01*self.sueldo_base*meses_trabajados
		asignacion_Familiar=0.05*float(self.cantidad_hijos)
		base_imponible=self.sueldo_base+bonificacion+asignacion_Familiar

		return base_imponible

	def fonasa(self):
		salud_fonasa=0.07*self.base_imponible()

		return salud_fonasa

	def afap(self):
		if self.afap_tipo==1:
			afps_gasto=0.12*self.base_imponible()
		elif self.afap_tipo==2:
			afps_gasto=0.114*self.base_imponible()

		return afps_gasto

	def sueldo(self):

		sueldo=self.base_imponible()-self.fonasa()-self.afap()
		return sueldo

	def __str__(self):
		return ('''
			Nombre y Apellido: {} {} 
			Sueldo Base: {}
			Base imponible: {} 
			Fonasa: {}
			Afap: {}
			Sueldo Neto: {}
					''').format(self.nombre,self.apellido,self.sueldo_base, self.base_imponible(),self.fonasa(),self.afap(),self.sueldo())