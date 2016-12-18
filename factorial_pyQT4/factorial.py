import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("factorial.ui")[0]

class MyWindowMain(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.btn_next.clicked.connect(self.btn_next_clicked)
		self.btn_reset.clicked.connect(self.btn_reset_clicked)
		self.txt_n.setText(str(1))
		self.txt_factorial.setText(str(1))

	def btn_next_clicked(self):
		n = int(self.txt_n.toPlainText())+1
		self.txt_n.setText(str(n))

		value_fac=1
		for i in range(1,n+1):
			value_fac*=i

		self.txt_factorial.setText(str(value_fac))

	def btn_reset_clicked(self):
		self.txt_n.setText(str(1))
		self.txt_factorial.setText(str(1))

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowMain(None)
MyWindow.show()
app.exec_()

