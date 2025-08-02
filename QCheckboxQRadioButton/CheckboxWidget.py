from PySide6.QtWidgets import QWidget, QCheckBox, QVBoxLayout, QGroupBox, QHBoxLayout, QButtonGroup
import sys

class CheckboxWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        os_layout = QVBoxLayout()
        drink_layout = QVBoxLayout()

        os_checkbox_group = QGroupBox("Select Your OS", self)
        drink_checkbox_group = QGroupBox("Select Your Drink", self,)

        checkbox_1 = QCheckBox("Windows")
        checkbox_2 = QCheckBox("Linux")
        checkbox_3 = QCheckBox("MacOS")

        checkbox_4 = QCheckBox("Coffee")
        checkbox_5 = QCheckBox("Tea")
        checkbox_6 = QCheckBox("Beer")
        

        drinks = QButtonGroup(self)
        drinks.addButton(checkbox_4)
        drinks.addButton(checkbox_5)
        drinks.addButton(checkbox_6)
        drinks.setExclusive(True)
        checkbox_4.setChecked(True)

        os_layout.addWidget(checkbox_1)
        os_layout.addWidget(checkbox_2)
        os_layout.addWidget(checkbox_3)

        drink_layout.addWidget(checkbox_4)
        drink_layout.addWidget(checkbox_5)
        drink_layout.addWidget(checkbox_6)

        os_checkbox_group.setLayout(os_layout)
        drink_checkbox_group.setLayout(drink_layout)

        layout = QHBoxLayout()
        layout.addWidget(os_checkbox_group)
        layout.addWidget(drink_checkbox_group)

        self.setLayout(layout)