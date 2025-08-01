from PySide6.QtWidgets import QApplication, QWidget
import sys

from CheckboxWidget import CheckboxWidget

app = QApplication(sys.argv)

window = CheckboxWidget()
window.show()

app.exec()
