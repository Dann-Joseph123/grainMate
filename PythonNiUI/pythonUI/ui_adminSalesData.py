# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salesDataeXzeRx.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        self.salesListView = QListView(Form)
        self.salesListView.setObjectName(u"salesListView")
        self.salesListView.setGeometry(QRect(130, 110, 541, 251))
        self.salesDataLabel = QLabel(Form)
        self.salesDataLabel.setObjectName(u"salesDataLabel")
        self.salesDataLabel.setGeometry(QRect(300, 10, 221, 81))
        font = QFont()
        font.setPointSize(34)
        font.setBold(False)
        self.salesDataLabel.setFont(font)
        self.salesDataLabel.setStyleSheet(u"color: rgb(29, 108, 77);")
        self.backBUtton = QPushButton(Form)
        self.backBUtton.setObjectName(u"backBUtton")
        self.backBUtton.setGeometry(QRect(50, 40, 61, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.backBUtton.setFont(font1)
        self.backBUtton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        icon = QIcon()
        icon.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBUtton.setIcon(icon)
        self.backBUtton.setIconSize(QSize(30, 30))
        self.backBUtton.setFlat(True)
        self.accountButton = QPushButton(Form)
        self.accountButton.setObjectName(u"accountButton")
        self.accountButton.setGeometry(QRect(700, 50, 51, 41))
        font2 = QFont()
        font2.setBold(False)
        self.accountButton.setFont(font2)
        self.accountButton.setStyleSheet(u"color: rgb(31, 116, 83);")
        icon1 = QIcon(QIcon.fromTheme(u"emblem-photos"))
        self.accountButton.setIcon(icon1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.salesDataLabel.setText(QCoreApplication.translate("Form", u"Sales Data", None))
        self.backBUtton.setText("")
        self.accountButton.setText(QCoreApplication.translate("Form", u"Account", None))
    # retranslateUi

