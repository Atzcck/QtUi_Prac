from PySide6.QtWidgets import QHBoxLayout, QSlider, QLabel, QWidget, QPushButton
import sys

class BoxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoxWidget Example")

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)
