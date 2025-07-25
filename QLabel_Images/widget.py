from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
import sys

class ImageLable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This Widget shows Image as a QLable")

        lable = QLabel()
        lable.setPixmap(QPixmap("images/rubberduck.png"))

        v_layout = QVBoxLayout()
        v_layout.addWidget(lable)
        self.setLayout(v_layout)



