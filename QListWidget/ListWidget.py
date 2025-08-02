from PySide6.QtWidgets import QWidget, QListWidget, QVBoxLayout, QPushButton
import sys

class ListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget Example")
        self.setGeometry(100, 100, 400, 300)

        
        
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

        self.button_1 = QPushButton("Add Item")
        self.button_1.clicked.connect(self.add_item)

        self.button_2 = QPushButton("Delete Item")
        self.button_2.clicked.connect(self.delete_item)

        self.button_3 = QPushButton("Item Count")
        self.button_3.clicked.connect(self.item_count)

        self.button_4 = QPushButton("Selected Item")
        self.button_4.clicked.connect(self.selected_items)

        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(self.button_1)
        v_layout.addWidget(self.button_2)
        v_layout.addWidget(self.button_3)
        v_layout.addWidget(self.button_4)
        self.setLayout(v_layout)

        

    def current_item_changed(self,item):
        try:
            print("Current item: ",item.text())
        except AttributeError:
            print("There is no item on list")

    def current_text_changed(self, text):
        print("Current text changed: ", text)

    def add_item(self):
        self.list_widget.addItem("New Item")

    def delete_item(self):
        for i in self.list_widget.selectedItems():
           self.list_widget.takeItem(self.list_widget.row(i))
        

    def item_count(self):
        print(self.list_widget.count())

    def selected_items(self):
        self.list = self.list_widget.selectedItems()
        for i in self.list:
            print(i.text())

        

