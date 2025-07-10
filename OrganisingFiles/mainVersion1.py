# Version 1: Setting everything in one file.

# importing necessary modules from PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Sys module is used to access command line arguments
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create a basic QWidget window
window = QMainWindow()
window.setWindowTitle("My First PySide6 App")

button = QPushButton("Click Me")

window.setCentralWidget(button)

# window closed default. show() method needed.
window.show()

# Start the application event loop
app.exec()