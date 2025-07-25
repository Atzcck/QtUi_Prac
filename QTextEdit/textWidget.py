from PySide6.QtWidgets import QWidget, QPushButton,  QTextEdit, QHBoxLayout, QVBoxLayout
import sys

class textWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextWidget Application")

        self.text_edit = QTextEdit()

        # Copy
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        # Cut
        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        # Paste
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)

        # Undo
        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        # Redo
        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        # Set Plain Text
        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(lambda: self.text_edit.setPlainText("lambda is needed to use this correctly. Coz function return value is None when button pressed! \n lambda calling first before function. It's make it 1 computation more iterable!"))

        # Set HTML
        set_html_button = QPushButton("HTML")
        set_html_button.clicked.connect(lambda: self.text_edit.setHtml("""<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple Page</title>
</head>
<body>
  <header>
    <h1>Welcome to My Page</h1>
  </header>

  <section>
    <p>This is the first line of content.</p>
  </section>

  <section>
    <p>This is the second line of content.</p>
  </section>

  <section>
    <p>This is the third line of content.</p>
  </section>
</body>
</html>"""))

        # Clear
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)


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
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)