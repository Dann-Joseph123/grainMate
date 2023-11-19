import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui, QtWidgets
from ui_thesisUIform2 import Ui_Form

class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):

        #Launching the Main Window
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.setWindowTitle("Grainmate")
        MainWindow.resize(800, 400)
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        MainWindow.setAnimated(True)

        #Landing Page
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(50, 50, 631, 171))
        self.label2.setPixmap(QPixmap(u"ricemate.png"))
        self.pushButton = QtWidgets.QPushButton(parent = self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setText("Tap to continue:")
        self.pushButton.setStyleSheet(u"color: rgb(0,0,0)")
        self.pushButton.setGeometry(QRect(30, 230, 721, 121))
        self.pushButton.clicked.connect(self.setThesisUIform1)
        font = QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        #OrderForm
        font = QFont()
        font.setPointSize(24)
        self.orderLabel = QLabel(self.centralwidget)
        self.orderLabel.setObjectName(u"orderLabel")
        self.orderLabel.setGeometry(QRect(290, 40, 231, 41))
        self.orderLabel.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel.setText("Select your Rice")
        self.orderLabel.setFont(font)
        self.orderLabel.hide()
        
        font1 = QFont()
        font1.setPointSize(18)
        self.orderLabel2 = QLabel(self.centralwidget)
        self.orderLabel2.setObjectName(u"orderLabel2")
        self.orderLabel2.setGeometry(QRect(80, 260, 111, 41))
        self.orderLabel2.setFont(font1)
        self.orderLabel2.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel2.setText("Dinorado")
        self.orderLabel2.hide()
        self.orderLabel3 = QLabel(self.centralwidget)
        self.orderLabel3.setObjectName(u"orderLabel3")
        self.orderLabel3.setGeometry(QRect(240, 260, 151, 41))
        self.orderLabel3.setFont(font1)
        self.orderLabel3.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel3.setText("Sinandomeng")
        self.orderLabel3.hide()
        self.orderLabel4 = QLabel(self.centralwidget)
        self.orderLabel4.setObjectName(u"orderLabel4")
        self.orderLabel4.setGeometry(QRect(450, 260, 91, 41))
        self.orderLabel4.setFont(font1)
        self.orderLabel4.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel4.setText("Jasmine")
        self.orderLabel4.hide()
        self.orderLabel5 = QLabel(self.centralwidget)
        self.orderLabel5.setObjectName(u"orderLabel5")
        self.orderLabel5.setGeometry(QRect(650, 260, 61, 41))
        self.orderLabel5.setFont(font1)
        self.orderLabel5.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel5.setText("NFA")
        self.orderLabel5.hide()
        self.orderLabel6 = QLabel(self.centralwidget)
        self.orderLabel6.setObjectName(u"orderLabel6")
        self.orderLabel6.setGeometry(QRect(100, 310, 81, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.orderLabel6.setFont(font2)
        self.orderLabel6.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel6.setText("P. 52.00")
        self.orderLabel6.hide()
        self.orderLabel7 = QLabel(self.centralwidget)
        self.orderLabel7.setObjectName(u"orderLabel7")
        self.orderLabel7.setGeometry(QRect(270, 310, 81, 21))
        self.orderLabel7.setFont(font2)
        self.orderLabel7.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel7.setText("P. 45.00")
        self.orderLabel7.hide()
        self.orderLabel8 = QLabel(self.centralwidget)
        self.orderLabel8.setObjectName(u"orderLabel8")
        self.orderLabel8.setGeometry(QRect(460, 310, 81, 21))
        self.orderLabel8.setFont(font2)
        self.orderLabel8.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel8.setText("P. 47.00")
        self.orderLabel8.hide()
        self.orderLabel9 = QLabel(self.centralwidget)
        self.orderLabel9.setObjectName(u"orderLabel9")
        self.orderLabel9.setGeometry(QRect(640, 310, 81, 21))
        self.orderLabel9.setFont(font2)
        self.orderLabel9.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel9.setText("P. 57.00")
        self.orderLabel9.hide()
        #OrderForm Buttons

        #Product #1
        self.orderPushButton1 = QPushButton(self.centralwidget)
        self.orderPushButton1.setObjectName(u"orderPushButton1")
        self.orderPushButton1.setGeometry(QRect(60, 120, 141, 131))
        icon = QIcon()
        icon.addFile(u"Graphics\Dinorado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton1.setIcon(icon)
        self.orderPushButton1.setIconSize(QSize(140, 140))
        self.orderPushButton1.hide()

        #Product#2
        self.orderPushButton2 = QPushButton(self.centralwidget)
        self.orderPushButton2.setObjectName(u"orderPushButton2")
        self.orderPushButton2.setGeometry(QRect(240, 120, 141, 131))
        icon1 = QIcon()
        icon1.addFile(u"Graphics\Sinandomeng.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton2.setIcon(icon1)
        self.orderPushButton2.setIconSize(QSize(181, 181))
        self.orderPushButton2.hide()

        #Product#3
        self.orderPushButton3 = QPushButton(self.centralwidget)
        self.orderPushButton3.setObjectName(u"orderPushButton3")
        self.orderPushButton3.setGeometry(QRect(420, 120, 141, 131))
        icon2 = QIcon()
        icon2.addFile(u"Graphics\Jasmine.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton3.setIcon(icon2)
        self.orderPushButton3.setIconSize(QSize(194, 191))
        self.orderPushButton3.hide()

        #Product#3
        self.orderPushButton4 = QPushButton(self.centralwidget)
        self.orderPushButton4.setObjectName(u"orderPushButton4")
        self.orderPushButton4.setGeometry(QRect(600, 120, 141, 131))
        icon3 = QIcon()
        icon3.addFile(u"Graphics\eNFA.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton4.setIcon(icon3)
        self.orderPushButton4.setIconSize(QSize(195, 140))
        self.orderPushButton4.hide()
        


        #Order Amount
        self.dinoradoHeadLabel = QLabel(self.centralwidget)
        self.dinoradoHeadLabel.setObjectName(u"dinoradoHeadLabel")
        self.dinoradoHeadLabel.setGeometry(QRect(320, 20, 131, 61))
        font = QFont()
        font.setPointSize(24)
        self.dinoradoHeadLabel.setFont(font)
        self.dinoradoHeadLabel.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.dinoradoGraphicsView = QGraphicsView(self.centralwidget)
        self.dinoradoGraphicsView.setObjectName(u"dinoradoGraphicsView")
        self.dinoradoGraphicsView.setGeometry(QRect(79, 110, 201, 201))
        self.dinoradoGroupBox = QGroupBox(self.centralwidget)
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
        self.dinoradoConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n" "color: rgb(240, 240, 240);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.dinoradoCancelButton = QPushButton(self.dinoradoGroupBox)
        self.dinoradoCancelButton.setObjectName(u"dinoradoCancelButton")
        self.dinoradoCancelButton.setGeometry(QRect(200, 150, 91, 31))
        self.dinoradoCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n" "font: 10pt \"MS Shell Dlg 2\";\n" "color: rgb(240, 240, 240);")
        
        
        
        
        
        
        
        
        
        
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", u"MainWindow", None))
        self.label2.setText("")
        self.pushButton.setText(_translate("MainWindow", u"Tap to order", None))
        self.pushButton.setText("Tap to Order")

    # retranslateUi

    def setThesisUIform(self):
        self.label2.show()
        self.pushButton.show()
        
        #self.label_2.hide()


    def setThesisUIform1(self):
        self.label2.hide()
        self.pushButton.hide()
        self.orderLabel.show()
        self.orderLabel2.show()
        self.orderLabel3.show()
        self.orderLabel4.show()
        self.orderLabel5.show()
        self.orderLabel6.show()
        self.orderLabel7.show()
        self.orderLabel8.show()
        self.orderLabel9.show()
        self.orderPushButton1.show()
        self.orderPushButton2.show()
        self.orderPushButton3.show()
        self.orderPushButton4.show()
        self.orderPushButton1.clicked.connect()
        print("Clicked")

    def setThesisUIform2(self):
        self.label2.hide()
        self.pushButton.hide()
        self.orderLabel.hide()
        self.orderLabel2.hide()
        self.orderLabel3.hide()
        self.orderLabel4.hide()
        self.orderLabel5.hide()
        self.orderLabel6.hide()
        self.orderLabel7.hide()
        self.orderLabel8.hide()
        self.orderLabel9.hide()
        self.orderPushButton1.hide()
        self.orderPushButton2.hide()
        self.orderPushButton3.hide()
        self.orderPushButton4.hide()



        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())