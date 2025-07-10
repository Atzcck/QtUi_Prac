# importing necessary modules from PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Sys module is used to access command line arguments
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App!")
        button = QPushButton("Click Me")
        # Set the button as the central widget of the main window
        self.setCentralWidget(button)
