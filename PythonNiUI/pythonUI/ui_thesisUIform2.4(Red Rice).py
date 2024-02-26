# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thesisUIform2xaZsSD.ui'
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

class Ui_redRiceForm(object):
    def setupUi(self, redRiceForm):
        if not redRiceForm.objectName():
            redRiceForm.setObjectName(u"redRiceForm")
        redRiceForm.resize(800, 400)
        redRiceForm.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        self.redRiceGroupBox = QGroupBox(redRiceForm)
        self.redRiceGroupBox.setObjectName(u"redRiceGroupBox")
        self.redRiceGroupBox.setGeometry(QRect(291, 120, 431, 201))
        self.redRiceLabel = QLabel(self.redRiceGroupBox)
        self.redRiceLabel.setObjectName(u"redRiceLabel")
        self.redRiceLabel.setGeometry(QRect(30, 10, 121, 31))
        font = QFont()
        font.setPointSize(14)
        self.redRiceLabel.setFont(font)
        self.redRicePrice = QLabel(self.redRiceGroupBox)
        self.redRicePrice.setObjectName(u"redRicePrice")
        self.redRicePrice.setGeometry(QRect(30, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.redRicePrice.setFont(font1)
        self.redRiceSpinBox = QSpinBox(self.redRiceGroupBox)
        self.redRiceSpinBox.setObjectName(u"redRiceSpinBox")
        self.redRiceSpinBox.setGeometry(QRect(30, 90, 81, 41))
        self.redRiceTextEdit = QPlainTextEdit(self.redRiceGroupBox)
        self.redRiceTextEdit.setObjectName(u"redRiceTextEdit")
        self.redRiceTextEdit.setEnabled(True)
        self.redRiceTextEdit.setGeometry(QRect(290, 30, 104, 41))
        self.redRiceTextEdit.setReadOnly(True)
        self.redRiceConfirmButton = QPushButton(self.redRiceGroupBox)
        self.redRiceConfirmButton.setObjectName(u"redRiceConfirmButton")
        self.redRiceConfirmButton.setGeometry(QRect(300, 150, 91, 31))
        self.redRiceConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n"
"color: rgb(240, 240, 240);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.redRiceCancelButton = QPushButton(self.redRiceGroupBox)
        self.redRiceCancelButton.setObjectName(u"redRiceCancelButton")
        self.redRiceCancelButton.setGeometry(QRect(200, 150, 91, 31))
        self.redRiceCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(240, 240, 240);")
        self.redriceHeadLabel = QLabel(redRiceForm)
        self.redriceHeadLabel.setObjectName(u"redriceHeadLabel")
        self.redriceHeadLabel.setGeometry(QRect(350, 40, 131, 61))
        font2 = QFont()
        font2.setPointSize(24)
        self.redriceHeadLabel.setFont(font2)
        self.redriceHeadLabel.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.redRiceView = QGraphicsView(redRiceForm)
        self.redRiceView.setObjectName(u"redRiceView")
        self.redRiceView.setGeometry(QRect(90, 120, 201, 201))

        self.retranslateUi(redRiceForm)

        QMetaObject.connectSlotsByName(redRiceForm)
    # setupUi

    def retranslateUi(self, redRiceForm):
        redRiceForm.setWindowTitle(QCoreApplication.translate("redRiceForm", u"Form", None))
        self.redRiceGroupBox.setTitle("")
        self.redRiceLabel.setText(QCoreApplication.translate("redRiceForm", u"Red Rice", None))
        self.redRicePrice.setText(QCoreApplication.translate("redRiceForm", u"P 80.00 per kilogram", None))
        self.redRiceConfirmButton.setText(QCoreApplication.translate("redRiceForm", u"Confirm", None))
        self.redRiceCancelButton.setText(QCoreApplication.translate("redRiceForm", u"Cancel", None))
        self.redriceHeadLabel.setText(QCoreApplication.translate("redRiceForm", u"Red Rice", None))
    # retranslateUi

