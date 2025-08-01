from PySide6.QtWidgets import QWidget, QRadioButton, QVBoxLayout, QGroupBox
import sys

class RadioButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        radio_1 = QRadioButton("Option 1")
        radio_2 = QRadioButton("Option 2")
        radio_3 = QRadioButton("Option 3")
        
        layout = QVBoxLayout()
        layout.addWidget(radio_1)
        layout.addWidget(radio_2)
        layout.addWidget(radio_3)

        radio_button_group = QGroupBox("Select an Option", self)
        radio_button_group.setLayout(layout)

        
        
       