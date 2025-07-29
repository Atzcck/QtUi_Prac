from PySide6.QtWidgets import   QWidget, QGridLayout, QPushButton, QSizePolicy
import sys

class GridWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridWidget")

        button_1 = QPushButton("one")
        # button_1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_2 = QPushButton("two")
        # button_2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_3 = QPushButton("three")
        button_3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_4 = QPushButton("four")
        # button_4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_5 = QPushButton("five")
        # button_5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_6 = QPushButton("six")
        # button_6.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        

        g_layout = QGridLayout()
        g_layout.addWidget(button_1, 0, 0)
        g_layout.addWidget(button_2, 0, 1, 1, 2)
        g_layout.addWidget(button_3, 1, 0, 2, 1)
        g_layout.addWidget(button_4, 1, 1)
        g_layout.addWidget(button_5, 1, 2)
        g_layout.addWidget(button_6, 2, 1)

        self.setLayout(g_layout)
