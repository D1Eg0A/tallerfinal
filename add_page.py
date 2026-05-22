from PySide6.QtWidgets import QWidget, QVBoxLayout,QHBoxLayout, QLabel, QLineEdit, QPushButton,QMessageBox
from PySide6.QtGui import QIntValidator,QValidator
from PySide6.QtCore import  Qt
import csv
import os
import re
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
from designs.addPage_ui import Ui_Form


class AddPage(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.iniciar_ui()

    def iniciar_ui(self):
        # self.layout = QVBoxLayout()

        # self.boton_estudiante = QPushButton("Student", self)
        # self.boton_profesor = QPushButton("Professor", self)
        # self.boton_clase = QPushButton("Class", self)
        # self.boton_guardar = QPushButton("Save", self)

        self.student_button.clicked.connect(self.mostrar_campos_estudiantes)
        self.professor_button.clicked.connect(self.mostrar_campos_profesores)
        self.class_button.clicked.connect(self.mostrar_campos_clases)
        self.save_button.clicked.connect(self.guardar_en_csv)

        # buttons_box = QHBoxLayout()
        # buttons_box.addWidget(self.student_button,0,Qt.AlignHCenter)
        # buttons_box.addWidget(self.professor_button,0,Qt.AlignHCenter)
        # buttons_box.addWidget(self.class_button,0,Qt.AlignHCenter)
        # self.layout.addLayout(buttons_box)

        caja_entrada = QHBoxLayout()
        self.etiqueta_nombre_clase = QLabel("Class Name:", self)
        self.campo_nombre_clase = QLineEdit(self)
        self.set_style(self.etiqueta_nombre_clase,self.campo_nombre_clase)
        caja_entrada.addWidget(self.etiqueta_nombre_clase)
        caja_entrada.addWidget(self.campo_nombre_clase)
        self.data_box.addLayout(caja_entrada)

        # Additional fields for students
        self.campos_estudiantes = [
            {"label": QLabel("First Name:", self), "field": QLineEdit()},
            {"label": QLabel("Last Name:", self), "field": QLineEdit()},
            {"label": QLabel("Age:", self), "field": QLineEdit()},
            {"label": QLabel("Mobile:", self), "field": QLineEdit()},
            {"label": QLabel("Email: ", self), "field": QLineEdit()},
            {"label": QLabel("Grade:", self), "field": QLineEdit()}
        ]

        self.campos_profesores = [
            {"label": QLabel("First Name:", self), "field": QLineEdit()},
            {"label": QLabel("Last Name:", self), "field": QLineEdit()},
            {"label": QLabel("Age:", self), "field": QLineEdit()},
            {"label": QLabel("Mobile:", self), "field": QLineEdit()},
            {"label": QLabel("Email: ", self), "field": QLineEdit()},
            {"label": QLabel("Title:", self), "field": QLineEdit()},
            {"label": QLabel("Department:", self), "field": QLineEdit()}
        ]

        self.campos_clases = [
            {"label": QLabel("Class:", self), "field": QLineEdit()},
            {"label": QLabel("Professors:", self), "field": QLineEdit()},
            {"label": QLabel("Lecture Hall:", self), "field": QLineEdit()},
            {"label": QLabel("Time:", self), "field": QLineEdit()},
        ]

        for field in self.campos_estudiantes:
            caja_entrada=QHBoxLayout()
            caja_entrada.addWidget(field["label"])
            caja_entrada.addWidget(field["field"],0,Qt.AlignVCenter)
            self.set_style(field["label"],field["field"])
            self.data_box.addLayout(caja_entrada)
        
        for field in self.campos_profesores:
            caja_entrada=QHBoxLayout()
            caja_entrada.addWidget(field["label"])
            caja_entrada.addWidget(field["field"],0,Qt.AlignVCenter)
            self.set_style(field["label"],field["field"])

            self.data_box.addLayout(caja_entrada)

        for field in self.campos_clases:
            caja_entrada=QHBoxLayout()
            caja_entrada.addWidget(field["label"])
            caja_entrada.addWidget(field["field"],0,Qt.AlignVCenter)
            self.set_style(field["label"],field["field"])

            self.data_box.addLayout(caja_entrada)

        # self.layout.addWidget(self.save_button,0,Qt.AlignHCenter)

        # self.back_button = QPushButton("Back", self)
        # self.layout.addWidget(self.back_button,0,Qt.AlignHCenter)

        # self.setLayout(self.layout)
        
        self.mostrar_campos_estudiantes()

        self.validador_edad = QIntValidator(self)
        self.validador_edad.setBottom(0)  # Age should be a positive integer
        self.campos_profesores[2]["field"].setValidator(self.validador_edad)
        self.campos_estudiantes[2]["field"].setValidator(self.validador_edad)
        
        self.validador_celular = QIntValidator(self)
        self.validador_celular.setBottom(0)  # Mobile number should be positive
        self.campos_estudiantes[3]["field"].setValidator(self.validador_celular)
        self.campos_profesores[3]["field"].setValidator(self.validador_celular)

        
    def set_style(self,label,field):
        label.setObjectName(u"label")
        label.setStyleSheet(u"#label\n"
        "{\n"
        "	border:none;\n"
        "	color:white;\n"
        "	font-size:18px;\n"
        "	font-weight:600;\n"
        "}\n"
        )
        
        field.setObjectName(u"field")
        field.setMinimumSize(QSize(800, 40))
        field.setMaximumSize(QSize(800, 40))
        field.setStyleSheet(u"#field\n"
        "{\n"
        "	border:none;\n"
        "	background-color:white;\n"
        "	color:black;\n"
        "	border-radius:10px;\n"
        "	font-size:18px;\n"
        "	font-weight:600;\n"
        "}\n"
        )

    def mostrar_campos_estudiantes(self):
        self.ocultar_todos_los_campos()
        for field in self.campos_estudiantes:
            field["field"].show()
            field["label"].show()
        self.etiqueta_nombre_clase.show()
        self.campo_nombre_clase.show()

    def mostrar_campos_profesores(self):
        self.ocultar_todos_los_campos()
        for field in self.campos_profesores:
            field["field"].show()
            field["label"].show()

    def mostrar_campos_clases(self):
        self.ocultar_todos_los_campos()
        for field in self.campos_clases:
            field["field"].show()
            field["label"].show()


    def ocultar_todos_los_campos(self):
        for field in self.campos_estudiantes + self.campos_profesores + self.campos_clases:
            field["field"].hide()
            field["label"].hide()
        self.etiqueta_nombre_clase.hide()
        self.campo_nombre_clase.hide()

    def clear_fields(self):
        for field in self.campos_estudiantes + self.campos_profesores + self.campos_clases:
            field["field"].clear()
        self.campo_nombre_clase.clear()

    def guardar_en_csv(self):
        # self.submit()
        nombre = self.campos_estudiantes[0]["field"].text()
        apellido = self.campos_estudiantes[1]["field"].text()
        edad = self.campos_estudiantes[2]["field"].text()
        celular = self.campos_estudiantes[3]["field"].text()
        correo = self.campos_estudiantes[4]["field"].text()
        grado = self.campos_estudiantes[5]["field"].text()
        nombre_clase = self.campo_nombre_clase.text()

        nombre_prof = self.campos_profesores[0]["field"].text()
        apellido_prof = self.campos_profesores[1]["field"].text()
        edad_prof = self.campos_profesores[2]["field"].text()
        celular_prof = self.campos_profesores[3]["field"].text()
        correo_prof = self.campos_profesores[4]["field"].text()
        titulo = self.campos_profesores[5]["field"].text()
        departamento = self.campos_profesores[6]["field"].text()

        clase_dato = self.campos_clases[0]["field"].text()
        profesores = self.campos_clases[1]["field"].text()
        aula = self.campos_clases[2]["field"].text()
        hora = self.campos_clases[3]["field"].text()


        if grado:
            data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            file_path = os.path.join(data_dir, "student.csv")

            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([nombre, apellido, edad, correo,celular, grado, nombre_clase])
                
                self.campo_nombre_clase.clear()
                for field in self.campos_estudiantes:
                    field["field"].clear()
        elif title :
            data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            file_path = os.path.join(data_dir, "profs.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([nombre_prof,apellido_prof,edad_prof, correo_prof,celular_prof, titulo, departamento])
                
                self.campo_nombre_clase.clear()
                for field in self.campos_profesores:
                    field["field"].clear()
        elif hall:
            data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
            file_path = os.path.join(data_dir, "classes.csv")
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([clase_dato, profesores, aula, hora])
                
                self.campo_nombre_clase.clear()
                for field in self.campos_clases:
                    field["field"].clear()
        else:
            QMessageBox.information(self," Not enough Args ", "Please fill the fields")
    

