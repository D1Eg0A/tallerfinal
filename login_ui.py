# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 781, 541))
        self.widget.setCursor(QCursor(Qt.ArrowCursor))
        self.widget.setStyleSheet(u"background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                             stop: 0 rgba(10,10,10,255), stop: 1 rgba(150,150,50,255));\n"
"")
        self.user_form = QLineEdit(self.widget)
        self.user_form.setObjectName(u"user_form")
        self.user_form.setGeometry(QRect(250, 190, 261, 51))
        self.password_form = QLineEdit(self.widget)
        self.password_form.setObjectName(u"password_form")
        self.password_form.setGeometry(QRect(250, 310, 261, 51))
        self.login_label = QLabel(self.widget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(330, 80, 131, 51))
        self.login_label.setStyleSheet(u"font-size:25pt;\n"
"font-weight:bold;\n"
"color:white;\n"
"background-color:rgba(255,255,255,0)")
        self.user_label = QLabel(self.widget)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(250, 170, 91, 16))
        self.user_label.setStyleSheet(u"color:white;\n"
"font-size:10pt;\n"
"background-color:rgba(255,255,255,0)")
        self.password_label = QLabel(self.widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(250, 290, 81, 16))
        self.password_label.setStyleSheet(u"color:white;\n"
"font-size:10pt;\n"
"background-color:rgba(255,255,255,0)")
        self.submit_PushButton = QPushButton(self.widget)
        self.submit_PushButton.setObjectName(u"submit_PushButton")
        self.submit_PushButton.setGeometry(QRect(300, 410, 141, 41))
        self.submit_PushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_PushButton.setStyleSheet(u"color:black;\n"
"font: 8pt \"MS Sans Serif\";\n"
"background-color:rgba(255,255,0,255);\n"
"font-size:15pt;\n"
"font-weight:bold;\n"
"padding-left:2%;\n"
"padding-right:2%;\n"
"padding-top:5%;\n"
"padding-bottom:5%;\n"
"border-radius:10;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.user_form.setText("")
        self.password_form.setText("")
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.submit_PushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

