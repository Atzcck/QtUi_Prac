from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTabWidget, QLabel, QHBoxLayout, QLineEdit
import sys

class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget Example")

        
        
        #Information Widget
        widget_Info = QWidget()
        h_layout = QHBoxLayout()
        fullname = QLabel("Fullname")
        line_edit = QLineEdit()
        h_layout.addWidget(fullname)
        h_layout.addWidget(line_edit)
        widget_Info.setLayout(h_layout)
        

        # Buttons
        widget_buttons = QWidget()
        button_v_layout = QVBoxLayout()
        button_1 = QPushButton("Button1")
        button_2 = QPushButton("Button2")
        button_3 = QPushButton("Button3")
        button_v_layout.addWidget(button_1)
        button_v_layout.addWidget(button_2)
        button_v_layout.addWidget(button_3)
        widget_buttons.setLayout(button_v_layout)

        # TabWidget
        tab_widget = QTabWidget(self)
        tab_widget.addTab(widget_Info, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

