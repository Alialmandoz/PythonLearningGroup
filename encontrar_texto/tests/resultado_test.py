import os
import unittest
from encontrar_texto import resultado

class Resultado_Test(unittest.TestCase):

	def test_resultadoPositive(self):
		valuesAcepted = ['4318630', '01/05/14', 'DIEZ', 'ESPINO', 'BENJAMIN', '30337', '2.5', 'DUDOSO']
		r = resultado.Resultado(valuesAcepted )


		assert r.get_id() == 4318630
		assert r.get_date() == '01/05/14'
		assert r.get_name() == "DIEZ ESPINO BENJAMIN"
		assert r.get_alfaValue() == 30337
		assert r.get_floatValue() == 2.5
		assert r.get_notes() == "DUDOSO "

	def test_resultadoNegative(self):
		valuesNone = ["daslkdn", "another", "29123801"]
		r = resultado.Resultado(valuesNone)

		assert r.get_id() == None
		assert r.get_date() == None
		assert r.get_name() == ""
		assert r.get_alfaValue() == 29123801
		assert r.get_floatValue() == None
		assert r.get_notes() == ""

if __name__ == '__main__':
	unittest.main()