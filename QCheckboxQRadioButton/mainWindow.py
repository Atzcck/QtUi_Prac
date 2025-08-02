from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QSizePolicy
import sys
from CheckboxWidget import CheckboxWidget
from RadiobutWidget import RadioButtonWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckbox and QRadioButton Example")
        self.setGeometry(100, 100, 600, 400)

        check_box_widget = CheckboxWidget()
        radio_button_widget = RadioButtonWidget()

        v_layout = QVBoxLayout()
        v_layout.addWidget(check_box_widget)
        v_layout.addWidget(radio_button_widget)

        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)
