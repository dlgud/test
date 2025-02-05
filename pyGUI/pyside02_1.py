import sys

from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QWidget: Font & ToolTip")

		self.btn = QtWidgets.QPushButton("Click Me!")
		QtWidgets.QToolTip.setFont(QtGui.QFont("SansSeif", pointSize=10))
		self.btn.setToolTip("Click the Button")

		self.txt = QtWidgets.QLabel("Hello World!", alignment=QtCore.Qt.AlignCenter)
		self.txt.setFont(QtGui.QFont("SansSerif", pointSize=15, weight=QtGui.QFont.Bold, italic=True))
		self.txt.setToolTip("Hi there!")		

		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.txt)
		self.layout.addWidget(self.btn)
	

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	widget = MyWidget()
	geometry = widget.screen().availableGeometry()
	print(f"geometry: {geometry}")
	widget.resize(geometry.width() * 0.35, geometry.height() * 0.3)
	#widget.setFixedSize(geometry.width() * 0.5, geometry.height() * 0.3)
	#widget.setBaseSize(geometry.width() * 0.5, geometry.height() * 0.3)

	widget.show()

	sys.exit(app.exec())
