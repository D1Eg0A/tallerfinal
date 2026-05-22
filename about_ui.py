# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from Resources import images_about_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(1250, 706)
        About.setStyleSheet(u"#About\n"
"{\n"
"	background:#2D2D2D;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(About)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(About)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 201, 201))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/images/top_left.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(About)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(400, 150))
        self.label_5.setPixmap(QPixmap(u":/newPrefix/Corporate_Management.png"))
        self.label_5.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)

        self.verticalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_15.setFont(font1)

        self.verticalLayout.addWidget(self.label_15)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setMinimumSize(QSize(800, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"color:#fff;\n"
"border:none;\n"
"background:#2D2D2D;")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textEdit)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.back_button = QPushButton(self.frame)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(150, 40))
        self.back_button.setMaximumSize(QSize(150, 100))
        font3 = QFont()
        font3.setPointSize(11)
        self.back_button.setFont(font3)
        self.back_button.setStyleSheet(u"#back_button\n"
"{\n"
"	border:none;\n"
"	background:#F33253;\n"
"	color:white;\n"
"	border-radius:16px;\n"
"}\n"
"\n"
"#back_button:hover\n"
"{\n"
"	border:2px solid #F33253;\n"
"	background:#2D2D2D;\n"
"	color:#F33253;\n"
"	border-radius:16px;\n"
"}")

        self.verticalLayout.addWidget(self.back_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(About)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 200, 211))
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(200, 16777215))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/images/top_right.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"Form", None))
        self.label_2.setText("")
        self.label_5.setText("")
        self.label_14.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">School managment system</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("About", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">About</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Our school management system, powered by Python and Qt, represents a culmination of advanced data structures and modern user interface design. This application seamlessly integrates the efficiency of Python's data structures with the intuitive interface provided by the Qt framework, offering a robust platform for managing various aspects of school opera"
                        "tions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; font-weight:600; color:#ffffff;\">Features of this app</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\">1) Clean and User Friendly Interface</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\">2) Record can be searched/viewed just by double click</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\">3) import/export data files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Goth"
                        "ic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\">4) Insert/Update/Delete record just by few clicks</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\">This project is developed under the supervision of </span><spa"
                        "n style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; font-weight:600; color:#ffffff;\">Meza team</span><span style=\" font-family:'q_serif,Georgia,Times,Times New Roman,Hiragino Kaku Gothic Pro,Meiryo,serif'; font-size:12pt; color:#ffffff;\">.</span></p></body></html>", None))
        self.back_button.setText(QCoreApplication.translate("About", u"Back", None))
        self.label_4.setText("")
    # retranslateUi

