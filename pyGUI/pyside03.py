import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QWidget: Event")

		# QMainWindow
		#self.statusBar().showMessage("Event Handling")

		self.button = QtWidgets.QPushButton("Click Me!")
		
		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.button)

	def MousePressEvent(self, event):
		print("Mouse is Pressed")
		return super().keyPressEvent(event)

	def MouseReleaseEvent(self, event):
		print("Mouse is Released")
		return super().keyReleaseEvent(event)

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWidget()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
