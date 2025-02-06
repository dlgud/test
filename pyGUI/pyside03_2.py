import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("QWidget: Event Mouse")

		self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
		self.text.setStyleSheet("backgound-color: grey")

		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.text)

		# self.text.setMouseTracking(True)
		self.setMouseTracking(True)	

	def mousePressEvent(self, e: QtGui.QKeyEvent) -> None:
		print(f"Press: {e.position().x(), e.position().y()}")

		btn = e.button()
		if btn == QtCore.Qt.LeftButton:
			print("- Left Button")
		elif btn == QtCore.Qt.RightButton:
			print("- Right Button")
		elif btn == QtCore.Qt.MiddleButton:
			print("- Middle Button")

		mod = e.modifiers()
		if mod == QtCore.Qt.ShiftModifier:
			print("- Modifier: Shif")
		elif mod == QtCore.Qt.AltModifier:
			print("- Modifier: Alt")
		elif mod == QtCore.Qt.ControlModifier:
			print("- Modifier: Ctrl")
		else:
			print(f"- Modifier: {mod}")
	
		return super().mousePressEvent(e)

	def mouseMoveEvent(self, e):
		print(f"Move: {e.position().x(), e.position().y()}")
		return super().mouseMoveEvent(e)

	def mouseReleaseEvent(self, e):
		print(f"Released: {e.position().x(), e.position().y()}")
		return super().mouseReleaseEvent(e)

	def mouseDoubleClickEvent(self, e):
		print(f"Double Clicked: {e.position().x(), e.position().y()}")
		return super().mouseDoubleClickEvent(e)

	def wheelEvent(self, e):
		print("Wheel")
		return super().wheelEvent(e)


if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWidget()
	window.resize(400, 200)
	window.show()

	sys.exit(app.exec())
