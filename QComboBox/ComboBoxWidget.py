from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTabWidget, QLabel, QHBoxLayout, QLineEdit, QComboBox
import sys

class ComboBoxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combobox Widget Example")

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

        layout = QVBoxLayout()
        button_1 = QPushButton("Current Value")
        button_1.clicked.connect(self.current_value)
        button_2 = QPushButton("Set Value")
        button_2.clicked.connect(self.set_value)
        button_3 = QPushButton("Get Values")
        button_3.clicked.connect(self.get_values)

        

        layout.addWidget(self.combo_box)
        layout.addWidget(button_1)
        layout.addWidget(button_2)
        layout.addWidget(button_3)
        self.setLayout(layout)


    def current_value(self):
        print("Current item: ", self.combo_box.currentText(), " Current Index: ", self.combo_box.currentIndex())

    def set_value(self):
        self.combo_box.setCurrentIndex(2)

    def get_values(self):
        for i in range(self.combo_box.count()):
            print(f"index {i} : ", self.combo_box.itemText(i))


        