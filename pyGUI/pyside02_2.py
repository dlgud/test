import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QMainWindow: 2.2")

		self.statusBar().showMessage("Hello~~")
		#self.statusBar().clearMessage()
		#print(self.statusBar().currentMessage())

		exitAction = QtGui.QAction("Exit", self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip("Exit Program")
		exitAction.triggered.connect(self.close)

		copyAction = QtGui.QAction("Copy", self)
		copyAction.setShortcut('Ctrl+C')
		copyAction.setStatusTip("Copy Text")

		zoominAction = QtGui.QAction("Zoom In", self)
		zoominAction.setShortcut('Ctrl+I')
		zoominAction.setStatusTip("Zoom In")

		zoomoutAction = QtGui.QAction("Zoom Out", self)
		zoomoutAction.setShortcut('Ctrl+O')
		zoomoutAction.setStatusTip("Zoom Out")

		menubar = self.menuBar()
		#menubar.setNativeMenuBar(False) # menubar in window

		filemenu = menubar.addMenu("&File") # alt + F
		editmenu = menubar.addMenu("&Edit") # alt + E
		viewmenu = menubar.addMenu("&View") # alt + V
		filemenu.addAction(exitAction)
		editmenu.addAction(copyAction)

		zoommenu = QtWidgets.QMenu("&Zoom", self)
		zoommenu.addAction(zoominAction)
		zoommenu.addSeparator()
		zoommenu.addAction(zoomoutAction)
		viewmenu.addMenu(zoommenu)

		self.toolbar = self.addToolBar("Exit")
		self.toolbar.addAction(exitAction)
		self.toolbar.addAction(zoominAction)
		self.toolbar.addAction(zoomoutAction)
		

if __name__ == "__main__":
	app = QtWidgets.QApplication([])

	window = MyWindow()
	geometry = window.screen().availableGeometry()
	window.resize(geometry.width() * 0.3, geometry.height() * 0.3)

	window.show()

	sys.exit(app.exec())
