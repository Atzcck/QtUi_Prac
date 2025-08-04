from PySide6.QtWidgets import QApplication, QWidget
import sys

from TabWidget import TabWidget

app = QApplication(sys.argv)

window = TabWidget()
window.show()

app.exec()