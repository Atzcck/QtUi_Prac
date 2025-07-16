from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QToolBar
import sys

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Window Title")

        # Menu and toolbar setup can be added here
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        quitAction = fileMenu.addAction("Quit")
        quitAction.triggered.connect(self.quit_app)
        #fileMenu.addAction("Exit", self.close)

        editMenu = menuBar.addMenu("Edit")
        editMenu.addAction("Cut")
        editMenu.addAction("Copy")
        editMenu.addAction("Paste")
        editMenu.addAction("Undo")
        editMenu.addAction("Redo")  

        windowMenu = menuBar.addMenu("Window")
        settingsMenu = menuBar.addMenu("Settings")
        helpMenu = menuBar.addMenu("Help")

        
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        


    def quit_app(self):
        self.app.quit()