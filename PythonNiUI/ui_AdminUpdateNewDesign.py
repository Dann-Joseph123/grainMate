# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminUpdateProduct1ulcCkF.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(241, 251, 249);")
        self.backBUtton = QPushButton(Form)
        self.backBUtton.setObjectName(u"backBUtton")
        self.backBUtton.setGeometry(QRect(20, 20, 61, 51))
        font1 = QFont()
        font1.setPointSize(13)
        self.backBUtton.setFont(font1)
        self.backBUtton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        icon = QIcon()
        icon.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBUtton.setIcon(icon)
        self.backBUtton.setIconSize(QSize(30, 30))
        self.backBUtton.setFlat(True)
        self.adminProduct1Label = QLabel(Form)
        self.adminProduct1Label.setObjectName(u"adminProduct1Label")
        self.adminProduct1Label.setGeometry(QRect(100, 60, 141, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.adminProduct1Label.setFont(font2)
        self.adminProduct1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductName1LineEdit = QLineEdit(Form)
        self.updateProductName1LineEdit.setObjectName(u"updateProductName1LineEdit")
        self.updateProductName1LineEdit.setGeometry(QRect(210, 100, 191, 31))
        self.updateProductName1LineEdit.setFont(font)
        self.updateProductName1LineEdit.setFrame(True)
        self.updateProductPrice1LineEdit = QLineEdit(Form)
        self.updateProductPrice1LineEdit.setObjectName(u"updateProductPrice1LineEdit")
        self.updateProductPrice1LineEdit.setGeometry(QRect(210, 140, 191, 31))
        self.updateProductPrice1LineEdit.setFont(font)
        self.adminUpdateProductName1Label = QLabel(Form)
        self.adminUpdateProductName1Label.setObjectName(u"adminUpdateProductName1Label")
        self.adminUpdateProductName1Label.setGeometry(QRect(100, 110, 111, 20))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.adminUpdateProductName1Label.setFont(font3)
        self.adminUpdateProductName1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.adminUpdateProductPrice1Label = QLabel(Form)
        self.adminUpdateProductPrice1Label.setObjectName(u"adminUpdateProductPrice1Label")
        self.adminUpdateProductPrice1Label.setGeometry(QRect(100, 150, 101, 21))
        self.adminUpdateProductPrice1Label.setFont(font)
        self.adminUpdateProductPrice1Label.setStyleSheet(u"color:rgb(30, 114, 81)")
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(670, 340, 75, 24))
        self.saveButton.setStyleSheet(u"background-color: rgb(74, 188, 150);")
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(580, 340, 75, 24))
        self.adminUpdateProductName1Label_2 = QLabel(Form)
        self.adminUpdateProductName1Label_2.setObjectName(u"adminUpdateProductName1Label_2")
        self.adminUpdateProductName1Label_2.setGeometry(QRect(100, 230, 111, 20))
        self.adminUpdateProductName1Label_2.setFont(font3)
        self.adminUpdateProductName1Label_2.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductName1LineEdit_2 = QLineEdit(Form)
        self.updateProductName1LineEdit_2.setObjectName(u"updateProductName1LineEdit_2")
        self.updateProductName1LineEdit_2.setGeometry(QRect(210, 220, 191, 31))
        self.updateProductName1LineEdit_2.setFont(font)
        self.updateProductName1LineEdit_2.setFrame(True)
        self.adminProduct1Label_2 = QLabel(Form)
        self.adminProduct1Label_2.setObjectName(u"adminProduct1Label_2")
        self.adminProduct1Label_2.setGeometry(QRect(100, 180, 141, 41))
        self.adminProduct1Label_2.setFont(font2)
        self.adminProduct1Label_2.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductPrice1LineEdit_2 = QLineEdit(Form)
        self.updateProductPrice1LineEdit_2.setObjectName(u"updateProductPrice1LineEdit_2")
        self.updateProductPrice1LineEdit_2.setGeometry(QRect(210, 260, 191, 31))
        self.updateProductPrice1LineEdit_2.setFont(font)
        self.adminUpdateProductPrice1Label_2 = QLabel(Form)
        self.adminUpdateProductPrice1Label_2.setObjectName(u"adminUpdateProductPrice1Label_2")
        self.adminUpdateProductPrice1Label_2.setGeometry(QRect(100, 270, 101, 21))
        self.adminUpdateProductPrice1Label_2.setFont(font)
        self.adminUpdateProductPrice1Label_2.setStyleSheet(u"color:rgb(30, 114, 81)")
        self.adminUpdateProductName1Label_3 = QLabel(Form)
        self.adminUpdateProductName1Label_3.setObjectName(u"adminUpdateProductName1Label_3")
        self.adminUpdateProductName1Label_3.setGeometry(QRect(420, 110, 111, 20))
        self.adminUpdateProductName1Label_3.setFont(font3)
        self.adminUpdateProductName1Label_3.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductName1LineEdit_3 = QLineEdit(Form)
        self.updateProductName1LineEdit_3.setObjectName(u"updateProductName1LineEdit_3")
        self.updateProductName1LineEdit_3.setGeometry(QRect(530, 100, 191, 31))
        self.updateProductName1LineEdit_3.setFont(font)
        self.updateProductName1LineEdit_3.setFrame(True)
        self.adminProduct1Label_3 = QLabel(Form)
        self.adminProduct1Label_3.setObjectName(u"adminProduct1Label_3")
        self.adminProduct1Label_3.setGeometry(QRect(420, 60, 141, 41))
        self.adminProduct1Label_3.setFont(font2)
        self.adminProduct1Label_3.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductPrice1LineEdit_3 = QLineEdit(Form)
        self.updateProductPrice1LineEdit_3.setObjectName(u"updateProductPrice1LineEdit_3")
        self.updateProductPrice1LineEdit_3.setGeometry(QRect(530, 140, 191, 31))
        self.updateProductPrice1LineEdit_3.setFont(font)
        self.adminUpdateProductPrice1Label_3 = QLabel(Form)
        self.adminUpdateProductPrice1Label_3.setObjectName(u"adminUpdateProductPrice1Label_3")
        self.adminUpdateProductPrice1Label_3.setGeometry(QRect(420, 150, 101, 21))
        self.adminUpdateProductPrice1Label_3.setFont(font)
        self.adminUpdateProductPrice1Label_3.setStyleSheet(u"color:rgb(30, 114, 81)")
        self.adminUpdateProductName1Label_4 = QLabel(Form)
        self.adminUpdateProductName1Label_4.setObjectName(u"adminUpdateProductName1Label_4")
        self.adminUpdateProductName1Label_4.setGeometry(QRect(420, 230, 111, 20))
        self.adminUpdateProductName1Label_4.setFont(font3)
        self.adminUpdateProductName1Label_4.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductName1LineEdit_4 = QLineEdit(Form)
        self.updateProductName1LineEdit_4.setObjectName(u"updateProductName1LineEdit_4")
        self.updateProductName1LineEdit_4.setGeometry(QRect(530, 220, 191, 31))
        self.updateProductName1LineEdit_4.setFont(font)
        self.updateProductName1LineEdit_4.setFrame(True)
        self.adminProduct1Label_4 = QLabel(Form)
        self.adminProduct1Label_4.setObjectName(u"adminProduct1Label_4")
        self.adminProduct1Label_4.setGeometry(QRect(420, 180, 141, 41))
        self.adminProduct1Label_4.setFont(font2)
        self.adminProduct1Label_4.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductPrice1LineEdit_4 = QLineEdit(Form)
        self.updateProductPrice1LineEdit_4.setObjectName(u"updateProductPrice1LineEdit_4")
        self.updateProductPrice1LineEdit_4.setGeometry(QRect(530, 260, 191, 31))
        self.updateProductPrice1LineEdit_4.setFont(font)
        self.adminUpdateProductPrice1Label_4 = QLabel(Form)
        self.adminUpdateProductPrice1Label_4.setObjectName(u"adminUpdateProductPrice1Label_4")
        self.adminUpdateProductPrice1Label_4.setGeometry(QRect(420, 270, 101, 21))
        self.adminUpdateProductPrice1Label_4.setFont(font)
        self.adminUpdateProductPrice1Label_4.setStyleSheet(u"color:rgb(30, 114, 81)")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.backBUtton.setText("")
        self.adminProduct1Label.setText(QCoreApplication.translate("Form", u"Product 1", None))
        self.updateProductName1LineEdit.setInputMask("")
        self.updateProductName1LineEdit.setText("")
        self.updateProductName1LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated name", None))
        self.updateProductPrice1LineEdit.setText("")
        self.updateProductPrice1LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated price", None))
        self.adminUpdateProductName1Label.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.adminUpdateProductPrice1Label.setText(QCoreApplication.translate("Form", u"Product Price", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.adminUpdateProductName1Label_2.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.updateProductName1LineEdit_2.setInputMask("")
        self.updateProductName1LineEdit_2.setText("")
        self.updateProductName1LineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated name", None))
        self.adminProduct1Label_2.setText(QCoreApplication.translate("Form", u"Product 2", None))
        self.updateProductPrice1LineEdit_2.setText("")
        self.updateProductPrice1LineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated price", None))
        self.adminUpdateProductPrice1Label_2.setText(QCoreApplication.translate("Form", u"Product Price", None))
        self.adminUpdateProductName1Label_3.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.updateProductName1LineEdit_3.setInputMask("")
        self.updateProductName1LineEdit_3.setText("")
        self.updateProductName1LineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated name", None))
        self.adminProduct1Label_3.setText(QCoreApplication.translate("Form", u"Product 3", None))
        self.updateProductPrice1LineEdit_3.setText("")
        self.updateProductPrice1LineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated price", None))
        self.adminUpdateProductPrice1Label_3.setText(QCoreApplication.translate("Form", u"Product Price", None))
        self.adminUpdateProductName1Label_4.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.updateProductName1LineEdit_4.setInputMask("")
        self.updateProductName1LineEdit_4.setText("")
        self.updateProductName1LineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated name", None))
        self.adminProduct1Label_4.setText(QCoreApplication.translate("Form", u"Product 4", None))
        self.updateProductPrice1LineEdit_4.setText("")
        self.updateProductPrice1LineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated price", None))
        self.adminUpdateProductPrice1Label_4.setText(QCoreApplication.translate("Form", u"Product Price", None))
    # retranslateUi

