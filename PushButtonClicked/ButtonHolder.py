# importing necessary modules from PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Sys module is used to access command line arguments
import sys
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App!")
        self.button = QPushButton("Click Me", self)
        self.button.setCheckable(True)  # Make the button checkable
        self.button.clicked.connect(self.buttonClicked)  # Connect the button's clicked signal to the slot
        # Set the button as the central widget of the main window
        self.setCentralWidget(self.button)
    def buttonClicked(self):
        if self.button.isChecked():
            self.button.setText("Clicked!")
            print("Button was clicked!")
        else:            
            self.button.setText("Click Me")
        