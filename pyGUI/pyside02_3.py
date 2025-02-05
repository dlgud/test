import sys
from PySide6 import QtCore, QtWidgets, QtGui


# 메뉴는 QMenu, 메뉴 항목은 QAction
class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QMainWindow: 2.3")

		self.statusBar().showMessage("Hello v.2.3")
		self.text = QtWidgets.QTextEdit()
		self.setCentralWidget(self.text)

		exitAction = QtGui.QAction("Exit", self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip("Exit Program")
		exitAction.triggered.connect(self.close)

		newAction = QtGui.QAction("New", self)
		newAction.setShortcut('Ctrl+N')
		newAction.setStatusTip("New File")
		newAction.triggered.connect(self.slot_new)

		openAction = QtGui.QAction("Open", self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip("Open File")
		openAction.triggered.connect(self.slot_open)

		saveAction = QtGui.QAction("Save", self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip("Save File")
		saveAction.triggered.connect(self.slot_save)

		saveasAction = QtGui.QAction("Save As", self)
		saveasAction.setShortcut('Ctrl+Shift+S')
		saveasAction.setStatusTip("Save As File")

		# self.slot_display("Save As File")이 즉시 실행되어 반환값(None)이 connect()에 전달됨.
		# 이렇게 되면 Triggered 시그널이 발생해도 아무런 동작응 하지 않음.
		#saveasAction.triggered.connect(self.slot_display("Save As File"))
	
		# 람다 함수를 사용해서 인자를 전달해야 함.
		saveasAction.triggered.connect(lambda: self.slot_display("Save As File"))

		menubar = self.menuBar()
		#menubar.setNativeMenuBar(False) # menubar in window

		filemenu = menubar.addMenu("&File") # alt + F
		filemenu.addAction(newAction)
		filemenu.addAction(openAction)
		filemenu.addSeparator()

		savemenu = QtWidgets.QMenu("&Save", self)
		savemenu.addAction(saveAction)
		savemenu.addAction(saveasAction)

		filemenu.addMenu(savemenu)
		filemenu.addSeparator()
		filemenu.addAction(exitAction)

		self.toolbar = self.addToolBar("File")
		self.toolbar.addAction(newAction)
		self.toolbar.addAction(openAction)
		self.toolbar.addSeparator()
		self.toolbar.addAction(saveAction)
		self.toolbar.addAction(saveasAction)
		self.toolbar.addSeparator()
		self.toolbar.addAction(exitAction)

	@QtCore.Slot()
	def slot_new(self):
		self.text.append("New File")

	@QtCore.Slot()
	def slot_open(self):
		self.text.append("Open File")
		
	@QtCore.Slot()
	def slot_save(self):
		self.text.append("Save File")
		
	@QtCore.Slot(str)
	def slot_display(self, msg):
		self.text.append(msg)

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWindow()
	geometry = window.screen().availableGeometry()
	window.resize(geometry.width() * 0.3, geometry.height() * 0.3)

	window.show()

	sys.exit(app.exec())
