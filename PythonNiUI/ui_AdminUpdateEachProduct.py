# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminUpdateProduct1RBntlW.ui'
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
        Form.setStyleSheet(u"background-color: rgb(241, 251, 249);")
        self.backBUtton = QPushButton(Form)
        self.backBUtton.setObjectName(u"backBUtton")
        self.backBUtton.setGeometry(QRect(30, 20, 61, 51))
        font = QFont()
        font.setPointSize(13)
        self.backBUtton.setFont(font)
        self.backBUtton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        icon = QIcon()
        icon.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBUtton.setIcon(icon)
        self.backBUtton.setIconSize(QSize(30, 30))
        self.backBUtton.setFlat(True)
        self.adminProduct1Label = QLabel(Form)
        self.adminProduct1Label.setObjectName(u"adminProduct1Label")
        self.adminProduct1Label.setGeometry(QRect(320, 110, 141, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.adminProduct1Label.setFont(font1)
        self.adminProduct1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductName1LineEdit = QLineEdit(Form)
        self.updateProductName1LineEdit.setObjectName(u"updateProductName1LineEdit")
        self.updateProductName1LineEdit.setGeometry(QRect(460, 150, 191, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.updateProductName1LineEdit.setFont(font2)
        self.updateProductName1LineEdit.setFrame(True)
        self.updateProductPrice1LineEdit = QLineEdit(Form)
        self.updateProductPrice1LineEdit.setObjectName(u"updateProductPrice1LineEdit")
        self.updateProductPrice1LineEdit.setGeometry(QRect(460, 200, 191, 41))
        self.updateProductPrice1LineEdit.setFont(font2)
        self.adminUpdateProductName1Label = QLabel(Form)
        self.adminUpdateProductName1Label.setObjectName(u"adminUpdateProductName1Label")
        self.adminUpdateProductName1Label.setGeometry(QRect(320, 160, 141, 20))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(False)
        self.adminUpdateProductName1Label.setFont(font3)
        self.adminUpdateProductName1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.adminUpdateProductPrice1Label = QLabel(Form)
        self.adminUpdateProductPrice1Label.setObjectName(u"adminUpdateProductPrice1Label")
        self.adminUpdateProductPrice1Label.setGeometry(QRect(320, 210, 121, 21))
        font4 = QFont()
        font4.setPointSize(15)
        self.adminUpdateProductPrice1Label.setFont(font4)
        self.adminUpdateProductPrice1Label.setStyleSheet(u"color:rgb(30, 114, 81)")
        self.addImageButton = QPushButton(Form)
        self.addImageButton.setObjectName(u"addImageButton")
        self.addImageButton.setGeometry(QRect(140, 120, 151, 151))
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(570, 250, 75, 24))
        self.saveButton.setStyleSheet(u"background-color: rgb(74, 188, 150);")
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(480, 250, 75, 24))

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
        self.addImageButton.setText(QCoreApplication.translate("Form", u"Add Image Function", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

