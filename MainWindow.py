import sys
import csv
import os
import shutil
from profileWidget import SecondWidget
from PySide6.QtWidgets import QApplication,QFileDialog, QMainWindow, QStackedWidget, QTableWidgetItem
from PySide6.QtGui import QKeySequence,QShortcut

from mainWidget import MainWidget
from add_page import AddPage
from aboutPage import AboutPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniciar_ui()
        

    def iniciar_ui(self):
        self.setWindowTitle("Main Window")
        self.resize(1100, 800)
        self.setStyleSheet("background:#2D2D2D;")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_widget = MainWidget()
        self.second_widget = SecondWidget()
        self.add_page = AddPage()
        self.aboutPage=AboutPage()

        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.second_widget)
        self.stacked_widget.addWidget(self.aboutPage)
        self.stacked_widget.addWidget(self.add_page)

        self.main_widget.add_button.clicked.connect(self.ir_a_pagina_agregar)
        self.main_widget.delete_button.clicked.connect(self.eliminar_items_seleccionados)
        self.main_widget.edit_button.clicked.connect(self.editar_items_seleccionados)
        self.main_widget.about_button.clicked.connect(self.ir_a_pagina_acerca)
        
        self.second_widget.back_button.clicked.connect(self.cambiar_a_widget_principal)
        self.add_page.back_button.clicked.connect(self.cambiar_a_widget_principal)
        self.aboutPage.back_button.clicked.connect(self.cambiar_a_widget_principal)

        self.main_widget.student_data_button.clicked.connect(self.mostrar_datos_estudiantes)
        self.main_widget.class_data_button.clicked.connect(self.mostrar_datos_clases)
        self.main_widget.professor_data_button.clicked.connect(self.mostrar_datos_profesores)

        # Add buttons to layout

        self.main_widget.search_field.textChanged.connect(self.filtrar_tabla) 

        self.main_widget.conectar_doble_click_tabla(self.manejar_doble_click_tabla)

        self.main_widget.import_button.clicked.connect(self.importar_csv)
        self.main_widget.export_button.clicked.connect(self.exportar_csv)
        QShortcut(QKeySequence("Ctrl+I"), self).activated.connect(self.importar_csv)
        QShortcut(QKeySequence("Ctrl+E"), self).activated.connect(self.exportar_csv)

        self.main_widget.search_field.textChanged.connect(self.filtrar_tabla)
        self.current_displayed_data = None


    def ir_a_pagina_agregar(self):
        self.stacked_widget.setCurrentWidget(self.add_page)
    def ir_a_pagina_acerca(self):
        self.stacked_widget.setCurrentWidget(self.aboutPage)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Delete):
            self.eliminar_items_seleccionados()
        else:
            super().keyPressEvent(event)

    def filtrar_tabla(self, text):
        text = text.lower()  
        for row in range(self.main_widget.table.rowCount()):
            item_email = self.main_widget.table.item(row, 3)
            item_first_name = self.main_widget.table.item(row, 0)
            item_last_name = self.main_widget.table.item(row, 1)
            if item_email or item_first_name or item_last_name:  
                email_text = item_email.text().lower()
                first_name_text = item_first_name.text().lower()
                last_name_text = item_last_name.text().lower()
                # Check if the search text is present in any of the cell texts
                if text in email_text or text in first_name_text or text in last_name_text:  
                # Show the row if it matches the search text
                    self.main_widget.table.setRowHidden(row, False)  
                else:
                    self.main_widget.table.setRowHidden(row, True)

    def importar_csv(self):
        data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
        # file_path = os.path.join(data_dir, file_name)
        if self.current_displayed_data == "student":
            data_file_path = os.path.join(data_dir, "student.csv")
        elif self.current_displayed_data == "professor": 
            data_file_path = os.path.join(data_dir, "profs.csv")
        elif self.current_displayed_data == "class": 
            data_file_path = os.path.join(data_dir, "classes.csv")

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                file_path = file_paths[0]
                with open(file_path, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    data = list(reader)
                    with open(data_file_path, 'a', newline='') as data_file:
                        writer = csv.writer(data_file)
                        
                        if data and data[0]:
                            data = data[1:]
                        writer.writerows(data)

    def exportar_csv(self):
        # Allow the user to choose the export path
        file_dialog = QFileDialog()
        exported_file, _ = file_dialog.getSaveFileName(self, 'Save CSV File', '', 'CSV Files (*.csv)')
        # Check if the user canceled the dialog
        if not exported_file:
            return
        # Read the CSV file (replace this with your own data processing)
        if self.current_displayed_data == "student":
            file_name = "student.csv"
        elif self.current_displayed_data == "professor":
            file_name = "profs.csv"  
        elif self.current_displayed_data == "class":
            file_name = "classes.csv" 
        else:
            return
        data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
        file_path = os.path.join(data_dir, file_name)
        shutil.copyfile(file_path, exported_file)

    def manejar_doble_click_tabla(self, index):
        row = index.row()
        num_columns = self.main_widget.table.columnCount()
        first_name_item = self.main_widget.table.item(row, 0)
        last_name_item = self.main_widget.table.item(row, 1)

        if first_name_item is None or last_name_item is None:
            return
        
        row_data = {}
        for col in range(num_columns):
            header_text = self.main_widget.table.horizontalHeaderItem(col).text()
            item_text = self.main_widget.table.item(row, col).text()
            row_data[header_text] = item_text

        # Update the profile in the SecondWidget
        self.second_widget.actualizar_perfil(row_data)
        if self.current_displayed_data == "class":
            student_data = self.cargar_datos_desde_csv("student.csv")
            self.second_widget.actualizar_tabla_perfil(student_data, row_data['class'])
        self.stacked_widget.setCurrentWidget(self.second_widget)
        
    def mostrar_datos_estudiantes(self):
        # Load and display student data
        student_data = self.cargar_datos_desde_csv("student.csv")
        self.main_widget.actualizar_tabla(student_data, "student")
        self.current_displayed_data = "student"

    def mostrar_datos_clases(self):
        # Load and display class data
        class_data = self.cargar_datos_desde_csv("classes.csv")
        self.main_widget.actualizar_tabla(class_data, "class")
        self.current_displayed_data = "class"

    def mostrar_datos_profesores(self):
        # Load and display professor data
        professor_data = self.cargar_datos_desde_csv("profs.csv")
        self.main_widget.actualizar_tabla(professor_data, "professor")
        self.current_displayed_data = "professor"

    def cargar_datos_desde_csv(self, file_name):
        # Load data from CSV file
        data = []
        data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
        file_path = os.path.join(data_dir, file_name)
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
        return data
    
    
    
    def eliminar_items_seleccionados(self):
        selected_items = self.main_widget.table.selectedItems()
        if selected_items:
            rows_to_delete = set()
            for item in selected_items:
                rows_to_delete.add(item.row())
            rows_to_delete = sorted(rows_to_delete, reverse=True)
            for row in rows_to_delete:
                self.main_widget.table.removeRow(row)
            self.guardar_tabla_en_csv()

    def editar_items_seleccionados(self):
        selected_items = self.main_widget.table.selectedItems()
        if selected_items:
            data = []
            num_cols = self.main_widget.table.columnCount()
            for item in selected_items:
                row_index = item.row()
                col_index = item.column()
                cell_data = item.text()
                data.append((row_index, col_index, cell_data))

            for row_index, col_index, cell_data in data:
                self.main_widget.table.setItem(row_index, col_index, QTableWidgetItem(cell_data))

            self.guardar_tabla_en_csv()

    def guardar_tabla_en_csv(self):
        num_cols = self.main_widget.table.columnCount()
        if self.current_displayed_data == "student":  
            file_name = "student.csv"
        elif self.current_displayed_data == "professor":
            file_name = "profs.csv"
        elif self.current_displayed_data == "class":  
            file_name = "classes.csv"
        else:
            print("Unknown data type")
            return

        # current_dir = 
        data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
        file_path = os.path.join(data_dir, file_name)

        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            num_rows = self.main_widget.table.rowCount()
            for row in range(num_rows):
                row_data = []
                for col in range(num_cols):
                    item = self.main_widget.table.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  # Empty cell
                writer.writerow(row_data)

    def cambiar_a_widget_segundo(self):
        self.stacked_widget.setCurrentWidget(self.second_widget)
    
    def cambiar_a_widget_principal(self):
        self.stacked_widget.setCurrentWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
