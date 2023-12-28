# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminUpdateProductsUUniPB.ui'
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
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        Form.setStyleSheet(u"background-color: rgb(241, 251, 249);")
        self.alertLabel = QLabel(Form)
        self.alertLabel.setObjectName(u"alertLabel")
        self.alertLabel.setGeometry(QRect(470, 350, 61, 16))
        self.alertLabel.setText(u"Alert Label")
        self.accountButton = QPushButton(Form)
        self.accountButton.setObjectName(u"accountButton")
        self.accountButton.setGeometry(QRect(700, 30, 51, 41))
        self.accountButton.setStyleSheet(u"color: rgb(31, 116, 83);")
        icon = QIcon(QIcon.fromTheme(u"emblem-photos"))
        self.accountButton.setIcon(icon)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, -50, 551, 231))
        self.label_3.setStyleSheet(u"background-image: url(:/newPrefix/ricemate.png);")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setPixmap(QPixmap(u"../ricemate.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.updateLabel = QLabel(Form)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(150, 350, 49, 16))
        self.security = QPushButton(Form)
        self.security.setObjectName(u"security")
        self.security.setGeometry(QRect(120, 230, 110, 110))
        self.security.setFlat(False)
        self.salesDataLabel = QLabel(Form)
        self.salesDataLabel.setObjectName(u"salesDataLabel")
        self.salesDataLabel.setGeometry(QRect(630, 350, 61, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 61, 31))
        font = QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        icon1 = QIcon()
        icon1.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setFlat(True)
        self.security_2 = QPushButton(Form)
        self.security_2.setObjectName(u"security_2")
        self.security_2.setGeometry(QRect(280, 230, 110, 110))
        self.security_2.setFlat(False)
        self.security_3 = QPushButton(Form)
        self.security_3.setObjectName(u"security_3")
        self.security_3.setGeometry(QRect(440, 230, 110, 110))
        self.security_3.setFlat(False)
        self.security_4 = QPushButton(Form)
        self.security_4.setObjectName(u"security_4")
        self.security_4.setGeometry(QRect(600, 230, 110, 110))
        self.security_4.setFlat(False)
        self.updateLabel_2 = QLabel(Form)
        self.updateLabel_2.setObjectName(u"updateLabel_2")
        self.updateLabel_2.setGeometry(QRect(310, 350, 49, 16))
        self.alertLabel_2 = QLabel(Form)
        self.alertLabel_2.setObjectName(u"alertLabel_2")
        self.alertLabel_2.setGeometry(QRect(290, 170, 251, 31))
        self.alertLabel_2.setStyleSheet(u"font-size: 24px;\n"
"color: rgb(31, 115, 82);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.alertLabel.setText(QCoreApplication.translate("Form", u"Product 3", None))
        self.accountButton.setText(QCoreApplication.translate("Form", u"Account", None))
        self.label_3.setText("")
        self.updateLabel.setText(QCoreApplication.translate("Form", u"Product 1", None))
        self.security.setText(QCoreApplication.translate("Form", u"Product 1 Image", None))
        self.salesDataLabel.setText(QCoreApplication.translate("Form", u"Product 4", None))
        self.pushButton.setText("")
        self.security_2.setText(QCoreApplication.translate("Form", u"Product 2 Image", None))
        self.security_3.setText(QCoreApplication.translate("Form", u"Product 3 Image", None))
        self.security_4.setText(QCoreApplication.translate("Form", u"Product 4 Image", None))
        self.updateLabel_2.setText(QCoreApplication.translate("Form", u"Product 1", None))
        self.alertLabel_2.setText(QCoreApplication.translate("Form", u"Update product details", None))
    # retranslateUi

