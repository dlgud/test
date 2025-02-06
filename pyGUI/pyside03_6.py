import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MySignal(QtCore.QObject):
	exitSignal = QtCore.Signal()
	setSignal = QtCore.Signal()

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

		self.setMouseTracking(True)

		self.mySignal = MySignal()
		self.mySignal.exitSignal.connect(self.close)			# only connect
		self.mySignal.setSignal.connect(self.slot_setText)

	@QtCore.Slot()
	def slot_setText(self):
		self.text.setText("User Defined Signal")

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			self.mySignal.exitSignal.emit()				# execute 
		return super().keyPressEvent(e)

	def mouseDoubleClickEvent(self, e):
		self.mySignal.setSignal.emit()
		return super().mouseDoubleClickEvent(e)

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWidget()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
