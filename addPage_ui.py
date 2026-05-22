# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1100, 712)
        Form.setStyleSheet(u"background-color: #2d2d2d;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.student_button = QPushButton(self.frame)
        self.student_button.setObjectName(u"student_button")
        self.student_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.student_button.setAcceptDrops(True)
        self.student_button.setStyleSheet(u"#student_button {\n"
"	background-color: rgb(191, 49, 49);\n"
"	border:none;\n"
"	height:100%;\n"
"	border-radius: 10px ;\n"
"	color:white;\n"
"	font-weight: 700;\n"
"	font-size: 15px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.student_button, 0, Qt.AlignTop)

        self.professor_button = QPushButton(self.frame)
        self.professor_button.setObjectName(u"professor_button")
        self.professor_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.professor_button.setStyleSheet(u"#professor_button{background-color:rgb(85, 124, 85);\n"
"border:none;\n"
"height:100%;\n"
"border-radius: 10px ;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 15px;\n"
"}")

        self.horizontalLayout.addWidget(self.professor_button, 0, Qt.AlignTop)

        self.class_button = QPushButton(self.frame)
        self.class_button.setObjectName(u"class_button")
        self.class_button.setMaximumSize(QSize(16777215, 150))
        self.class_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.class_button.setStyleSheet(u"#class_button{\n"
"background-color:rgb(97, 163, 186);\n"
"border:none;\n"
"height:100%;\n"
"border-radius: 10px ;\n"
"color:white;\n"
"font-weight: 700;\n"
"font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.class_button, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame)

        self.frame_7 = QFrame(Form)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.add_fields_box = QFrame(self.frame_7)
        self.add_fields_box.setObjectName(u"add_fields_box")
        self.add_fields_box.setStyleSheet(u"background-color: black;\n"
"border-radius:25px;")
        self.add_fields_box.setFrameShape(QFrame.StyledPanel)
        self.add_fields_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.add_fields_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.add_fields_box)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 0))
        self.frame_4.setMaximumSize(QSize(100, 16777215))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.data_box = QVBoxLayout()
        self.data_box.setObjectName(u"data_box")

        self.horizontalLayout_4.addLayout(self.data_box)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.add_fields_box)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.save_button = QPushButton(self.frame_3)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(200, 40))
        self.save_button.setMaximumSize(QSize(200, 100))
        font = QFont()
        font.setPointSize(11)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet(u"#save_button\n"
"{\n"
"	border:none;\n"
"	background:#F33253;\n"
"	color:white;\n"
"	border-radius:16px;\n"
"}\n"
"\n"
"#save_button:hover\n"
"{\n"
"	border:2px solid #F33253;\n"
"	background:#2D2D2D;\n"
"	color:#F33253;\n"
"	border-radius:16px;\n"
"}")

        self.verticalLayout_2.addWidget(self.save_button, 0, Qt.AlignHCenter)

        self.back_button = QPushButton(self.frame_3)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(200, 40))
        self.back_button.setMaximumSize(QSize(200, 100))
        self.back_button.setFont(font)
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

        self.verticalLayout_2.addWidget(self.back_button, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.student_button.setText(QCoreApplication.translate("Form", u"Students", None))
        self.professor_button.setText(QCoreApplication.translate("Form", u"Professors", None))
        self.class_button.setText(QCoreApplication.translate("Form", u"Classes", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"Save", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"Back", None))
    # retranslateUi

