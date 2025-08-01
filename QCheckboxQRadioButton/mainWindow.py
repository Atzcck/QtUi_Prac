from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout
import sys
from CheckboxWidget import CheckboxWidget
from RadiobutWidget import RadiobutWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckbox and QRadioButton Example")

        v_layoput = QVBoxLayout()
        h_layout = QHBoxLayout()

        # OS Selection Widget
        self.checkbox_widget = CheckboxWidget()

        # ABC Selection Widget
        self.radiobut_widget = RadiobutWidget()

        self.setLayout(v_layoput)

    
