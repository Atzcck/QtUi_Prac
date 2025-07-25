# importing necessary modules from PySide6
from PySide6.QtWidgets import QApplication, QWidget

# Sys module is used to access command line arguments
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)

# Create a basic QWidget window
window = QWidget()

# window closed default. show() method needed.
window.show()

# Start the application event loop
app.exec()