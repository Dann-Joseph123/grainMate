# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thesisUIform2Kcecrv.ui'
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

class Ui_sinandomengForm(object):
    def setupUi(self, sinandomengForm):
        if not sinandomengForm.objectName():
            sinandomengForm.setObjectName(u"sinandomengForm")
        sinandomengForm.resize(800, 400)
        sinandomengForm.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        self.label = QLabel(sinandomengForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 40, 211, 61))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.sinandomengGroupBox = QGroupBox(sinandomengForm)
        self.sinandomengGroupBox.setObjectName(u"sinandomengGroupBox")
        self.sinandomengGroupBox.setGeometry(QRect(281, 120, 431, 201))
        self.sinandomengLabel = QLabel(self.sinandomengGroupBox)
        self.sinandomengLabel.setObjectName(u"sinandomengLabel")
        self.sinandomengLabel.setGeometry(QRect(30, 10, 121, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.sinandomengLabel.setFont(font1)
        self.sinandomengPrice = QLabel(self.sinandomengGroupBox)
        self.sinandomengPrice.setObjectName(u"sinandomengPrice")
        self.sinandomengPrice.setGeometry(QRect(30, 40, 171, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.sinandomengPrice.setFont(font2)
        self.sinandomengSpinBox = QSpinBox(self.sinandomengGroupBox)
        self.sinandomengSpinBox.setObjectName(u"sinandomengSpinBox")
        self.sinandomengSpinBox.setGeometry(QRect(30, 90, 81, 41))
        self.sinandomengTextEdit = QPlainTextEdit(self.sinandomengGroupBox)
        self.sinandomengTextEdit.setObjectName(u"sinandomengTextEdit")
        self.sinandomengTextEdit.setEnabled(True)
        self.sinandomengTextEdit.setGeometry(QRect(290, 30, 104, 41))
        self.sinandomengTextEdit.setReadOnly(True)
        self.sinandomengConfirmButton = QPushButton(self.sinandomengGroupBox)
        self.sinandomengConfirmButton.setObjectName(u"sinandomengConfirmButton")
        self.sinandomengConfirmButton.setGeometry(QRect(300, 150, 91, 31))
        self.sinandomengConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n"
"color: rgb(240, 240, 240);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.sinandomengCancelButton = QPushButton(self.sinandomengGroupBox)
        self.sinandomengCancelButton.setObjectName(u"sinandomengCancelButton")
        self.sinandomengCancelButton.setGeometry(QRect(200, 150, 91, 31))
        self.sinandomengCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(240, 240, 240);")
        self.sinandomengView = QGraphicsView(sinandomengForm)
        self.sinandomengView.setObjectName(u"sinandomengView")
        self.sinandomengView.setGeometry(QRect(80, 120, 201, 201))

        self.retranslateUi(sinandomengForm)

        QMetaObject.connectSlotsByName(sinandomengForm)
    # setupUi

    def retranslateUi(self, sinandomengForm):
        sinandomengForm.setWindowTitle(QCoreApplication.translate("sinandomengForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("sinandomengForm", u"Sinandomeng", None))
        self.sinandomengGroupBox.setTitle("")
        self.sinandomengLabel.setText(QCoreApplication.translate("sinandomengForm", u"Sinandomeng", None))
        self.sinandomengPrice.setText(QCoreApplication.translate("sinandomengForm", u"P 45.00 per kilogram", None))
        self.sinandomengConfirmButton.setText(QCoreApplication.translate("sinandomengForm", u"Confirm", None))
        self.sinandomengCancelButton.setText(QCoreApplication.translate("sinandomengForm", u"Cancel", None))
    # retranslateUi

