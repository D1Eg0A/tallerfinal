from PySide6.QtWidgets import QWidget
from designs.about_ui import Ui_About

class AboutPage(QWidget, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom TableModel")
        self.setStyleSheet("background:#2D2D2D;")
