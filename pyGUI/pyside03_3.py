import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MyLabel(QtWidgets.QLabel):
	def __init__(self):
		super().__init__()
		self.setText("Hello World")
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setStyleSheet("background-color: yellow")

	# override
	def enterEvent(self, e):
		self.setText("Entered")
		return super().enterEvent(e)

	def leaveEvent(self, e):
		self.setText("Leaved")
		return super().leaveEvent(e)


class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QWidget: Event")
		
		self.text = MyLabel()
		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.text)


if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWidget()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
