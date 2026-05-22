# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import Resources.images_rc as images_rc

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.resize(1017, 774)
        mainWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_3 = QHBoxLayout(mainWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(mainWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(270, 16777215))
        self.frame.setBaseSize(QSize(245, 0))
        self.frame.setStyleSheet(u"background-color: transparent;\n"
"width:40px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Corporate_Management.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.add_button = QPushButton(self.frame)
        self.add_button.setObjectName(u"add_button")
        font = QFont()
        font.setPointSize(11)
        self.add_button.setFont(font)
        self.add_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_button.setStyleSheet(u"#add_button\n"
"{\n"
"	text-align:left;\n"
"	padding-left:20px;\n"
"	border:none;\n"
"	border-left:6px solid dodgerblue;\n"
"	color:white;	\n"
"	background:#333333;\n"
"	height:45px\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Images/icons8_Find_User_Male_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon)
        self.add_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.add_button)

        self.import_button = QPushButton(self.frame)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setFont(font)
        self.import_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_button.setStyleSheet(u"#import_button\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:rgb(31,31,31);\n"
"	height:45px\n"
"}\n"
"#import_button:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Images/icons8_Add_User_Male_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_button.setIcon(icon1)
        self.import_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.import_button)

        self.export_button = QPushButton(self.frame)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setFont(font)
        self.export_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.export_button.setStyleSheet(u"#export_button\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"	height:45px\n"
"}\n"
"#export_button:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Images/icons8_Registration_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_button.setIcon(icon2)
        self.export_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.export_button)

        self.delete_button = QPushButton(self.frame)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setFont(font)
        self.delete_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_button.setStyleSheet(u"#delete_button\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"height:45px}\n"
"#delete_button:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Images/icons8_Remove_User_Male_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon3)
        self.delete_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.delete_button)

        self.edit_button = QPushButton(self.frame)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setFont(font)
        self.edit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_button.setStyleSheet(u"#edit_button\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"	height:45px\n"
"}\n"
"#edit_button:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;	\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333333;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Images/icons8_Hand_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_button.setIcon(icon4)
        self.edit_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.edit_button)

        self.about_button = QPushButton(self.frame)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setFont(font)
        self.about_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_button.setStyleSheet(u"#about_button\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#1F1F1F;\n"
"	height:45px\n"
"}\n"
"#about_button:hover\n"
"{\n"
"	text-align:left;\n"
"	padding-left:26px;	\n"
"	border:none;	\n"
"	color:white;	\n"
"	background:#333333;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Images/icons8_Money_50px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_button.setIcon(icon5)
        self.about_button.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.about_button)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_3.addWidget(self.label_9)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(mainWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.student_data_button = QPushButton(self.frame_2)
        self.student_data_button.setObjectName(u"student_data_button")
        self.student_data_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.student_data_button.setAcceptDrops(True)
        self.student_data_button.setStyleSheet(u"#student_data_button {\n"
"	background-color: rgb(191, 49, 49);\n"
"	border:none;\n"
"	height:100%;\n"
"	border-radius: 10px ;\n"
"	color:white;\n"
"	font-weight: 700;\n"
"	font-size: 15px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.student_data_button)

        self.professor_data_button = QPushButton(self.frame_2)
        self.professor_data_button.setObjectName(u"professor_data_button")
        self.professor_data_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.professor_data_button.setStyleSheet(u"#professor_data_button{background-color:rgb(85, 124, 85);\n"
"border:none;\n"
"height:100%;\n"
"border-radius: 10px ;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 15px;\n"
"}")

        self.horizontalLayout.addWidget(self.professor_data_button)

        self.class_data_button = QPushButton(self.frame_2)
        self.class_data_button.setObjectName(u"class_data_button")
        self.class_data_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.class_data_button.setStyleSheet(u"#class_data_button{\n"
"background-color:rgb(97, 163, 186);\n"
"border:none;\n"
"height:100%;\n"
"border-radius: 10px ;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.class_data_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_label = QLabel(self.frame_3)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setStyleSheet(u"#search_label{\n"
"font-size:20px;\n"
"font-weight: 700;\n"
"font-size: 15px;\n"
"color:white;\n"
"}")

        self.horizontalLayout_2.addWidget(self.search_label)

        self.search_field = QLineEdit(self.frame_3)
        self.search_field.setObjectName(u"search_field")
        self.search_field.setStyleSheet(u"#search_field{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px ;\n"
"height:30px\n"
"}")

        self.horizontalLayout_2.addWidget(self.search_field)


        self.verticalLayout.addWidget(self.frame_3)

        self.table = QTableWidget(self.frame_2)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"#table{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QHeaderView::section{\n"
"background:rgb(31,31,31);\n"
"color:white;\n"
"border:none;\n"
"height:35px\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.table)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.retranslateUi(mainWidget)

        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"Form", None))
        self.label_2.setText("")
        self.add_button.setText(QCoreApplication.translate("mainWidget", u"Add", None))
        self.import_button.setText(QCoreApplication.translate("mainWidget", u"Import", None))
        self.export_button.setText(QCoreApplication.translate("mainWidget", u"Export", None))
        self.delete_button.setText(QCoreApplication.translate("mainWidget", u"Delete", None))
        self.edit_button.setText(QCoreApplication.translate("mainWidget", u"Edit", None))
        self.about_button.setText(QCoreApplication.translate("mainWidget", u"About App", None))
        self.label_9.setText(QCoreApplication.translate("mainWidget", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">App Version: 1.0.0</span></p></body></html>", None))
        self.student_data_button.setText(QCoreApplication.translate("mainWidget", u"Students", None))
        self.professor_data_button.setText(QCoreApplication.translate("mainWidget", u"Professors", None))
        self.class_data_button.setText(QCoreApplication.translate("mainWidget", u"Classes", None))
        self.search_label.setText(QCoreApplication.translate("mainWidget", u"Search :", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWidget", u"First Name", None))
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWidget", u"Last Name", None))
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWidget", u"Age", None))
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWidget", u"Email", None))
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWidget", u"Mobile", None))
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWidget", u"Grade", None))
    # retranslateUi

