from PySide6.QtWidgets import QApplication, QWidget
import sys
from widget import ImageLable

app = QApplication(sys.argv)

window = ImageLable()
window.show()

app.exec()