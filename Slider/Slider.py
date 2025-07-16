from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
import sys

def respond_to_slider(data):
    print("Slider value changed:", data)

app = QApplication(sys.argv)
Slider = QSlider(Qt.Horizontal)
Slider.setMinimum(1)
Slider.setMaximum(100)
Slider.setValue(25)
Slider.valueChanged.connect(respond_to_slider)
Slider.show()
app.exec()