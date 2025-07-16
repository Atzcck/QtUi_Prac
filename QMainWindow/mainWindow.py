from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar
import sys

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Window Title")

        # Menu and toolbar setup can be added here
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        quitAction = fileMenu.addAction(QIcon("exit-svgrepo-com.png"), "")
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

        # Toolbar Added
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Actions for the toolbar
        toolbar.addAction(quitAction)

        # Action 1
        action1 = QAction("Action 1", self)
        action1.setStatusTip("This is Action 1")
        action1.triggered.connect(self.action1_triggered)
        toolbar.addAction(action1)

        # Action 2
        action2 = QAction(QIcon("disk-svgrepo-com.png"), "Action 2", self)
        action2.setStatusTip("This is Action 2")
        action2.setCheckable(True)
        action2.triggered.connect(self.action2_triggered)
        toolbar.addAction(action2)

    def action1_triggered(self):
        print("Action 1 triggered")

    def action2_triggered(self):
        print("Action 2 triggered")

    def quit_app(self):
        self.app.quit()