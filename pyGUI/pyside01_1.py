#
## Signal-Slot of Qt. : Slot = Method,  Signal = Event, etc.
#	connect() -> emit()
#	@SLot(): for keeping performance and stability

from PySide6. QtCore import QObject, Signal, Slot

class Example(QObject):
	my_signal = Signal(str)

	@Slot(str)
	def my_slot(self, message):
		print(f"Received: {message}")

obj = Example()
obj.my_signal.connect(obj.my_slot)
obj.my_signal.emit("Hello~~")
