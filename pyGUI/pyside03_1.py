import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QWidget: Event Key Input")

	# Override 
	#def keyPressEvent(self, e):	 # e: event
	def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
		if e.key() == QtCore.Qt.Key_Escape:
			self.close()
		else:
			print(f"Pressed: key={e.key()}, text={e.text()}, type={e.type()}")
		return super().keyPressEvent(e)

	def keyReleaseEvent(self, e):
		print(f"Released: key={e.key()}, text={e.text()}, type={e.type()}")
		return super().keyReleaseEvent(e)

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWidget()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
