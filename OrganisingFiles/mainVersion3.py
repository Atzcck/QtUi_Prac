# importing necessary modules from PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Sys module is used to access command line arguments
import sys
import version3ButtonHolder

app = QApplication(sys.argv)
window = version3ButtonHolder.ButtonHolder()
window.show()
app.exec()