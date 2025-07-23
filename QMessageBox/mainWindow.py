from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QMessageBox, QWidget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Window Title")
        
         # Hard way qmessage box trigger button
        buttonCustomDefMessageBox = QPushButton("Custom Defined", self)
        buttonCustomDefMessageBox.clicked.connect(self.button_clicked_custom)

         # Critical Qmessage box trigger button
        button_critical_clicked = QPushButton("Critical Message!", self)
        button_critical_clicked.clicked.connect(self.button_critical_clicked)

        # Information QMessageBox trigger button
        button_information_clicked = QPushButton("Information Message!", self)
        button_information_clicked.clicked.connect(self.button_information_clicked)

        # Warning QMessageBox trigger button
        button_warning_clicked = QPushButton("Warning Message!", self)
        button_warning_clicked.clicked.connect(self.button_warning_clicked)

        # Question QMessageBox trigger button
        button_question_clicked = QPushButton("Question Message!", self)
        button_question_clicked.clicked.connect(self.button_question_clicked)

        # About QMessageBox trigger button
        button_about_clicked = QPushButton("About Message!", self)
        button_about_clicked.clicked.connect(self.button_about_clicked)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(buttonCustomDefMessageBox)
        buttonLayout.addWidget(button_critical_clicked)
        buttonLayout.addWidget(button_information_clicked)
        buttonLayout.addWidget(button_warning_clicked)
        buttonLayout.addWidget(button_question_clicked)
        buttonLayout.addWidget(button_about_clicked)
        
        centralWidget = QWidget()
        centralWidget.setLayout(buttonLayout)
        self.setCentralWidget(centralWidget)

    def button_clicked_custom(self):
        message = QMessageBox(self)
        message.setMinimumSize(700, 500)
        message.setWindowTitle("Custom Message Box")
        message.setText("This is a custom message box.")
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("OK clicked")
        else:
            print("Cancel clicked")

    def button_critical_clicked(self):
        message = QMessageBox.critical(self, "Critical Error", "A critical error occurred!", QMessageBox.Ok | QMessageBox.Cancel)
        print("Critical message box closed with:", message)

    def button_information_clicked(self):
        message = QMessageBox.information(self, "Information", "This is an informational message.", QMessageBox.Ok | QMessageBox.Cancel)
        print("Information message box closed with:", message)

    def button_warning_clicked(self):
        message = QMessageBox.warning(self, "Warning", "This is a warning message.", QMessageBox.Ok | QMessageBox.Cancel)
        print("Warning message box closed with:", message)

    def button_question_clicked(self):
        message = QMessageBox.question(self, "Question", "Do you want to proceed?", QMessageBox.Yes | QMessageBox.No)
        print("Question message box closed with:", message)

    def button_about_clicked(self):
        message = QMessageBox.about(self, "About", "This is an about message box.")
        print("About message box closed with:", message)

        