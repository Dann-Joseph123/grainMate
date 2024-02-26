# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thesisUIform2oGDsjS.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_jasmineForm(object):
    def setupUi(self, jasmineForm):
        if not jasmineForm.objectName():
            jasmineForm.setObjectName(u"jasmineForm")
        jasmineForm.resize(800, 400)
        jasmineForm.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        self.sinandomengGroupBox = QGroupBox(jasmineForm)
        self.sinandomengGroupBox.setObjectName(u"sinandomengGroupBox")
        self.sinandomengGroupBox.setGeometry(QRect(281, 120, 431, 201))
        self.jasmineLabel = QLabel(self.sinandomengGroupBox)
        self.jasmineLabel.setObjectName(u"jasmineLabel")
        self.jasmineLabel.setGeometry(QRect(30, 10, 121, 31))
        font = QFont()
        font.setPointSize(14)
        self.jasmineLabel.setFont(font)
        self.jasminePrice = QLabel(self.sinandomengGroupBox)
        self.jasminePrice.setObjectName(u"jasminePrice")
        self.jasminePrice.setGeometry(QRect(30, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.jasminePrice.setFont(font1)
        self.jasmineSpinBox = QSpinBox(self.sinandomengGroupBox)
        self.jasmineSpinBox.setObjectName(u"jasmineSpinBox")
        self.jasmineSpinBox.setGeometry(QRect(30, 90, 81, 41))
        self.jasmineTextEdit = QPlainTextEdit(self.sinandomengGroupBox)
        self.jasmineTextEdit.setObjectName(u"jasmineTextEdit")
        self.jasmineTextEdit.setEnabled(True)
        self.jasmineTextEdit.setGeometry(QRect(290, 30, 104, 41))
        self.jasmineTextEdit.setReadOnly(True)
        self.jasmineConfirmButton = QPushButton(self.sinandomengGroupBox)
        self.jasmineConfirmButton.setObjectName(u"jasmineConfirmButton")
        self.jasmineConfirmButton.setGeometry(QRect(300, 150, 91, 31))
        self.jasmineConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n"
"color: rgb(240, 240, 240);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.jasmineCancelButton = QPushButton(self.sinandomengGroupBox)
        self.jasmineCancelButton.setObjectName(u"jasmineCancelButton")
        self.jasmineCancelButton.setGeometry(QRect(200, 150, 91, 31))
        self.jasmineCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(240, 240, 240);")
        self.jasmineView = QGraphicsView(jasmineForm)
        self.jasmineView.setObjectName(u"jasmineView")
        self.jasmineView.setGeometry(QRect(80, 120, 201, 201))
        self.jasmineHeadLabel = QLabel(jasmineForm)
        self.jasmineHeadLabel.setObjectName(u"jasmineHeadLabel")
        self.jasmineHeadLabel.setGeometry(QRect(340, 40, 131, 61))
        font2 = QFont()
        font2.setPointSize(24)
        self.jasmineHeadLabel.setFont(font2)
        self.jasmineHeadLabel.setStyleSheet(u"color: rgb(33, 123, 88);")

        self.retranslateUi(jasmineForm)

        QMetaObject.connectSlotsByName(jasmineForm)
    # setupUi

    def retranslateUi(self, jasmineForm):
        jasmineForm.setWindowTitle(QCoreApplication.translate("jasmineForm", u"Form", None))
        self.sinandomengGroupBox.setTitle("")
        self.jasmineLabel.setText(QCoreApplication.translate("jasmineForm", u"Jasmine", None))
        self.jasminePrice.setText(QCoreApplication.translate("jasmineForm", u"P 48.00 per kilogram", None))
        self.jasmineConfirmButton.setText(QCoreApplication.translate("jasmineForm", u"Confirm", None))
        self.jasmineCancelButton.setText(QCoreApplication.translate("jasmineForm", u"Cancel", None))
        self.jasmineHeadLabel.setText(QCoreApplication.translate("jasmineForm", u"Jasmine", None))
    # retranslateUi

