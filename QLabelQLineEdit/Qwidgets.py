from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout
import sys

class qWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel and QLineEdit Example")

        # Create a vertical layout
        v_layout = QVBoxLayout()

        # Create a horizontal layout for label and line edit
        h_layout = QHBoxLayout()

        # Create a label
        label = QLabel("Fullname:")
        h_layout.addWidget(label)

        # Submitted text
        label2 = QLabel(self.submitted_text)

        # Create a line edit
        line_edit = QLineEdit()
        h_layout.addWidget(line_edit)

        # Add the horizontal layout to the vertical layout
        v_layout.addLayout(h_layout)

        # Adding Push Button
        button = QPushButton("Submit")
        button.clicked.connect(self.submit_form)
        v_layout.addWidget(button)

    def submit_form(self):
        print("Form submitted!")