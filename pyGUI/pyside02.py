import sys
import random

from PySide6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QMainWindow")

		self.statusBar().showMessage("Hello~~")

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWindow()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
