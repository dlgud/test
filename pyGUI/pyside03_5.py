import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QWidget: Slot")
		
		self.button = QtWidgets.QPushButton("Click Me!")
		self.button.setToolTip("Clear Text above")

		self.text = QtWidgets.QLabel("Hello World!", alignment=QtCore.Qt.AlignCenter)
		self.text.setStyleSheet("background-color: gray")

		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.button)

		self.button.clicked.connect(self.slot_clicked)
		#self.button.clicked.disconnect(self.slot_clicked)
		#self.button.clicked.emit()		# publish clicked event

	@QtCore.Slot()
	def slot_clicked(self):
		self.text.setText("Button Clicked")


if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWidget()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
