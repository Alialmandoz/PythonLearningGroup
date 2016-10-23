from datetime import datetime


class Resultado():
	def __init__(self,data):
		self.len=2

		self.id=self.set_id(data)
		self.date=self.set_date(data)
		self.name=self.set_name(data)
		self.alfaValue=self.set_alfavalue(data)
		self.floatValue=self.set_floatValue(data)
		self.notes=self.set_notes(data)

	def set_id(self, input):
		try:
			int(input[0])
			self.id=input[0]
			return self.id
		except:
			self.id="Case not Exist"
			return self.id

	def get_id(self):
		try:
			return int(self.id)
		except:
			pass


	def set_date(self, input):
		try:
			d = datetime.strptime(input[1], '%d/%m/%y')
			self.date=d.strftime('%d/%m/%y')
			return  self.date
		except:
			self.date = None

	def get_date(self):
			return self.date


	def set_name(self, input):
		try:
			temp = ""
			while not any(char.isdigit() for char in input[self.len]):
				if self.len > 2:
					temp += ' '
				temp += input[self.len]
				self.len += 1

			self.name=temp
			return self.name

		except:
			self.name=None

	def get_name(self):
		return self.name

	def set_alfavalue(self, input):
		try:
			int(input[self.len])
			self.alfaValue=input[self.len]
			self.len += 1
			return int(self.alfaValue)
		except:
			self.alfaValue=None


	def get_alfaValue(self):
		return self.alfaValue

	def set_floatValue(self, input):
		try:
			float(input[self.len])
			self.floatValue= input[self.len]
			self.len += 1
			return float(self.floatValue)
		except:
			self.floatValue = None

	def get_floatValue(self):
		return self.floatValue

	def set_notes(self, input):
		try:
			temp = ""
			while len(input) > self.len:
				temp += input[self.len] + ' '
				self.len += 1

			self.notes=temp
			return self.notes
		except:
			self.notes=None

	def get_notes(self):
		return self.notes

	def get_all(self):
		return 'ID: {} \nDate: {} \nName: {}\nAlfa: {}\nFloat: {}\nNotes: {}'.format(self.id,self.date,
															self.name,self.alfaValue, self.floatValue,self.notes)


