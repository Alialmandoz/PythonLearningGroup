
class DataStructure():
	def __init__(self, file=None):
		self.data_structure=[]
		self.file=file

	def open_fill(self):
		with open(self.file) as f:
			data = []
			for line in f:
				data.append(line)

		self.format(data)

	def format(self,input):
		for info in input:
			temp = info.replace("\t", "").split(" ")
			temp = filter(None, temp)
			if "\n" in temp: temp.remove("\n")
			self.data_structure.append(temp)

		self.data_structure = filter(None, self.data_structure)

	def get_all(self):
		return  self.data_structure

	def get_case(self,value):
		try:
			if int(self.data_structure[value][0]):
				return self.data_structure[value]
		except:
			return "Case not Exists"