# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminUnregisteredSalesvIELtT.ui'
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
        self.accountButton = QPushButton(Form)
        self.accountButton.setObjectName(u"accountButton")
        self.accountButton.setGeometry(QRect(700, 50, 51, 41))
        font = QFont()
        font.setBold(False)
        self.accountButton.setFont(font)
        self.accountButton.setStyleSheet(u"color: rgb(31, 116, 83);")
        icon = QIcon(QIcon.fromTheme(u"emblem-photos"))
        self.accountButton.setIcon(icon)
        self.backBUtton = QPushButton(Form)
        self.backBUtton.setObjectName(u"backBUtton")
        self.backBUtton.setGeometry(QRect(50, 40, 61, 31))
        font1 = QFont()
        font1.setPointSize(13)
        self.backBUtton.setFont(font1)
        self.backBUtton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        icon1 = QIcon()
        icon1.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBUtton.setIcon(icon1)
        self.backBUtton.setIconSize(QSize(30, 30))
        self.backBUtton.setFlat(True)
        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(130, 110, 541, 251))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 20, 381, 81))
        font2 = QFont()
        font2.setPointSize(34)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(29, 108, 77);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.accountButton.setText(QCoreApplication.translate("Form", u"Account", None))
        self.backBUtton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Unregistered Sales", None))
    # retranslateUi

