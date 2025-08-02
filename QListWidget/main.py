from PySide6.QtWidgets import QApplication, QWidget
import sys

from ListWidget import ListWidget

app = QApplication(sys.argv)

window = ListWidget()

window.setWindowTitle("QListWidget Example")
window.show()

app.exec()
