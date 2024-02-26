# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thesisUIform2wmlZoR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        Form.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        self.dinoradoHeadLabel = QLabel(Form)
        self.dinoradoHeadLabel.setObjectName(u"dinoradoHeadLabel")
        self.dinoradoHeadLabel.setGeometry(QRect(320, 20, 131, 61))
        font = QFont()
        font.setPointSize(24)
        self.dinoradoHeadLabel.setFont(font)
        self.dinoradoHeadLabel.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.dinoradoGraphicsView = QGraphicsView(Form)
        self.dinoradoGraphicsView.setObjectName(u"dinoradoGraphicsView")
        self.dinoradoGraphicsView.setGeometry(QRect(79, 110, 201, 201))
        self.dinoradoGroupBox = QGroupBox(Form)
        self.dinoradoGroupBox.setObjectName(u"dinoradoGroupBox")
        self.dinoradoGroupBox.setGeometry(QRect(280, 110, 431, 201))
        self.dinoradoLabel = QLabel(self.dinoradoGroupBox)
        self.dinoradoLabel.setObjectName(u"dinoradoLabel")
        self.dinoradoLabel.setGeometry(QRect(30, 10, 81, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.dinoradoLabel.setFont(font1)
        self.dinoradoPriceLabel = QLabel(self.dinoradoGroupBox)
        self.dinoradoPriceLabel.setObjectName(u"dinoradoPriceLabel")
        self.dinoradoPriceLabel.setGeometry(QRect(30, 40, 171, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.dinoradoPriceLabel.setFont(font2)
        self.dinoradoSpinBox = QSpinBox(self.dinoradoGroupBox)
        self.dinoradoSpinBox.setObjectName(u"dinoradoSpinBox")
        self.dinoradoSpinBox.setGeometry(QRect(30, 90, 81, 41))
        self.dinoradoTextEdit = QPlainTextEdit(self.dinoradoGroupBox)
        self.dinoradoTextEdit.setObjectName(u"dinoradoTextEdit")
        self.dinoradoTextEdit.setEnabled(False)
        self.dinoradoTextEdit.setGeometry(QRect(290, 30, 104, 41))
        self.dinoradoConfirmButton = QPushButton(self.dinoradoGroupBox)
        self.dinoradoConfirmButton.setObjectName(u"dinoradoConfirmButton")
        self.dinoradoConfirmButton.setGeometry(QRect(300, 150, 91, 31))
        self.dinoradoConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n"
"color: rgb(240, 240, 240);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.dinoradoCancelButton = QPushButton(self.dinoradoGroupBox)
        self.dinoradoCancelButton.setObjectName(u"dinoradoCancelButton")
        self.dinoradoCancelButton.setGeometry(QRect(200, 150, 91, 31))
        self.dinoradoCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(240, 240, 240);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dinoradoHeadLabel.setText(QCoreApplication.translate("Form", u"Dinorado", None))
        self.dinoradoGroupBox.setTitle("")
        self.dinoradoLabel.setText(QCoreApplication.translate("Form", u"Dinorado", None))
        self.dinoradoPriceLabel.setText(QCoreApplication.translate("Form", u"P 52.00 per kilogram", None))
        self.dinoradoConfirmButton.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.dinoradoCancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
