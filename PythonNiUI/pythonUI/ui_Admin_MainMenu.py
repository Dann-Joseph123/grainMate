# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_MainMenuPaJjSC.ui'
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
import newResource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        Form.setStyleSheet(u"background-color: rgb(241, 251, 249);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 40, 61, 31))
        font = QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        icon = QIcon()
        icon.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setFlat(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, -30, 551, 231))
        self.label_3.setStyleSheet(u"background-image: url(:/newPrefix/ricemate.png);")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setLineWidth(1)
        self.label_3.setPixmap(QPixmap(u"../ricemate.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 200, 130, 130))
        self.pushButton_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../Graphics/updateIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(100, 100))
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setFlat(False)
        self.security = QPushButton(Form)
        self.security.setObjectName(u"security")
        self.security.setGeometry(QRect(330, 200, 130, 130))
        self.security.setFlat(False)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(560, 200, 130, 130))
        self.updateLabel = QLabel(Form)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(140, 340, 49, 16))
        self.alertLabel = QLabel(Form)
        self.alertLabel.setObjectName(u"alertLabel")
        self.alertLabel.setGeometry(QRect(370, 340, 49, 16))
        self.salesDataLabel = QLabel(Form)
        self.salesDataLabel.setObjectName(u"salesDataLabel")
        self.salesDataLabel.setGeometry(QRect(610, 340, 49, 16))
        self.accountButton = QPushButton(Form)
        self.accountButton.setObjectName(u"accountButton")
        self.accountButton.setGeometry(QRect(710, 30, 51, 41))
        icon2 = QIcon(QIcon.fromTheme(u"emblem-photos"))
        self.accountButton.setIcon(icon2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.label_3.setText("")
        self.pushButton_2.setText("")
        self.security.setText(QCoreApplication.translate("Form", u"Security Icon", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Sales Icon", None))
        self.updateLabel.setText(QCoreApplication.translate("Form", u"Update", None))
        self.alertLabel.setText(QCoreApplication.translate("Form", u"Security", None))
        self.salesDataLabel.setText(QCoreApplication.translate("Form", u"Sales", None))
        self.accountButton.setText(QCoreApplication.translate("Form", u"Account", None))
    # retranslateUi

