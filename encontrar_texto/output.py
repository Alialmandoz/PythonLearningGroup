from resultado import Resultado
from data_structure import DataStructure

class Output():
	def __init__(self, entry=None):
		self.input=entry
		self.output=[]

	def create_output(self):
		"""Funcion que crea el objeto con la estrusctura de datos leible y luego
			crea el objeto resultado que posee una estructura mas leible para ser introducido
			en el output.txt ademas de guardarlo en lista a los valores
		"""
		f = open("Output.txt", "w")
		dt = DataStructure(self.input)
		dt.open_fill()
		for i in dt.get_all():
			p = Resultado(i)
			if type(p.get_id()) == (int):
				self.output.append(p.get_all())
				f.write("{}\n\n".format(p.get_all()))

		f.close()

	def get_output(self):
		return self.output

	def get_input(self):
		return self.input