from PySide6.QtWidgets import   QApplication, QWidget
import sys
from GridWidget import GridWidget

app = QApplication(sys.argv)

window = GridWidget()
window.show()

app.exec()