from PySide6.QtWidgets import   QApplication, QWidget
import sys
from sizePolicyWidget import Widget

app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()