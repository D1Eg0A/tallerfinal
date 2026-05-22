from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget, QLineEdit, QTableWidget, QHBoxLayout, QTableWidgetItem
from designs.profile_page_ui import Ui_Profile_page


class SecondWidget(QWidget,Ui_Profile_page):
    def __init__(self):
        super().__init__()
        # self.init_ui()
        self.setupUi(self)

    # def init_ui(self):
    #     pass

    def actualizar_perfil(self, profile_data):
        # # Clear previous labels
        # for i in reversed(range(self.layout().count()-1)):
        #     widget = self.layout().itemAt(i).widget()
        #     if widget:
        #         widget.deleteLater()
        self.limpiar_disposicion(self.data_container_layout)

        # Add new labels for each header-value pair
        for header, value in profile_data.items():
            label_text = f"{header}: {value}"
            label = QLabel(label_text)
            self.establecer_estilo(label)
            self.data_container_layout.addWidget(label)

    def establecer_estilo(self,label):
        label.setObjectName(u"label")
        label.setStyleSheet(u"#label\n"
        "{\n"
        "color:white;\n"
        "font-size: 15px;\n"
        "font-weight: 700;\n"
        "}\n")

    def limpiar_disposicion(self ,layout):
        # while layout.count():
        for i in reversed(range(layout.count()-1)):
            item = layout.takeAt(i).widget()
            if item:
                item.deleteLater()


    def actualizar_tabla_perfil(self, data, name:str):
        num_rows = len(data)
        num_cols = 2

        self.table = QTableWidget(self)
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)

        if num_rows > 0:
            headers = ["Name", "Grade"]
            self.table.setHorizontalHeaderLabels(headers)
            rows_to_delete = []
            for i, row in enumerate(data):
                if row[6] == name:
                    self.table.setItem(i, 0, QTableWidgetItem(f'{row[0]} {row[1]}'))
                    self.table.setItem(i, 1, QTableWidgetItem(row[5]))
                else:
                    rows_to_delete.append(i)
            for i in range(len(rows_to_delete)):
                    self.table.removeRow(rows_to_delete[-1])
                    rows_to_delete.pop()
        
        self.data_container_layout.insertWidget(self.layout().count() - 1, self.table)