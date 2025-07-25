from PySide6.QtWidgets import   QApplication, QWidget
import sys
import textWidget

app = QApplication(sys.argv)

window = textWidget.textWidget()
window.show()

app.exec()