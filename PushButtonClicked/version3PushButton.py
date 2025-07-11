# importing necessary modules from PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Sys module is used to access command line arguments
import sys
import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder.ButtonHolder()

window.show()
app.exec()