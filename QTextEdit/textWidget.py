from PySide6.QtWidgets import QWidget, QPushButton,  QTextEdit, QHBoxLayout, QVBoxLayout
import sys

class textWidget(QWidget):
    def __init__(self):
        super.__init__()
        self.setWindowTitle("QTextWidget Application")

        text_edit = QTextEdit()

        # Copy
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_button_clicked())

        # Cut
        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.cut_button_clicked())

        # Paste
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.paste_button_clicked())

        # Undo
        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.undo_button_clicked())

        # Redo
        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.redo_button_clicked())

        # Set Plain Text
        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text_button_clicked())

        # Set HTML
        set_html_button = QPushButton("HTML")
        set_html_button.clicked.connect(self.set_html_button_clicked())

        # Clear
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_button_clicked())


        h_layout = QHBoxLayout()
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(text_edit)

    #def copy_button_clicked():
        
    #def cut_button_clicked():
        
    #def paste_button_clicked():
    
    #def undo_button_clicked():
    
    #def redo_button_clicked():
    
    #def set_plain_text_button_clicked():

    #def set_html_button_clicked():
    
    #def clear_button_clicked():


        

