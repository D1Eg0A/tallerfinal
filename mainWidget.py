from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget, QLineEdit, QHBoxLayout, QTableWidgetItem
from designs.mainWidget_ui import Ui_mainWidget

class MainWidget(QWidget,Ui_mainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def actualizar_tabla(self, data, selected_data:str):
        num_rows = len(data)
        num_cols = len(data[0]) if num_rows > 0 else 0

        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        if num_rows > 0:
            if selected_data == "student":
                headers = ["Frist Name","Last Name","Age","Email","Mobile","Grade","Class"]  # Default headers
            elif selected_data == "professor":
                headers = ["Frist Name","Last Name","Age","Email","Mobile", "Title", "Department"]  # Default headers
            elif selected_data == "class":
                headers = ["class", "Professors", "Lecture Hall", "Time"]  # Default headers
            self.table.setHorizontalHeaderLabels(headers)

            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(col))

    def conectar_doble_click_tabla(self, callback):
        self.table.doubleClicked.connect(callback)
