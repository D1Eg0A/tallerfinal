# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
from Resources import profile_images_rc

class Ui_Profile_page(object):
    def setupUi(self, Profile_page):
        if not Profile_page.objectName():
            Profile_page.setObjectName(u"Profile_page")
        Profile_page.resize(1005, 734)
        Profile_page.setStyleSheet(u"	background:#2D2D2D;")
        self.verticalLayout = QVBoxLayout(Profile_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Profile_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 400))
        self.frame.setBaseSize(QSize(5, 1))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.data_container = QFrame(self.frame)
        self.data_container.setObjectName(u"data_container")
        self.data_container.setMinimumSize(QSize(700, 450))
        self.data_container.setStyleSheet(u"background:rgb(20,146,230);\n"
"border-radius:20px;\n"
"")
        self.data_container.setFrameShape(QFrame.StyledPanel)
        self.data_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.data_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.data_container_layout = QVBoxLayout()
        self.data_container_layout.setObjectName(u"data_container_layout")

        self.horizontalLayout_2.addLayout(self.data_container_layout)

        self.frame_7 = QFrame(self.data_container)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(270, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit = QTextEdit(self.frame_7)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.textEdit, 0, Qt.AlignVCenter)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/newPrefix/images/personal_card.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label_5, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout_3.addWidget(self.data_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Profile_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 250))
        self.frame_2.setBaseSize(QSize(1, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u":/newPrefix/images/bottom.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignBottom)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.back_button = QPushButton(self.frame_3)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(200, 50))
        self.back_button.setMaximumSize(QSize(200, 50))
        self.back_button.setStyleSheet(u"#back_button\n"
"        {\n"
"        	border:none;\n"
"        	background:rgb(20,146,230);\n"
"        	color:white;\n"
"        	border-radius:16px\n"
"        }\n"
"        \n"
"        #back_button:hover\n"
"        {\n"
"        background:rgb(20,146,230);\n"
"        background:#2D2D2D;\\n\n"
"        color:#F33253;\\n\n"
"        	border-radius:16px;\\n\n"
"        }")

        self.verticalLayout_2.addWidget(self.back_button, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/newPrefix/images/Corporate_Management.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_3)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 200))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/images/bottom right.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Profile_page)

        QMetaObject.connectSlotsByName(Profile_page)
    # setupUi

    def retranslateUi(self, Profile_page):
        Profile_page.setWindowTitle(QCoreApplication.translate("Profile_page", u"Form", None))
        self.textEdit.setHtml(QCoreApplication.translate("Profile_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">Profile</span></p></body></html>", None))
        self.label_5.setText("")
        self.label.setText("")
        self.back_button.setText(QCoreApplication.translate("Profile_page", u"Back", None))
        self.label_3.setText("")
        self.label_2.setText("")
    # retranslateUi

