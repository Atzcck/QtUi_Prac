from PySide6.QtWidgets import   QWidget, QGridLayout, QPushButton, QSizePolicy
import sys

class GridWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridWidget")

        button_1 = QPushButton("one")
        button_2 = QPushButton("two")
        button_3 = QPushButton("three")
        button_4 = QPushButton("four")
        button_5 = QPushButton("five")
        button_6 = QPushButton("six")
        button_7 = QPushButton("seven")

        g_layout = QGridLayout()
        

