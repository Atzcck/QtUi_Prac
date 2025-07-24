from PySide6.QtWidgets import QApplication
import sys
import mainWidgets

app = QApplication(sys.argv)

window = mainWidgets.qWidget()
window.setWindowTitle("QLabel and QLineEdit Example")
window.show()

app.exec()
