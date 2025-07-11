from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from mainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
app.exec()
