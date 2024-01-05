# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminUpdateProduct1sGksgA.ui'
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
    QSizePolicy, QSpinBox, QWidget)

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
        self.adminProduct1Label.setGeometry(QRect(210, 149, 141, 41))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.adminProduct1Label.setFont(font2)
        self.adminProduct1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.updateProductName1LineEdit = QLineEdit(Form)
        self.updateProductName1LineEdit.setObjectName(u"updateProductName1LineEdit")
        self.updateProductName1LineEdit.setGeometry(QRect(360, 199, 201, 41))
        self.updateProductName1LineEdit.setFont(font)
        self.updateProductName1LineEdit.setFrame(True)
        self.updateProductPrice1LineEdit = QLineEdit(Form)
        self.updateProductPrice1LineEdit.setObjectName(u"updateProductPrice1LineEdit")
        self.updateProductPrice1LineEdit.setGeometry(QRect(360, 259, 201, 41))
        self.updateProductPrice1LineEdit.setFont(font)
        self.adminUpdateProductName1Label = QLabel(Form)
        self.adminUpdateProductName1Label.setObjectName(u"adminUpdateProductName1Label")
        self.adminUpdateProductName1Label.setGeometry(QRect(210, 209, 131, 20))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(False)
        self.adminUpdateProductName1Label.setFont(font3)
        self.adminUpdateProductName1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.adminUpdateProductPrice1Label = QLabel(Form)
        self.adminUpdateProductPrice1Label.setObjectName(u"adminUpdateProductPrice1Label")
        self.adminUpdateProductPrice1Label.setGeometry(QRect(210, 269, 121, 21))
        font4 = QFont()
        font4.setPointSize(15)
        self.adminUpdateProductPrice1Label.setFont(font4)
        self.adminUpdateProductPrice1Label.setStyleSheet(u"color:rgb(30, 114, 81)")
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(480, 319, 75, 24))
        self.saveButton.setStyleSheet(u"background-color: rgb(74, 188, 150);")
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(390, 319, 75, 24))
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(510, 150, 51, 41))
        font5 = QFont()
        font5.setPointSize(16)
        self.spinBox.setFont(font5)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.backBUtton.setText("")
        self.adminProduct1Label.setText(QCoreApplication.translate("Form", u"Product", None))
        self.updateProductName1LineEdit.setInputMask("")
        self.updateProductName1LineEdit.setText("")
        self.updateProductName1LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated name", None))
        self.updateProductPrice1LineEdit.setText("")
        self.updateProductPrice1LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter updated price", None))
        self.adminUpdateProductName1Label.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.adminUpdateProductPrice1Label.setText(QCoreApplication.translate("Form", u"Product Price", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

