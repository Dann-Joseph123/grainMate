# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thesisUIformUnpaidOrPaidxwEwJP.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(800, 400)
        Form.setMouseTracking(True)
        Form.setTabletTracking(True)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(110, 10, 581, 361))
        self.orderSummaryLabel = QLabel(self.groupBox)
        self.orderSummaryLabel.setObjectName(u"orderSummaryLabel")
        self.orderSummaryLabel.setGeometry(QRect(50, 50, 261, 51))
        font = QFont()
        font.setPointSize(26)
        self.orderSummaryLabel.setFont(font)
        self.totalLabel = QLabel(self.groupBox)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setGeometry(QRect(60, 120, 91, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.totalLabel.setFont(font1)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(350, 110, 181, 61))
        font2 = QFont()
        font2.setPointSize(22)
        self.textEdit.setFont(font2)
        self.textEdit.setReadOnly(True)
        self.orderConfirmation = QPushButton(self.groupBox)
        self.orderConfirmation.setObjectName(u"orderConfirmation")
        self.orderConfirmation.setGeometry(QRect(100, 280, 381, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.orderConfirmation.setFont(font3)
        self.orderConfirmation.setMouseTracking(True)
        self.orderConfirmation.setTabletTracking(True)
        self.orderConfirmation.setStyleSheet(u"background-color: rgb(109, 109, 109);\n"
"color: rgb(241, 251, 249);")
        self.orderConfirmation.setCheckable(True)
        self.orderConfirmation.setFlat(False)
        self.instructionLabel = QLabel(self.groupBox)
        self.instructionLabel.setObjectName(u"instructionLabel")
        self.instructionLabel.setGeometry(QRect(190, 250, 221, 16))
        self.instructionLabel.setFont(font3)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 51, 24))
        icon = QIcon()
        icon.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.orderSummaryLabel.setText(QCoreApplication.translate("Form", u"Order Summary", None))
        self.totalLabel.setText(QCoreApplication.translate("Form", u"Total: ", None))
        self.orderConfirmation.setText(QCoreApplication.translate("Form", u"Continue to Payment", None))
        self.instructionLabel.setText(QCoreApplication.translate("Form", u"Please insert the exact amount", None))
        self.pushButton.setText("")
    # retranslateUi

