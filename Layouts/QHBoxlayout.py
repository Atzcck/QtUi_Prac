from PySide6.QtWidgets import  QApplication
import BoxWidget
import sys

app = QApplication(sys.argv)

window = BoxWidget.BoxWidget()
window.show()
app.exec()