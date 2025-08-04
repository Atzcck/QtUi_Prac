from PySide6.QtWidgets import QApplication, QWidget
import sys

from ComboBoxWidget import ComboBoxWidget

app = QApplication(sys.argv)

window = ComboBoxWidget()
window.show()

app.exec()