#import PySide6.QtCore
#print(PySide6.__version__)
#print(f"QtCore Ver.: {PySide6.QtCore.__version__}")

import sys
from PySide6 import QtCore, QtGui, QtWidgets

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("First PySide6")
		self.txt = QtWidgets.QLabel("Hello PySide6", alignment=QtCore.Qt.AlignCenter)
		self.btn = QtWidgets.QPushButton("Click Me")

		self.layout = QtWidgets.QVBoxLayout(self)
		self.layout.addWidget(self.txt)
		self.layout.addWidget(self.btn)

		self.btn.clicked.connect(self.btnSlot)

	@QtCore.Slot()
	def btnSlot(self):
		self.txt.setText("Hello~~~")


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	widget = MyWidget()
	widget.resize(400, 200)
	widget.show()

	sys.exit(app.exec())
