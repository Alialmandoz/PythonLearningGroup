import os
import unittest
from encontrar_texto import data_structure

TEST_TXT = os.path.join(os.path.dirname(__file__), 'text.txt')

class DataStructure_Test(unittest.TestCase):

	def test_createStructure(self):
		expect = [['4305912', '27/05/14', 'LONGHINI', 'MATEO', '20081', '0.7', 'NORMAL', 'AYU\n'],
				  ['4305862', '09/06/14', '1.0', 'NORMAL\n'],
				  ['4320064', '27/05/14', 'ZUCCOLO', 'CATRIEL', '20081', '1.2', 'NORMAL', 'AYU\n'],
				  ['4305864', '09/06/14', '1.2', 'NORMAL']]

		dt = data_structure.DataStructure(TEST_TXT)
		dt.open_fill()

		assert dt.get_all() == expect

	def test_format(self):
		values = [' 4318630\t 01/05/14\t   DIEZ ESPINO BENJAMIN\t             30337       2.5     DUDOSO             '
				  ' \n', '\n', ' 4280898\t 01/05/14\t   GONZALEZ ISIS       \t           '
							   '  30041       2.6     DUDOSO              \n', '\n', ' 4423229\t 08/05/14\t  '
																					 ' LUGONES MOURE JOSEFI\t       '
											 '80124       2.5     DUDOSO   ']
		dt = data_structure.DataStructure()
		dt.format(values)

		assert dt.get_case(0) == ['4318630', '01/05/14', 'DIEZ', 'ESPINO', 'BENJAMIN', '30337', '2.5', 'DUDOSO']
		assert dt.get_case(1) == ['4280898', '01/05/14', 'GONZALEZ', 'ISIS', '30041', '2.6', 'DUDOSO']
		assert dt.get_case(2) == ['4423229', '08/05/14', 'LUGONES', 'MOURE', 'JOSEFI', '80124', '2.5', 'DUDOSO']

if __name__ == '__main__':
	unittest.main()