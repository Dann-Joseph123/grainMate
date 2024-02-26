# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminKJsXyW.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import newResource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        Form.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(310, 230, 261, 41))
        font = QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QFrame.Panel)
        self.textEdit_2 = QTextEdit(Form)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(310, 290, 261, 41))
        self.textEdit_2.setFrameShape(QFrame.Panel)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 240, 101, 21))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(32, 119, 85);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 290, 91, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(30, 112, 80);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, -120, 701, 291))
        self.label_3.setStyleSheet(u"background-image: url(:/newPrefix/ricemate.png);")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setPixmap(QPixmap(u"ricemate.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 190, 241, 21))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(31, 114, 82)")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 61, 31))
        font3 = QFont()
        font3.setPointSize(13)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/previous.png)")
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 350, 371, 24))
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.pushButton_2.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"ADMINISTRATOR MODE", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Click here for New Account", None))
    # retranslateUi

