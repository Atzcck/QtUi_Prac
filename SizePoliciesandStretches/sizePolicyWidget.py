from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QLineEdit
import sys

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Size Policies and Streches")

        label       = QLabel("Some Text: ")
        line_edit   = QLineEdit() 

        label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        v_layout = QVBoxLayout()

        h_layout1.addWidget(label)
        h_layout1.addWidget(line_edit)
        h_layout2.addWidget(button_1,2)
        h_layout2.addWidget(button_2,1)
        h_layout2.addWidget(button_3,1)

        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)

        self.setLayout(v_layout)