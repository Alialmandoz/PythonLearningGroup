import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("peliculas.ui")[0]


class MyWindowMain(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.btn_add.clicked.connect(self.btn_add_clicked)
		self.lbl_alert.setText("")

	def btn_add_clicked(self):
		name = self.le_movie.text()

		if name != "":
			if self.check_movie_exists(name):
				self.listwgt_movies.addItem(name)
				self.lbl_alert.setText("")
				self.le_movie.setText("")
			else:
				self.lbl_alert.setText("Esta pelicula ya se encuentra listada")
		else:
			self.lbl_alert.setText("Inserte una pelicula valida")

	def check_movie_exists(self, name):
		if not self.listwgt_movies.findItems(name, QtCore.Qt.MatchContains):
			return True


app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowMain(None)
MyWindow.show()
app.exec_()
