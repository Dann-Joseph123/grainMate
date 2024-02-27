import sys
import csv
#import gpiozero
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
# from  gpiozero.pins.pigpio import PiGPIOFactory
# from gpiozero import AngularServo
# from time import sleep
# import RPi.GPIO as GPIO
# from hx711 import HX711

# from coin_acceptor import setup, loop
#from TempSensor import read_temp
#from load_Sensor import get_load

class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
               
        #Launching the Main Window
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.setWindowTitle("GrainMate")   
        MainWindow.resize(800, 480)
        MainWindow.setTabletTracking(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(241, 251, 249)")
        MainWindow.setAnimated(True)
        
        #variable for the previous value of coin
        self.previousValue = 0
        self.coinsValue = 0
        
    ####################################################################################################################
            #--------------------------------------------- LANDING PAGE ------------------------------------------>
    ####################################################################################################################
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(90, -50, 631, 401))
        titleFont = QFont()
        titleFont.setPointSize(80)
        titleFont.setBold(True)
        self.label2.setFont(titleFont)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setText("Ricemate")
        self.label2.setStyleSheet("color: rgb(33,123,88)")   
        self.pushButton = QtWidgets.QPushButton(parent = self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setText("Tap to continue:")
        self.pushButton.setStyleSheet(u"color: rgb(0,0,0)")
        self.pushButton.setGeometry(QRect(30, 270, 721, 121))
        self.pushButton.clicked.connect(self.setOrderPage)
        font = QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(720, 70, 51, 41))
        self.pushButton_2.setStyleSheet(u"image: url(home.png)")
        self.pushButton_2.setText("Home")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.clicked.connect(self.setAdminLandingPage)
        MainWindow.setCentralWidget(self.centralwidget)

    ####################################################################################################################
            #--------------------------------------------- ORDER FORM------------------------------------------>
    ####################################################################################################################
        font = QFont()
        font.setPointSize(24)
        self.orderLabel = QLabel(self.centralwidget)
        self.orderLabel.setObjectName(u"orderLabel")
        self.orderLabel.setGeometry(QRect(300, 70, 231, 41))
        self.orderLabel.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel.setText("Select your Rice")
        self.orderLabel.setFont(font)
        self.orderLabel.hide()
        
        font1 = QFont()
        font1.setPointSize(18)
        self.orderLabel2 = QLabel(self.centralwidget)
        self.orderLabel2.setObjectName(u"orderLabel2")
        self.orderLabel2.setGeometry(QRect(170, 320, 111, 41))
        self.orderLabel2.setFont(font1)
        self.orderLabel2.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel2.setAlignment(Qt.AlignCenter)
        # self.orderLabel2.setReadOnly(True)
        # self.orderLabel2.setText("Dinorado")
        self.orderLabel2.hide()
        self.orderLabel3 = QLabel(self.centralwidget)
        self.orderLabel3.setObjectName(u"orderLabel3")
        self.orderLabel3.setGeometry(QRect(340, 320, 151, 41))
        self.orderLabel3.setFont(font1)
        self.orderLabel3.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel3.setAlignment(Qt.AlignCenter)
        #self.orderLabel3.setReadOnly(True)
        # self.orderLabel3.setText("Sinandomeng")
        self.orderLabel3.hide()
        self.orderLabel4 = QLabel(self.centralwidget)
        self.orderLabel4.setObjectName(u"orderLabel4")
        self.orderLabel4.setGeometry(QRect(540, 320, 100, 41))
        self.orderLabel4.setFont(font1)
        self.orderLabel4.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel4.setAlignment(Qt.AlignCenter)
        self.orderLabel4.hide()
        self.orderLabel6 = QLabel(self.centralwidget)
        self.orderLabel6.setObjectName(u"orderLabel6")
        self.orderLabel6.setGeometry(QRect(180, 370, 81, 21))
        font2 = QFont()
        font2.setPointSize(10       )
        self.orderLabel6.setFont(font2)
        self.orderLabel6.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel6.setAlignment(Qt.AlignCenter)
        self.orderLabel6.hide()
        self.orderLabel7 = QLabel(self.centralwidget)
        self.orderLabel7.setObjectName(u"orderLabel7")
        self.orderLabel7.setGeometry(QRect(370, 370, 81, 21))
        self.orderLabel7.setFont(font2)
        self.orderLabel7.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel7.setAlignment(Qt.AlignCenter)
        self.orderLabel7.hide()
        self.orderLabel8 = QLabel(self.centralwidget)
        self.orderLabel8.setObjectName(u"orderLabel8")
        self.orderLabel8.setGeometry(QRect(550, 370, 81, 21))
        self.orderLabel8.setFont(font2)
        self.orderLabel8.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel8.setAlignment(Qt.AlignCenter)
        self.orderLabel8.hide()
        
        
    ####################################################################################################################
        #--------------------------------------------- ORDER FORM BUTTONS ------------------------------------------>
    ####################################################################################################################

        backIcon = QIcon()
        backIcon.addFile(u"Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adminProductBackButton = QPushButton(self.centralwidget)
        self.adminProductBackButton.setObjectName(u"adminProductBackButton")
        self.adminProductBackButton.setGeometry(QRect(20, 30, 61, 31))
        self.adminProductBackButton.setIcon(backIcon)
        self.adminProductBackButton.setText(" <<< ")
        self.adminProductBackButton.setFlat(True)
        self.adminProductBackButton.clicked.connect(self.displayHomePage)
        adminProductBackButtonFont3 = QFont()
        adminProductBackButtonFont3.setPointSize(12)

    ####################################################################################################################
        #--------------------------------------------- ORDER FORM BUTTON 1 ------------------------------------------>
    ####################################################################################################################
        self.orderPushButton1 = QPushButton(self.centralwidget)
        self.orderPushButton1.setObjectName(u"orderPushButton1")
        self.orderPushButton1.setGeometry(QRect(160, 150, 141, 131))
        icon = QIcon()
        icon.addFile(u"Graphics/genRice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton1.setIcon(icon)
        self.orderPushButton1.setIconSize(QSize(140, 140))
        self.orderPushButton1.hide()

    ####################################################################################################################
        #--------------------------------------------- ORDER FORM BUTTON 2 ------------------------------------------>
    ####################################################################################################################
        self.orderPushButton2 = QPushButton(self.centralwidget)
        self.orderPushButton2.setObjectName(u"orderPushButton2")
        self.orderPushButton2.setGeometry(QRect(340, 150, 141, 131))
        icon1 = QIcon()
        icon1.addFile(u"Graphics/genRice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton2.setIcon(icon1)
        self.orderPushButton2.setIconSize(QSize(181, 181))
        self.orderPushButton2.hide()

    ####################################################################################################################
        #--------------------------------------------- ORDER FORM BUTTON 3------------------------------------------>
    ####################################################################################################################
        self.orderPushButton3 = QPushButton(self.centralwidget)
        self.orderPushButton3.setObjectName(u"orderPushButton3")
        self.orderPushButton3.setGeometry(QRect(520, 150, 141, 131))
        icon2 = QIcon()
        icon2.addFile(u"Graphics\Jasmine.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton3.setIcon(icon2)
        self.orderPushButton3.setIconSize(QSize(194, 191))
        self.orderPushButton3.hide()

    ####################################################################################################################
    #--------------------------------------------- ORDER FORM WEIGHT LABEL 1------------------------------------------>
    ####################################################################################################################
        self.orderWeight = QLabel(self.centralwidget)
        self.orderWeight.setObjectName(u"orderWeight")
        self.orderWeight.setGeometry(QRect(170, 290, 111, 41))
        self.orderWeight.setFont(font2)
        self.orderWeight.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderWeight.setAlignment(Qt.AlignCenter)
        self.orderWeight.hide()
        
    ####################################################################################################################
    #--------------------------------------------- ORDER FORM WEIGHT LABEL 2 ------------------------------------------>
    ####################################################################################################################
        self.orderWeight2 = QLabel(self.centralwidget)
        self.orderWeight2.setObjectName(u"orderWeight2")
        self.orderWeight2.setGeometry(QRect(360, 290, 111, 41))
        self.orderWeight2.setFont(font2)
        self.orderWeight2.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderWeight2.setAlignment(Qt.AlignCenter)
        self.orderWeight2.hide()

    ####################################################################################################################
    #--------------------------------------------- ORDER FORM WEIGHT LABEL 3 ------------------------------------------>
    ####################################################################################################################

        self.orderWeight3 = QLabel(self.centralwidget)
        self.orderWeight3.setObjectName(u"orderWeight3")
        self.orderWeight3.setGeometry(QRect(535, 290, 111, 41))
        self.orderWeight3.setFont(font2)
        self.orderWeight3.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderWeight3.setAlignment(Qt.AlignCenter)
        self.orderWeight3.hide()

    ####################################################################################################################
    #--------------------------------------------- PRODUCT 1 || GENERAL FORMAT ---------------------------------------->
    ####################################################################################################################
        self.productTitle1 = QLabel(self.centralwidget)
        self.productTitle1.setObjectName(u"label")
        self.productTitle1.setGeometry(QRect(290, 40, 211, 61))
        font = QFont()
        font.setPointSize(24)
        self.universalGroupBox = QGroupBox(self.centralwidget)
        self.universalGroupBox.setObjectName(u"productGroupBox1")
        self.universalGroupBox.setGeometry(QRect(281, 130, 431, 201))
        self.universalGroupBox.hide()
        self.universalTextEdit = QLineEdit(self.universalGroupBox)
        self.universalTextEdit.setObjectName(u"productTextEdit1")
        self.universalTextEdit.setEnabled(True)
        self.universalTextEdit.setGeometry(QRect(290, 40, 104, 51))
        self.universalTextEdit.setReadOnly(True)
        self.universalTextEdit.setFont(font1)
        self.universalTextEdit.hide()
        self.universalConfirmButton = QPushButton(self.universalGroupBox)
        self.universalConfirmButton.setObjectName(u"productConfirmButton1")
        self.universalConfirmButton.setGeometry(QRect(300, 160, 91, 31))
        self.universalConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n" "color: rgb(240, 240, 240);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.universalConfirmButton.setText(u"Confirm")
        self.universalCancelButton = QPushButton(self.universalGroupBox)
        self.universalCancelButton.setObjectName(u"productCancelButton1")
        self.universalCancelButton.setGeometry(QRect(200, 160, 91, 31))
        self.universalCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n""font: 10pt \"MS Shell Dlg 2\";\n""color: rgb(240, 240, 240);")
        self.universalCancelButton.setText(u"Cancel")
        self.productTitle1.setFont(font)
        self.productTitle1.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle1.hide()
        self.productLabel1 = QLabel(self.universalGroupBox)
        self.productLabel1.setObjectName(u"productLabel1")
        self.productLabel1.setGeometry(QRect(30, 20, 121, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.productLabel1.setFont(font1)
        self.productLabel1.hide()
        self.productPrice1 = QTextEdit(self.universalGroupBox)
        self.productPrice1.setObjectName(u"productPrice1")
        self.productPrice1.setGeometry(QRect(30, 50, 80, 31))
        self.productPrice1.setEnabled(True)
        self.productPrice1.setReadOnly(True)
        font2 = QFont()
        font2.setPointSize(11)
        self.productPrice1.setFont(font2)
        self.productPrice1.hide()
        self.productView1= QGraphicsView(self.centralwidget)
        self.productView1.setObjectName(u"productView1")
        self.productView1.setGeometry(QRect(80, 130, 201, 201))
        self.productView1.hide()
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        self.universalConfirmButton.clicked.connect(self.coins)
        self.productSpinBox1 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox1.setObjectName(u"productSpinBox1")
        spinBoxFontSize = QFont()
        spinBoxFontSize.setPointSize(15)
        self.productSpinBox1.setFont(spinBoxFontSize)
        self.productSpinBox1.setGeometry(QRect(30, 100, 81, 41))
        self.productSpinBox1.setMaximum(5)
        self.productSpinBox1.hide()
        self.temperatureSensor = QLabel(MainWindow)
        self.temperatureSensor.setObjectName(u"temperatureSensor")
        self.temperatureSensor.setGeometry(QRect(185, 120, 100, 21))
        self.temperatureSensor.setFont(font2)
        self.temperatureSensor.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.temperatureSensor.setAlignment(Qt.AlignCenter)
        self.temperatureSensor.hide()

        self.productSpinBox1.valueChanged.connect(self.displayToTotal1)
        self.productPrice1.textChanged.connect(self.priceToAmount1)

    ####################################################################################################################
    #--------------------------------------------- PRODUCT 2 ORDER DETAILS ------------------------------------------>
    ####################################################################################################################
        self.productTitle2 = QLabel(self.centralwidget)
        self.productTitle2.setObjectName(u"label")
        self.productTitle2.setGeometry(QRect(290, 50, 211, 61))
        self.productTitle2.setFont(font)
        self.productTitle2.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle2.hide()
        self.productLabel2 = QLabel(self.universalGroupBox)
        self.productLabel2.setObjectName(u"sinandomengLabel")
        self.productLabel2.setGeometry(QRect(30, 20, 121, 31))
        self.productLabel2.setFont(font1)
        self.productLabel2.hide()
        self.productPrice2 = QTextEdit(self.universalGroupBox)
        self.productPrice2.setObjectName(u"sinandomengPrice")
        self.productPrice2.setGeometry(QRect(30, 50, 80, 31))
        self.productPrice2.setEnabled(True)
        self.productPrice2.setReadOnly(True)
        self.productPrice2.setFont(font2)
        self.productPrice2.hide()
        self.productView2 = QGraphicsView(self.centralwidget)
        self.productView2.setObjectName(u"sinandomengView")
        self.productView2.setGeometry(QRect(80, 130, 201, 201))
        self.productView2.hide()
        self.productSpinBox2 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox2.setObjectName(u"productSpinBox2")
        self.productSpinBox2.setFont(spinBoxFontSize)
        self.productSpinBox2.setGeometry(QRect(30, 100, 81, 41))
        self.productSpinBox2.setMaximum(10      )
        self.productSpinBox2.hide()
        self.productPrice2.textChanged.connect(self.priceToAmount2)  
        self.productSpinBox2.valueChanged.connect(self.displayToTotal2)
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        #self.universalConfirmButton.clicked.connect(self.setOrderSummary)
        
    ####################################################################################################################
    #--------------------------------------------- PRODUCT 3 ORDER DETAILS ------------------------------------------>
    ####################################################################################################################
        self.productTitle3 = QLabel(self.centralwidget)
        self.productTitle3.setObjectName(u"label")
        self.productTitle3.setGeometry(QRect(290, 50, 211, 61))
        self.productTitle3.setFont(font)
        self.productTitle3.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle3.hide()
        self.productLabel3 = QLabel(self.universalGroupBox)
        self.productLabel3.setObjectName(u"productLabel3")
        self.productLabel3.setGeometry(QRect(30, 20, 121, 31))
        self.productLabel3.setFont(font1)
        self.productLabel3.hide()
        self.productPrice3 = QTextEdit(self.universalGroupBox)
        self.productPrice3.setObjectName(u"productPrice3")
        self.productPrice3.setGeometry(QRect(30, 50, 80, 31))
        self.productPrice3.setEnabled(True)
        self.productPrice3.setReadOnly(True)
        self.productPrice3.setFont(font2)
        self.productPrice3.hide()
        self.productView3 = QGraphicsView(self.centralwidget)
        self.productView3.setObjectName(u"productView3")
        self.productView3.setGeometry(QRect(80, 130, 201, 201))
        self.productView3.hide()
        self.productSpinBox3 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox3.setObjectName(u"productSpinBox3")
        self.productSpinBox3.setFont(spinBoxFontSize)
        self.productSpinBox3.setGeometry(QRect(30, 100, 81, 41))
        self.productSpinBox3.setMaximum(10      )
        self.productSpinBox3.hide()
        self.productPrice3.textChanged.connect(self.priceToAmount3)  
        self.productSpinBox3.valueChanged.connect(self.displayToTotal3)
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        #self.universalConfirmButton.clicked.connect(self.setOrderSummary)

    ####################################################################################################################
        #--------------------------------------------- ORDER SUMMARY ------------------------------------------>
    ####################################################################################################################
        self.orderSummaryLabelgroupBox = QGroupBox(self.centralwidget)
        self.orderSummaryLabelgroupBox.setObjectName(u"groupBox")
        self.orderSummaryLabelgroupBox.setGeometry(QRect(110, 50, 581, 361))
        self.orderSummaryLabel = QLabel(self.orderSummaryLabelgroupBox)
        self.orderSummaryLabel.setObjectName(u"orderSummaryLabel")
        self.orderSummaryLabel.setGeometry(QRect(50, 50, 261, 51))
        font = QFont()
        font.setPointSize(26)
        self.orderSummaryLabel.setFont(font)
        self.orderSummaryLabel.setText(u"Order Summary")
        self.totalLabel = QLabel(self.orderSummaryLabelgroupBox)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setGeometry(QRect(20, 120, 131, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.totalLabel.setFont(font1)
        self.totalLabel.setText("Total")
        self.textEdit = QLineEdit(self.orderSummaryLabelgroupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(350, 110, 181, 61))
        font2 = QFont()
        font2.setPointSize(22)
        self.textEdit.setFont(font2)
        self.textEdit.setReadOnly(True)
        self.orderConfirmationToCoins = QPushButton(self.orderSummaryLabelgroupBox)
        self.orderConfirmationToCoins.setObjectName(u"orderConfirmation")
        self.orderConfirmationToCoins.setGeometry(QRect(100, 280, 381, 41))
        font3 = QFont()
        font3.setPointSize(10)

        font3instruction = QFont()
        font3instruction.setPointSize(15)
        self.orderConfirmationToCoins.setFont(font3)
        self.orderConfirmationToCoins.setMouseTracking(True)
        self.orderConfirmationToCoins.setTabletTracking(True)
        self.orderConfirmationToCoins.setStyleSheet(u"background-color: rgb(109, 109, 109); ""\n""color: rgb(241, 251, 249);")
        self.orderConfirmationToCoins.setFlat(False)
        self.orderConfirmationToCoins.setText("Tap to proceed to coins")
        self.orderConfirmationToCoins.clicked.connect(self.coins)
        self.instruction = QLabel(self.orderSummaryLabelgroupBox)
        self.instruction.setObjectName(u"instruction")
        self.instruction.setGeometry(QRect(185, 240, 270, 16))
        self.instruction.setFont(font3instruction)
        self.instruction.setText(u"Please insert the bills first")

        self.amountPaid = QLabel(self.orderSummaryLabelgroupBox)
        self.amountPaid.setObjectName(u"amountPaid")
        self.amountPaid.setGeometry(QRect(20, 180, 321, 31))
        self.amountPaid.setFont(font1)
        self.amountPaid.setText(u"Amount Paid in Bills")
        self.amountPaidTextEdit = QLineEdit(self.orderSummaryLabelgroupBox)
        self.amountPaidTextEdit.setObjectName(u"amountPaidTextEdit")
        self.amountPaidTextEdit.setEnabled(True)
        self.amountPaidTextEdit.setGeometry(QRect(350, 170, 181, 51))
        self.amountPaidTextEdit.setFont(font2)
        self.amountPaidTextEdit.setReadOnly(True)
        
        
    ####################################################################################################################
    #--------------------------------------------- COIN ACCEPTING PAGE ------------------------------------------>
    ####################################################################################################################
        self.instruction1 = QLabel(self.orderSummaryLabelgroupBox)
        self.instruction1.setObjectName(u"instruction1")
        self.instruction1.setGeometry(QRect(185, 240, 270, 16))
        self.instruction1.setFont(font3instruction)
        self.instruction1.setText(u"Please insert the coins")
        self.amountCoinPaid = QLabel(self.orderSummaryLabelgroupBox)
        self.amountCoinPaid.setObjectName(u"amountPaid")
        self.amountCoinPaid.setGeometry(QRect(20, 180, 321, 31))
        self.amountCoinPaid.setFont(font1)
        self.amountCoinPaid.setText(u"Amount Paid in Coins")
        self.amountCoinPaidTextEdit = QLineEdit(self.orderSummaryLabelgroupBox)
        self.amountCoinPaidTextEdit.setObjectName(u"amountPaidTextEdit")
        self.amountCoinPaidTextEdit.setEnabled(True)
        self.amountCoinPaidTextEdit.setGeometry(QRect(350, 170, 181, 51))
        self.amountCoinPaidTextEdit.setFont(font2)
        self.amountCoinPaidTextEdit.setReadOnly(False)
        self.amountCoinPaid.hide()
        self.amountCoinPaidTextEdit.hide()
        self.orderConfirmation = QPushButton(self.orderSummaryLabelgroupBox)
        self.orderConfirmation.setObjectName(u"orderConfirmation")
        self.orderConfirmation.setGeometry(QRect(100, 280, 381, 41))
        self.orderConfirmation.setFont(font3)
        self.orderConfirmation.setStyleSheet(u"background-color: rgb(109, 109, 109); ""\n""color: rgb(241, 251, 249);")
        self.orderConfirmation.setText("Click to Continue")
        self.orderConfirmation.clicked.connect(self.verifyInputPrice)

        
    ####################################################################################################################
    #--------------------------------------------- TOTAL AMOUNT INSERTED ------------------------------------------>
    ####################################################################################################################
        self.amountTotalPaid = QLabel(self.orderSummaryLabelgroupBox)
        self.amountTotalPaid.setObjectName(u"amountTotalPaid")
        self.amountTotalPaid.setGeometry(QRect(20, 180, 321, 31))
        self.amountTotalPaid.setFont(font1)
        self.amountTotalPaid.setText(u"Amount Paid by User")
        self.amountTotalPaidTextEdit = QLineEdit(self.orderSummaryLabelgroupBox)
        self.amountTotalPaidTextEdit.setObjectName(u"amountTotalPaidTextEdit")
        self.amountTotalPaidTextEdit.setEnabled(True)
        self.amountTotalPaidTextEdit.setGeometry(QRect(350, 170, 181, 51))
        self.amountTotalPaidTextEdit.setFont(font2)
        self.amountTotalPaidTextEdit.setReadOnly(False)
        self.amountTotalPaid.hide()
        self.amountTotalPaidTextEdit.hide()
        self.verifyOrderConfirmation = QPushButton(self.orderSummaryLabelgroupBox)
        self.verifyOrderConfirmation.setObjectName(u"verifyOrderConfirmation")
        self.verifyOrderConfirmation.setGeometry(QRect(100, 280, 381, 41))
        self.verifyOrderConfirmation.setFont(font3)
        self.verifyOrderConfirmation.setStyleSheet(u"background-color: rgb(109, 109, 109); ""\n""color: rgb(241, 251, 249);")
        self.verifyOrderConfirmation.setText("Click to continue")
        self.verifyOrderConfirmation.clicked.connect(self.verifyInputPrice)
        self.verifyOrderConfirmation.hide()

            
    ####################################################################################################################
    #--------------------------------------------- BACK BUTTON || CANCEL TRANSACTION ---------------------------------->
    ####################################################################################################################
        self.backPushButton = QPushButton(self.orderSummaryLabelgroupBox)
        self.backPushButton.setObjectName(u"pushButton")
        self.backPushButton.setGeometry(QRect(20, 20, 51, 24))
        backIcon = QIcon()
        backIcon.addFile(u"Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backPushButton.setIcon(backIcon)
        self.backPushButton.setText(" <<< ")
        self.backPushButton.setFlat(True)
        self.backPushButton.clicked.connect(self.reminderMessage)
        
        self.instruction.hide()
        self.orderSummaryLabel.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.textEdit.hide()
        self.orderConfirmation.hide()
        self.backPushButton.hide()
        self.totalLabel.hide()
        self.orderConfirmationToCoins.hide()
        self.instruction1.hide()


        
    ####################################################################################################################
    #---------------------------------------------  THANK YOU PAGE ------------------------------------------>
    ####################################################################################################################
        self.thankYoulabel = QLabel(MainWindow)
        self.thankYoulabel.setObjectName(u"thankYoulabel")
        self.thankYoulabel.setGeometry(QRect(260, 140, 261, 51))
        font = QFont()
        font.setPointSize(24)
        self.thankYoulabel.setFont(font)
        self.thankYoulabel.setStyleSheet(u"color: rgb(33, 123, 88)")
        self.thankYoulabel.setText(u"Order is Complete")
        self.thankYoulabel.setAlignment(Qt.AlignCenter)
        self.thankYoulabel_2 = QLabel(MainWindow)
        self.thankYoulabel_2.setObjectName(u"thankYoulabel_2")
        self.thankYoulabel_2.setGeometry(QRect(100, 210, 591, 51))
        self.thankYoulabel_2.setFont(font)
        self.thankYoulabel_2.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.thankYoulabel_2.setText(u"You can now pick your order")
        self.thankYoulabel_2.setAlignment(Qt.AlignCenter)
        self.thankYoupushButton = QPushButton(MainWindow)
        self.thankYoupushButton.setObjectName(u"thankYoupushButton")
        self.thankYoupushButton.setGeometry(QRect(290, 300, 201, 51))
        self.thankYoupushButton.clicked.connect(self.displayHomePage)
        self.thankYoupushButton.setText("Return to Home Page")

        self.thankYoulabel.hide()
        self.thankYoulabel_2.hide()
        self.thankYoupushButton.hide()

                
    ####################################################################################################################
    #------------------------------------------- LOADING AND DISPENSING PAGE ------------------------------------------>
    ####################################################################################################################
        splashScreenfont = QFont()
        splashScreenfont.setPointSize(18)
        self.splashScreenLabel = QLabel(MainWindow)
        self.splashScreenLabel.setObjectName(u"splashScreenLabel")
        self.splashScreenLabel.setGeometry(QRect(160, 270, 491, 71))
        self.splashScreenLabel.setText("Please wait for your rice to fill")
        self.splashScreenLabel.setAlignment(Qt.AlignCenter)
        splashScreenfont1 = QFont()
        splashScreenfont1.setPointSize(24)
        self.splashScreenLabel.setFont(splashScreenfont1)
        self.splashScreenLabel.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.splashScreenLabel1 = QLabel(MainWindow)
        self.splashScreenLabel1.setObjectName(u"splashScreenLabel1")
        self.splashScreenLabel1.setGeometry(QRect(130, 60, 551, 181))
        self.splashScreenLabel1.setAlignment(Qt.AlignCenter)
        self.splashScreenLabel1.setText("Grainmate")
        self.splashScreenLabel1.setStyleSheet("color: rgb(33,123,88)") 
        self.splashScreenLabel1.setFont(titleFont)
        self.splashButton = QPushButton(MainWindow)
        self.splashButton.setGeometry(QRect(230, 330, 371, 54))
        self.splashButton.setText("Proceed")
        self.splashButton.clicked.connect(self.thankYouCard)

        self.splashButton.hide()
        self.splashScreenLabel.hide()
        self.splashScreenLabel1.hide()




           
    ####################################################################################################################
    #--------------------------------------------- ADMIN LOGIN PAGE PAGE ------------------------------------------>
    ####################################################################################################################
        AdminLogo = QFont()
        AdminLogo.setPointSize(60)
        AdminLogo.setBold(True)
        self.adminLogoLabel = QLabel(self.centralwidget)
        self.adminLogoLabel.setObjectName(u"adminLogoLabel")
        self.adminLogoLabel.setGeometry(QRect(50, -60, 701, 291))
        self.adminLogoLabel.setFont(AdminLogo)
        self.adminLogoLabel.setText("Ricemate")
        self.adminLogoLabel.setStyleSheet(u"color: rgb(30, 112, 80);")
        self.adminLogoLabel.setAlignment(Qt.AlignCenter)
        adminTextEditFont = QFont()
        adminTextEditFont.setPointSize(12)
        self.adminPasswordLineEdit2 = QLineEdit(self.centralwidget)
        self.adminPasswordLineEdit2.setObjectName(u"adminPasswordLineEdit2")
        self.adminPasswordLineEdit2.setFont(adminTextEditFont)
        self.adminPasswordLineEdit2.setGeometry(QRect(280, 220, 261, 41))
        self.adminPasswordLineEdit2.setPlaceholderText(u"Enter your pin number")
        self.adminPasswordLineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminPasswordLabel2 = QLabel(self.centralwidget)
        self.adminPasswordLabel2.setObjectName(u"adminPasswordLabel2")
        self.adminPasswordLabel2.setGeometry(QRect(230, 230, 41, 21))
        self.adminPasswordLabel2.setFont(adminTextEditFont)
        self.adminPasswordLabel2.setStyleSheet(u"color: rgb(30, 112, 80);")
        self.adminPasswordLabel2.setText("Pin:")

        self.adminTitleLabel = QLabel(self.centralwidget)
        self.adminTitleLabel.setObjectName(u"adminTitleLabel")
        self.adminTitleLabel.setGeometry(QRect(300, 180, 241, 21))
        self.adminTitleLabel.setText("Administrator Mode")
        adminLabelFont2 = QFont()
        adminLabelFont2.setPointSize(15)
        adminLabelFont2.setBold(True)
        self.adminTitleLabel.setFont(adminLabelFont2)
        self.adminTitleLabel.setStyleSheet(u"color: rgb(31, 114, 82)")
        self.adminBackButton = QPushButton(self.centralwidget)
        self.adminBackButton.setObjectName(u"adminBackButton")
        self.adminBackButton.setGeometry(QRect(20, 30, 61, 31))
        self.adminBackButton.setIcon(backIcon)
        self.adminBackButton.setText(" <<< ")
        self.adminBackButton.setFlat(True)
        self.adminBackButton.clicked.connect(self.displayHomePage)
        adminBackButtonFont3 = QFont()
        adminBackButtonFont3.setPointSize(12)
        self.adminCreateNewAccount = QPushButton(self.centralwidget)
        self.adminCreateNewAccount.setObjectName(u"adminCreateNewAccount")
        self.adminCreateNewAccount.setGeometry(QRect(200, 420, 371, 41))
        self.adminCreateNewAccount.setFont(adminBackButtonFont3)
        self.adminCreateNewAccount.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.adminCreateNewAccount.setFlat(False)
        self.adminCreateNewAccount.setText("Sign in")
        self.adminCreateNewAccount.clicked.connect(self.verifyAccount)
        
        self.icon1pushButton = QPushButton(MainWindow)
        self.icon1pushButton.setObjectName(u"icon1pushButton")
        self.icon1pushButton.setGeometry(QRect(280, 300, 41, 41))
        self.icon2pushButton = QPushButton(MainWindow)
        self.icon2pushButton.setObjectName(u"icon2pushButton")
        self.icon2pushButton.setGeometry(QRect(340, 300, 41, 41))
        self.icon3pushButton = QPushButton(MainWindow)
        self.icon3pushButton.setObjectName(u"icon3pushButton")
        self.icon3pushButton.setGeometry(QRect(460, 300, 41, 41))
        self.icon4pushButton = QPushButton(MainWindow)
        self.icon4pushButton.setObjectName(u"icon4pushButton")
        self.icon4pushButton.setGeometry(QRect(400, 300, 41, 41))
        self.icon5pushButton = QPushButton(MainWindow)
        self.icon5pushButton.setObjectName(u"icon5pushButton")
        self.icon5pushButton.setGeometry(QRect(340, 350, 41, 41))
        self.icon6pushButton = QPushButton(MainWindow)
        self.icon6pushButton.setObjectName(u"icon6pushButton")
        self.icon6pushButton.setGeometry(QRect(400, 350, 41, 41))
        self.icon7pushButton = QPushButton(MainWindow)
        self.icon7pushButton.setObjectName(u"icon7pushButton")
        self.icon7pushButton.setGeometry(QRect(280, 350, 41, 41))
        self.icon8pushButton = QPushButton(MainWindow)
        self.icon8pushButton.setObjectName(u"icon8pushButton")
        self.icon8pushButton.setGeometry(QRect(460, 350, 41, 41))
        self.icon1pushButton.clicked.connect(self.icon1Button)
        self.icon2pushButton.clicked.connect(self.icon2Button)
        self.icon3pushButton.clicked.connect(self.icon3Button)
        self.icon4pushButton.clicked.connect(self.icon4Button)
        self.icon5pushButton.clicked.connect(self.icon5Button)
        self.icon6pushButton.clicked.connect(self.icon6Button)
        self.icon7pushButton.clicked.connect(self.icon7Button)
        self.icon8pushButton.clicked.connect(self.pushButton_erase_clicked)
        self.icon1pushButton.setText("1")
        self.icon2pushButton.setText("2")
        self.icon4pushButton.setText("3")
        self.icon3pushButton.setText("4")
        self.icon5pushButton.setText("6")
        self.icon6pushButton.setText("7")   
        self.icon7pushButton.setText("5")
        self.icon8pushButton.setText("del")
        self.icon1pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon2pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon3pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon4pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon5pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon6pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon7pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon8pushButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.icon1pushButton.hide()
        self.icon2pushButton.hide()
        self.icon3pushButton.hide()
        self.icon4pushButton.hide()
        self.icon5pushButton.hide()
        self.icon6pushButton.hide()
        self.icon7pushButton.hide()
        self.icon8pushButton.hide()

        self.adminPasswordLineEdit2.hide()
        self.adminPasswordLabel2.hide()
        self.adminLogoLabel.hide()
        self.adminTitleLabel.hide()
        self.adminBackButton.hide()
        self.adminCreateNewAccount.hide()
        self.adminProductBackButton.hide()
        

               
    ####################################################################################################################
    #--------------------------------------------- ADMIN MAIN MENU PAGE ------------------------------------------>
    ####################################################################################################################
        self.adminToLandingPageButton = QPushButton(self.centralwidget)
        self.adminToLandingPageButton.setObjectName(u"adminToLandingPageButton")
        self.adminToLandingPageButton.setGeometry(QRect(20, 30, 61, 31))
        self.adminToLandingPageButton.setIcon(backIcon)
        self.adminToLandingPageButton.setFlat(True)
        self.adminToLandingPageButton.clicked.connect(self.adminReminderMessage)
        self.adminUpdateButton = QPushButton(MainWindow)
        self.adminUpdateButton.setObjectName(u"adminUpdateButton")
        self.adminUpdateButton.setGeometry(QRect(60, 230, 130, 130))
        updateIcon = QIcon()
        updateIcon.addFile(u"Graphics/updateIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adminUpdateButton.setIcon(updateIcon)
        self.adminUpdateButton.setIconSize(QSize(100, 100))
        self.adminUpdateButton.clicked.connect(self.adminUpdateProductDetails)
        self.adminNotificationButton = QPushButton(MainWindow)
        self.adminNotificationButton.setObjectName(u"adminNotificationButton")
        self.adminNotificationButton.setGeometry(QRect(250, 230, 130, 130))
        self.adminNotificationButton.setText(u"Admin Notification")
        self.adminNotificationButton.clicked.connect(self.setAlertSettings)
        self.adminSalesButton = QPushButton(MainWindow)
        self.adminSalesButton.setObjectName(u"adminSalesButton")
        self.adminSalesButton.setGeometry(QRect(430, 230, 130, 130))
        self.adminSalesButton.setText(u"Admin Sales")
        self.adminSalesButton.clicked.connect(self.setSalesData)
        self.adminSecurityButton = QPushButton(MainWindow)
        self.adminSecurityButton.setObjectName(u"adminSecurityButton")
        self.adminSecurityButton.setGeometry(QRect(610, 230, 130, 130))
        self.adminSecurityButton.setText(u"Admin Security")
        self.adminSecurityButton.clicked.connect(self.setPinVerification)
        self.updateLabel = QLabel(MainWindow)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(65, 370, 131, 20))
        self.updateLabel.setStyleSheet(u"color: rgb(31, 114, 82)")
        self.updateLabel.setText(u"Update Product Details")
        self.notificationLabel = QLabel(MainWindow)
        self.notificationLabel.setObjectName(u"notificationLabel")
        self.notificationLabel.setGeometry(QRect(270, 370, 90, 25))
        self.notificationLabel.setText("Rice Notification")
        self.salesDataLabel = QLabel(MainWindow)
        self.salesDataLabel.setObjectName(u"salesDataLabel")
        self.salesDataLabel.setGeometry(QRect(470, 370, 61, 20))
        self.salesDataLabel.setText("Sales Data")
        self.securityLabel = QLabel(MainWindow)
        self.securityLabel.setObjectName(u"securityLabel")
        self.securityLabel.setGeometry(QRect(630, 370, 81, 20))
        self.securityLabel.setText("Rice Security")
        
        self.adminAccountButton = QPushButton(MainWindow)
        self.adminAccountButton.setObjectName(u"adminAccountButton")
        self.adminAccountButton.setGeometry(QRect(710, 30, 51, 41))

        self.adminNotificationButton.hide()
        self.adminUpdateButton.hide()
        self.adminSecurityButton.hide()
        self.adminSalesButton.hide()
        self.updateLabel.hide()
        self.notificationLabel.hide()
        self.salesDataLabel.hide()
        self.securityLabel.hide()
        self.adminAccountButton.hide()
        self.adminToLandingPageButton.hide()


        #adminUpdateProducts
        self.adminUpdateBackButton = QPushButton(self.centralwidget)
        self.adminUpdateBackButton.setObjectName(u"adminUpdateBackButton")
        self.adminUpdateBackButton.setGeometry(QRect(20, 30, 61, 31))
        self.adminUpdateBackButton.setIcon(backIcon)
        self.adminUpdateBackButton.setFlat(True)
        self.adminUpdateBackButton.clicked.connect(self.adminBackButtonLang)
        
                
    ####################################################################################################################
    #--------------------------------------------- UPDATE PRODUCT PAGE ------------------------------------------>
    ####################################################################################################################
        # self.backBUtton = QPushButton(MainWindow)
        # self.backBUtton.setObjectName(u"backBUtton")
        # self.backBUtton.setGeometry(QRect(30, 20, 61, 51))
        # font = QFont()
        # font.setPointSize(13)
        # self.backBUtton.setFont(font)
        # self.backBUtton.setStyleSheet(u"image: url(:/newPrefix/Graphics/previous.png)")
        # icon = QIcon()
        # icon.addFile(u"../Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.backBUtton.setIcon(icon)
        # self.backBUtton.setIconSize(QSize(30, 30))
        # self.backBUtton.setFlat(True)
        self.adminProduct1Label = QLabel(MainWindow)
        self.adminProduct1Label.setObjectName(u"adminProduct1Label")
        self.adminProduct1Label.setGeometry(QRect(210, 160, 141, 41))
        self.adminProduct1Label.setText("Product")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        adminfont3 = QFont()
        adminfont3.setPointSize(15)
        self.adminProduct1Label.setFont(font2)
        self.adminProduct1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.spinBox = QSpinBox(MainWindow)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(510, 160, 51, 41))
        self.spinBox.setFont(adminfont3)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(4)        
        self.updateProductName1LineEdit = QLineEdit(MainWindow)
        self.updateProductName1LineEdit.setObjectName(u"updateProductName1LineEdit")
        self.updateProductName1LineEdit.setGeometry(QRect(360, 269, 201, 41))
        self.updateProductName1LineEdit.setFont(adminfont3)
        self.updateProductName1LineEdit.setFrame(True)
        self.updateProductName1LineEdit.setPlaceholderText(u"Enter Product Name")
        self.updateProductPrice1LineEdit = QLineEdit(MainWindow)
        self.updateProductPrice1LineEdit.setObjectName(u"updateProductPrice1LineEdit")
        self.updateProductPrice1LineEdit.setGeometry(QRect(360, 329, 201, 41))
        self.updateProductPrice1LineEdit.setFont(adminfont3)
        self.updateProductPrice1LineEdit.setPlaceholderText(u"Enter Product Price")
        self.adminUpdateProductName1Label = QLabel(MainWindow)
        self.adminUpdateProductName1Label.setObjectName(u"adminUpdateProductName1Label")
        self.adminUpdateProductName1Label.setGeometry(QRect(210, 279, 131, 20))
        self.adminUpdateProductName1Label.setFont(adminfont3)
        self.adminUpdateProductName1Label.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.adminUpdateProductName1Label.setText("Product Name")
        self.adminUpdateProductPrice1Label = QLabel(MainWindow)
        self.adminUpdateProductPrice1Label.setObjectName(u"adminUpdateProductPrice1Label")
        self.adminUpdateProductPrice1Label.setGeometry(QRect(210, 339, 121, 21))
        self.adminUpdateProductPrice1Label.setText("Product Price")
        self.adminUpdateProductPrice1Label.setFont(adminfont3)
        self.adminUpdateProductPrice1Label.setStyleSheet(u"color:rgb(30, 114, 81)")
        self.saveButton = QPushButton(MainWindow)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(480, 390, 75, 31))
        self.saveButton.setStyleSheet(u"background-color: rgb(74, 188, 150);")
        self.saveButton.setText(u"Save")
        self.saveButton.clicked.connect(self.productRiceLabel)
        self.cancelButton = QPushButton(MainWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(390, 390, 75, 31))
        self.cancelButton.setText(u"Cancel")
        self.adminUpdateProductName1Label_2 = QLabel(MainWindow)
        self.adminUpdateProductName1Label_2.setObjectName(u"adminUpdateProductName1Label_2")
        self.adminUpdateProductName1Label_2.setGeometry(QRect(210, 219, 151, 31))
        self.adminUpdateProductName1Label_2.setFont(adminfont3)
        self.adminUpdateProductName1Label_2.setStyleSheet(u"color: rgb(30, 114, 81)")
        self.adminUpdateProductName1Label_2.setText("Product Weight")
        #WEIGHT SPINBOX
        self.spinBox_2 = QSpinBox(MainWindow)
        self.spinBox_2.setObjectName(u"spinBox_2") 
        self.spinBox_2.setGeometry(QRect(510, 210, 51, 41))
        self.spinBox_2.setFont(adminfont3)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(12)


        self.spinBox_2.hide()
        self.adminUpdateProductName1Label_2.hide()                            
        self.spinBox.hide()
        self.adminProduct1Label.hide()
        self.updateProductName1LineEdit.hide()
        self.updateProductPrice1LineEdit.hide()
        self.adminUpdateProductName1Label.hide()
        self.adminUpdateProductPrice1Label.hide()
        self.saveButton.hide()
        self.cancelButton.hide()

    #Notification System
        #Sales Data 
        self.salesListView = QListView(MainWindow)
        self.salesListView.setObjectName(u"salesListView")
        self.salesListView.setGeometry(QRect(130, 110, 541, 251))
        self.salesDataLabel2 = QLabel(MainWindow)
        self.salesDataLabel2.setObjectName(u"salesDataLabel")
        self.salesDataLabel2.setGeometry(QRect(300, 10, 221, 81))
        salesDataLabelFont = QFont()
        salesDataLabelFont.setPointSize(34)
        self.salesDataLabel2.setFont(salesDataLabelFont)
        self.salesDataLabel2.setStyleSheet(u"color: rgb(29, 108, 77);")
        self.salesDataLabel2.setText("Sales Data")

        self.salesListView.hide()
        self.salesDataLabel2.hide()
        self.adminUpdateBackButton.hide()
        self.adminBackButton.hide()
        self.backPushButton.hide()
        self.adminProductBackButton.hide()

        
        
    ####################################################################################################################
    #--------------------------------------------- CHANGE PIN PAGE ------------------------------------------>
    ####################################################################################################################
        self.changePinConfirmButton = QPushButton(MainWindow)
        self.changePinConfirmButton.setObjectName(u"changePinConfirmButton")
        self.changePinConfirmButton.setGeometry(QRect(330, 320, 181, 51))
        self.changePinConfirmButton.setText("Confirm")
        self.changePinConfirmButton.setFont(adminBackButtonFont3)
        self.changePinConfirmButton.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.changePinConfirmButton.clicked.connect(self.pinVerificationConfirmButton)
        self.changePinLineEdit = QLineEdit(MainWindow)
        self.changePinLineEdit.setPlaceholderText("Enter Pin")
        self.changePinLineEdit.setGeometry(QRect(280, 235, 321, 51))
        self.changePinLineEdit.setFont(adminTextEditFont)
        self.changePinLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changePinLineEdit.setObjectName(u"changePinLineEdit")
        self.changePinLabel = QLabel(MainWindow)
        self.changePinLabel.setObjectName(u"changePinLlabel")
        self.changePinLabel.setGeometry(QRect(200, 240, 51, 41))
        self.changePinLabel.setText("Pin: ")
        self.changePinLabel.setFont(adminTextEditFont)
        self.changePinConfirmButton.hide()
        self.changePinLineEdit.hide()
        self.changePinLabel.hide()
    #Update Pin Password
        self.updatePinLogo = QLabel(self.centralwidget)
        self.updatePinLogo.setObjectName(u"adminLogoLabel")
        self.updatePinLogo.setGeometry(QRect(50, -60, 701, 291))
        self.updatePinLogo.setStyleSheet(u"background-image: url(:ricemate.png);")
        self.updatePinLogo.setPixmap(QPixmap(u"ricemate.png"))
        self.updatePinPushButton = QPushButton(MainWindow)
        self.updatePinPushButton.setObjectName(u"updatePinPushButton")
        self.updatePinPushButton.setGeometry(QRect(310, 390, 181, 51))
        self.updatePinPushButton.setFont(adminBackButtonFont3)
        self.updatePinPushButton.setStyleSheet("color: rgb(31, 115, 82);")
        self.updatePinPushButton.clicked.connect(self.userUpdatedPinPassword)
        self.updatePinPushButton.setText(u"Update Pin")
        self.updatePinLineEdit = QLineEdit(MainWindow)
        self.updatePinLineEdit.setObjectName(u"updatePinLineEdit")
        self.updatePinLineEdit.setGeometry(QRect(240, 200, 321, 51))
        self.updatePinLineEdit.setFont(adminTextEditFont)
        self.updatePinLineEdit.setPlaceholderText(u"Enter New Pin")
        self.updatePinNewPinLabel = QLabel(MainWindow)
        self.updatePinNewPinLabel.setObjectName(u"updatePinNewPinLabel")
        self.updatePinNewPinLabel.setGeometry(QRect(240, 150, 121, 41))
        self.updatePinNewPinLabel.setFont(adminTextEditFont)
        self.updatePinNewPinLabel.setText(u"New Pin")
        self.updatePinConfirmPinLabel = QLabel(MainWindow)
        self.updatePinConfirmPinLabel.setObjectName(u"updatePinConfirmPinLabel")
        self.updatePinConfirmPinLabel.setGeometry(QRect(240, 270, 151, 41))
        self.updatePinConfirmPinLabel.setFont(adminTextEditFont)
        self.updatePinConfirmPinLabel.setText("Confirm Pin")
        self.updatePinConfirmLineEdit = QLineEdit(MainWindow)
        self.updatePinConfirmLineEdit.setObjectName(u"updatePinConfirmLineEdit")
        self.updatePinConfirmLineEdit.setGeometry(QRect(240, 310, 321, 51))
        self.updatePinConfirmLineEdit.setFont(adminTextEditFont)
        self.updatePinConfirmLineEdit.setPlaceholderText(u"Confirm your Pin")

        self.updatePinPushButton.hide()
        self.updatePinLineEdit.hide()
        self.updatePinConfirmLineEdit.hide()
        self.updatePinNewPinLabel.hide()
        self.updatePinConfirmPinLabel.hide()
        self.updatePinLogo.hide()

        
    ####################################################################################################################
    #--------------------------------------------- ALERT MENU PAGE ------------------------------------------>
    ####################################################################################################################
        # font = QFont()
        # font.setPointSize(11)
        # Form.setFont(font)
        self.alertSettingLabel = QLabel(MainWindow)
        self.alertSettingLabel.setObjectName(u"alertSettingLabel")
        self.alertSettingLabel.setGeometry(QRect(290, 40, 201, 61))
        alertSettingfont1 = QFont()
        alertSettingfont1.setPointSize(25)
        self.alertSettingLabel.setFont(alertSettingfont1)
        self.alertSettingLabel.setText(u"Alert Setting")
        self.alertSettingItem1 = QLabel(MainWindow)
        self.alertSettingItem1.setObjectName(u"alertSettingItem1")
        self.alertSettingItem1.setGeometry(QRect(110, 170, 201, 16))
        self.alertSettingItem1.setText(u"Turn on Notifications")
        alertSettingfont2 = QFont()
        alertSettingfont2.setPointSize(15)
        self.alertSettingItem1.setFont(alertSettingfont2)
        self.alertSettingItem2 = QLabel(MainWindow)
        self.alertSettingItem2.setObjectName(u"alertSettingItem2")
        self.alertSettingItem2.setGeometry(QRect(110, 200, 261, 31))
        self.alertSettingItem2.setFont(alertSettingfont2)
        self.alertSettingItem2.setText("Near-empty Container Alert")
        self.alertSettingItem3 = QLabel(MainWindow)
        self.alertSettingItem3.setObjectName(u"alertSettingItem3")
        self.alertSettingItem3.setGeometry(QRect(110, 250, 201, 16))
        self.alertSettingItem3.setFont(alertSettingfont2)
        self.alertSettingItem3.setText("Rice Condition Alerts")
        self.alertSettingItem6 = QLabel(MainWindow)
        self.alertSettingItem6.setObjectName(u"alertSettingItem6")
        self.alertSettingItem6.setGeometry(QRect(110, 300, 201, 16))
        self.alertSettingItem6.setFont(alertSettingfont2)
        self.alertSettingItem6.setText("Sales Alert")
        self.alertSettingItem7 = QLabel(MainWindow)
        self.alertSettingItem7.setObjectName(u"alertSettingItem7")
        self.alertSettingItem7.setGeometry(QRect(110, 350, 201, 16))
        self.alertSettingItem7.setFont(alertSettingfont2)
        self.alertSettingItem7.setText("Unauthorized Sale")
        self.checkBoxItem1 = QCheckBox(MainWindow)
        self.checkBoxItem1.setObjectName(u"checkBoxItem1")
        self.checkBoxItem1.setGeometry(QRect(500, 170, 75, 20))
        self.checkBoxItem1.setText("Enable")
        self.checkBoxItem2 = QCheckBox(MainWindow)
        self.checkBoxItem2.setObjectName(u"checkBoxItem2")
        self.checkBoxItem2.setGeometry(QRect(500, 210, 75, 20))
        self.checkBoxItem2.setText("Enable")
        self.checkBoxItem3 = QCheckBox(MainWindow)
        self.checkBoxItem3.setObjectName(u"checkBoxItem3")
        self.checkBoxItem3.setGeometry(QRect(500, 250, 75, 20))
        self.checkBoxItem3.setText("Enable")
        self.checkBoxItem6 = QCheckBox(MainWindow)
        self.checkBoxItem6.setObjectName(u"checkBoxItem6")
        self.checkBoxItem6.setGeometry(QRect(500, 300, 75, 20))
        self.checkBoxItem6.setText("Enable")
        self.checkBoxItem7 = QCheckBox(MainWindow)
        self.checkBoxItem7.setObjectName(u"checkBoxItem7")
        self.checkBoxItem7.setGeometry(QRect(500, 350, 75, 20))
        self.checkBoxItem7.setText("Enable")
        self.comboBoxItem2 = QComboBox(MainWindow)
        self.comboBoxItem2.addItem("1 kg")
        self.comboBoxItem2.addItem("2 kg")
        self.comboBoxItem2.addItem("3 kg")
        self.comboBoxItem2.addItem("4 kg")
        self.comboBoxItem2.addItem("5 kg")
        self.comboBoxItem2.setObjectName(u"comboBoxItem2")
        self.comboBoxItem2.setGeometry(QRect(620, 205, 69, 31))
        self.comboBoxItem6 = QComboBox(MainWindow)
        self.comboBoxItem6.addItem("Daily")
        self.comboBoxItem6.addItem("Monthly")
        self.comboBoxItem6.setObjectName(u"comboBoxItem6")
        self.comboBoxItem6.setGeometry(QRect(620, 350, 69, 22))

        self.alertSettingLabel.hide()
        self.alertSettingItem1.hide()
        self.alertSettingItem2.hide()
        self.alertSettingItem3.hide()
        self.alertSettingItem6.hide()
        self.alertSettingItem7.hide()
        self.checkBoxItem1.hide()
        self.checkBoxItem2.hide()
        self.checkBoxItem3.hide()
        self.checkBoxItem6.hide()
        self.checkBoxItem7.hide()
        self.comboBoxItem2.hide()
        self.comboBoxItem6.hide()
        


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", u"Grainmate", None))
        #self.label2.setText("Ricemate")
        self.pushButton.setText(_translate("MainWindow", u"Tap to order", None))
        self.pushButton.setText("Tap to Order")

    # retranslateUi



    def priceToAmount1(self): #price of the product#1
        priceBox = self.sender()
        priceValue = priceBox.toPlainText()
        self.userPrice1 = int(priceValue)
    
    def priceToAmount2(self): #price of the product#2
        priceBox = self.sender()
        priceValue = priceBox.toPlainText()
        self.userPrice2 = int(priceValue)

    def priceToAmount3(self): #price of the product#3
        priceBox = self.sender()
        priceValue = priceBox.toPlainText()
        self.userPrice3 = float(priceValue)

    def displayToTotal1(self): #amount bought by the buyer in product#1
        spinbox1 = self.sender()
        value = spinbox1.value() * self.userPrice1
        self.universalTextEdit.setText(str(int(value)))
        self.textEdit.setText(str(int(value)))

    def displayToTotal2(self): #amount bought by the buyer in product#2
        spinbox2 = self.sender()
        value = spinbox2.value() * self.userPrice2
        self.universalTextEdit.setText(str(int(value)))
        self.textEdit.setText(str(int(value)))

    def displayToTotal3(self): #amount bought by the buyer in product#3
        spinbox3 = self.sender()
        value = spinbox3.value() * self.userPrice3
        self.universalTextEdit.setText(str(int(value)))
        self.textEdit.setText(str(int(value)))

    ####################################################################################################################
    #--------------------------------------------- DISPLAY HOMEPAGE ------------------------------------------>
    ####################################################################################################################
    def displayHomePage(self):
        self.hideOrders()
        self.label2.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.adminPasswordLineEdit2.hide()
        self.adminPasswordLabel2.hide()
        self.adminPasswordLineEdit2.clear()
        self.adminLogoLabel.hide()
        self.adminTitleLabel.hide()
        self.adminBackButton.hide()
        self.adminCreateNewAccount.hide()
        self.salesListView.hide()
        self.salesDataLabel2.hide()
        self.adminUpdateBackButton.hide()
        self.adminBackButton.hide()
        self.backPushButton.hide()
        self.spinBox.hide()
        self.adminProduct1Label.hide()
        self.updateProductName1LineEdit.hide()
        self.updateProductPrice1LineEdit.hide()
        self.adminUpdateProductName1Label.hide()
        self.adminUpdateProductPrice1Label.hide()
        self.saveButton.hide()
        self.cancelButton.hide()
        self.adminProductBackButton.hide()
        self.orderLabel.hide()
        self.orderLabel2.hide()
        self.orderLabel3.hide()
        self.orderLabel4.hide()
        self.orderLabel6.hide()
        self.orderLabel7.hide()
        self.orderLabel8.hide()
        self.orderPushButton1.hide()
        self.orderPushButton2.hide()
        self.orderPushButton3.hide()
        self.thankYoulabel.hide()
        self.thankYoulabel_2.hide()
        self.thankYoupushButton.hide()
        self.splashScreenLabel.hide()
        self.splashScreenLabel1.hide()
        self.amountTotalPaid.hide()
        self.amountCoinPaid.hide()
        self.instruction.show()
        self.orderWeight.hide()
        self.orderWeight2.hide()
        self.orderWeight3.hide()
        self.updatePinPushButton.hide()
        self.updatePinLineEdit.hide()
        self.updatePinConfirmLineEdit.hide()
        self.updatePinNewPinLabel.hide()
        self.updatePinConfirmPinLabel.hide()
        self.updatePinLogo.hide()
        self.temperatureSensor.hide()
        self.icon1pushButton.hide()
        self.icon2pushButton.hide()
        self.icon3pushButton.hide()
        self.icon4pushButton.hide()
        self.icon5pushButton.hide()
        self.icon6pushButton.hide()
        self.icon7pushButton.hide()
        self.icon8pushButton.hide()
    
    ####################################################################################################################
    #---------------------------- BACK TO HOME PAGE || CANCELS TRANSACTIONS ---------------------------------------->
    ####################################################################################################################
    def reminderMessage(self):
        reminder = QMessageBox(self)
        reminder.setWindowTitle("Notice")
        reminder.setText("Pressing YES will cancel your transaction. Everything will not be saved.")
        reminder.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reminder.setIcon(QMessageBox.Warning)
        button = reminder.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
            self.displayHomePage()
        else:
            print("No!")


    ####################################################################################################################
    #--------------------------------------------- ACCOUNT VERIFIER ------------------------------------------>
    ####################################################################################################################
    def verifyAccount(self):
        password = self.adminPasswordLineEdit2.text()
        with open('CSVFiles/password.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            pin = data[0]
        if password == pin:
            print("Logged In")
            self.setAdminMainMenu()

        else:
            invalidMessage = QMessageBox(self)
            invalidMessage.setWindowTitle("Invalid Input")
            invalidMessage.setText("You entered an invalid account username or password")
            invalidMessage.setStandardButtons(QMessageBox.Ok)
            invalidMessage.setIcon(QMessageBox.Warning)
            asdf = invalidMessage.exec()
            self.adminPasswordLineEdit2.clear()
            print("Invalid username or password")

    ####################################################################################################################
    #------------------------------------------ HIDE ORDERS FOR BACK BUTTON ------------------------------------------>
    ####################################################################################################################
    def hideOrders(self): #hide orders when clicking back/ cancel
        self.productTitle1.hide()
        self.productView1.hide()
        self.productLabel1.hide()
        self.productTitle2.hide()
        self.universalGroupBox.hide()
        self.productLabel2.hide()
        self.productPrice2.hide()
        self.productSpinBox1.hide()
        self.productSpinBox2.hide()
        self.productSpinBox3.hide()
        self.universalTextEdit.hide()
        self.universalConfirmButton.hide()
        self.universalCancelButton.hide()
        self.productView2.hide()
        self.productTitle3.hide()
        self.productLabel3.hide()
        self.productView3.hide()
        self.productPrice3.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.temperatureSensor.hide()
        self.adminUpdateButton.hide()
        self.adminNotificationButton.hide()
        self.adminSecurityButton.hide()
        self.adminSalesButton.hide()
        self.updateLabel.hide()
        self.notificationLabel.hide()
        self.salesDataLabel.hide()
        self.securityLabel.hide()
        self.adminAccountButton.hide()  
    def hideMainMenus(self):
        self.label2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()

    ####################################################################################################################
    #--------------------------------------------- SET MAIN MENU PAGE ------------------------------------------>
    ####################################################################################################################
    def setOrderPage(self): #MainMenue page
        self.hideOrders()
        self.temperatureSensor.show()
        self.hideMainMenus()
        self.adminBackButton.hide()
        self.adminProductBackButton.hide()
        self.adminProductBackButton.show()
        self.orderLabel.show()
        self.orderLabel2.show()
        self.orderLabel3.show()
        self.orderLabel4.show()
        self.orderLabel6.show()
        self.orderLabel7.show()
        self.orderLabel8.show()
        self.orderPushButton1.show()
        self.orderPushButton2.show()
        self.orderPushButton3.show()
        self.clearInputs()
        self.orderPushButton1.clicked.connect(self.setProduct1)
        self.orderPushButton2.clicked.connect(self.setProduct2)
        self.orderPushButton3.clicked.connect(self.setProduct3)
        self.orderWeight.show()
        self.orderWeight2.show()
        QtWidgets.QApplication.processEvents()
        #self.temperatureReading()        

    ####################################################################################################################
    #---------------------------- READ FROM THE PRODUCT DETAILS FROM CSV  ------------------------------------------>
    ####################################################################################################################
        with open('CSVFiles/product1Weight.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            loadProductWeight1 = data[0]
            self.orderWeight.setText(loadProductWeight1 + " KG")

        with open('CSVFiles/product2Weight.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            loadProductWeight2 = data[0]
            print(loadProductWeight2)

            self.orderWeight2.setText(loadProductWeight2 + " KG")


        with open('CSVFiles/product3Weight.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            loadProductWeight3 = data[0]
            self.orderWeight3.setText(loadProductWeight3 + " KG")

        with open('CSVFiles/product#1NameAndPrice.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            # print(data)
            
            loadProductLabel1 = data[0]
            loadProductPrice1 = data[1]
            print(loadProductLabel1, loadProductPrice1)

            self.orderLabel2.setText(loadProductLabel1)
            self.orderLabel6.setText(loadProductPrice1)
            self.productPrice1.setText(loadProductPrice1)
            self.productTitle1.setText(loadProductLabel1)
            self.productLabel1.setText(loadProductLabel1)

            # loadProductWeight2 = 
            # self.orderWeight2.setText(loadProductWeight2 + " KG")

        with open('CSVFiles/product#2NameAndPrice.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            loadProductLabel2 = data[0]
            loadProductPrice2 = data[1]
            self.productPrice2.setText(loadProductPrice2)
            self.orderLabel3.setText(loadProductLabel2)
            self.orderLabel7.setText(loadProductPrice2)
            self.productTitle2.setText(loadProductLabel2)
            self.productLabel2.setText(loadProductLabel2)

        with open('CSVFiles/product#3NameAndPrice.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            # loadProductWeight3 = data[0]
            loadProductLabel3 = data[0]
            loadProductPrice3 = data[1]
            # self.orderWeight3.setText(loadProductWeight3 + " KG")
            self.productPrice3.setText(loadProductPrice3)
            self.orderLabel4.setText(loadProductLabel3)
            self.orderLabel8.setText(loadProductPrice3)
            self.productTitle3.setText(loadProductLabel3)
            self.productLabel3.setText(loadProductLabel3)
        
        #Order Summary
        self.orderSummaryLabel.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.textEdit.hide()
        self.orderConfirmation.hide()
        self.orderConfirmationToCoins.hide()
        self.totalLabel.hide()

    ####################################################################################################################
    #------------------------------------- CLEAR TOTAL AND AMOUNT FIELDS ------------------------------------------>
    ####################################################################################################################
    def clearInputs(self):  # Clear Total and Amount fields 
        self.universalTextEdit.clear()
        self.productSpinBox1.clear()
        self.productSpinBox2.clear()
        self.productSpinBox3.clear()
        self.textEdit.clear()
        self.amountTotalPaidTextEdit.clear()
    
    ####################################################################################################################
    #--------------------------------------------- DISPLAY PRODUCT 1 UI ------------------------------------------>
    ####################################################################################################################

    def setProduct1(self): # UI_2.Product1
        self.label2.hide()
        self.pushButton.hide()
        self.orderLabel.hide()
        self.orderLabel2.hide()
        self.orderLabel3.hide()
        self.orderLabel4.hide()
        self.orderLabel6.hide()
        self.orderLabel7.hide()
        self.orderLabel8.hide()
        self.orderPushButton1.hide()
        self.orderPushButton2.hide()
        self.orderPushButton3.hide()
        self.productTitle1.show()
        self.productView1.show()
        self.productLabel1.show()
        self.productPrice1.show()
        self.productView1.show()
        self.productSpinBox1.show()
        self.showUniversalGroupBox()
        self.orderWeight.hide()
        self.orderWeight2.hide()
        self.orderWeight3.hide()
        self.pushButton_2.hide()
        self.temperatureSensor.hide()
    

    ####################################################################################################################
    #--------------------------------------------- DISPLAY PRODUCT 2 UI ------------------------------------------>
    ####################################################################################################################
    def setProduct2(self): # UI_2.Product2
        self.label2.hide()
        self.temperatureSensor.hide()
        self.pushButton.hide()
        self.orderLabel.hide()
        self.orderLabel2.hide()
        self.orderLabel3.hide()
        self.orderLabel4.hide()
        self.orderLabel6.hide()
        self.orderLabel7.hide()
        self.orderLabel8.hide()
        self.orderPushButton1.hide()
        self.orderPushButton2.hide()
        self.orderPushButton3.hide()
        self.orderWeight.hide()
        self.orderWeight2.hide()
        self.orderWeight3.hide()    
        self.productTitle2.show()
        self.productView2.show()
        self.productLabel2.show()
        self.productPrice2.show()
        self.productSpinBox2.show()
        self.showUniversalGroupBox()
        self.pushButton_2.hide()
  
    ####################################################################################################################
        #--------------------------------------------- DISPLAY PRODUCT 3 UI ------------------------------------------>
    ####################################################################################################################
    def setProduct3(self): # UI_2.Product3
        self.productTitle3.show()
        self.productView3.show()
        self.productLabel3.show()
        self.productPrice3.show()
        self.productSpinBox3.show()
        self.showUniversalGroupBox()
        self.label2.hide()
        self.temperatureSensor.hide()
        self.pushButton.hide()
        self.orderLabel.hide()
        self.orderLabel2.hide()
        self.orderLabel3.hide()
        self.orderLabel4.hide()
        self.orderLabel6.hide()
        self.orderLabel7.hide()
        self.orderLabel8.hide()
        self.orderPushButton1.hide()
        self.orderPushButton2.hide()
        self.orderPushButton3.hide()
        self.orderWeight.hide()
        self.orderWeight2.hide()
        self.orderWeight3.hide()
        self.pushButton_2.hide()
    

    ####################################################################################################################
    #--------------------------------------------- DISPLAY ORDER SUMMARY ------------------------------------------>
    ####################################################################################################################
    def setOrderSummary(self):  #Order Summary going to Payment
            
        self.hideOrders()
        self.adminProductBackButton.hide()
        self.temperatureSensor.hide()
#        self.instruction.show()
#        self.orderSummaryLabel.show()
#        self.orderSummaryLabelgroupBox.show()
#        self.textEdit.show()
#        self.orderConfirmationToCoins.show()
#        self.backPushButton.show()
#        self.totalLabel.show()
        self.pushButton_2.hide()
        #Calculate the reduced weight
        
        #print(int(orderedAmount))

    ####################################################################################################################
    #------------------------------------- DISPLAY ORIGINAL WEIGHT FROM WEIGHT CSV ------------------------------------>
    ####################################################################################################################
    def readOriginalWeight(self):
        with open('CSVFiles/product1Weight.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            orderedAmount = self.sender()
            orderedAmount = self.productSpinBox1.value()
            loadProductWeight1 = data[0]
            minusWeight = int(orderedAmount)

            totalWeight = int(loadProductWeight1)- minusWeight
            return totalWeight
            #self.orderWeight.setText(totalWeight + " KG")


    ####################################################################################################################
    #------------------------------------------- DISPLAY ORDER FORM GROUP BOX ----------------------------------------->
    ####################################################################################################################
    def showUniversalGroupBox(self):    #Orders universal group box
        self.universalGroupBox.show()
        self.universalTextEdit.show()
        self.universalConfirmButton.show()
        self.universalCancelButton.show()  

    ####################################################################################################################
    #--------------------------------------------- DISPLAY ORDER CONFIRMATION ------------------------------------------>
    ####################################################################################################################
    def orderConfirmed(self): #Orders confirmed
        print("confirmed order. waiting for payment")
        self.orderSummaryLabelgroupBox.show()
        self.orderSummaryLabel.show()
        self.totalLabel.show()
        self.textEdit.show()
        self.instruction.show()
        self.amountTotalPaid.hide()
        self.temperatureSensor.hide()

        #run coin and bill methods
        #if inputs == price, check plastic in the case. call ir, 
        #then if plastic is present then rice dispense method 

    ####################################################################################################################
    #-------------------------------------- DISPLAY COIN ACCEPTING PAGE ------------------------------------------>
    ####################################################################################################################
    def coins(self):
        self.hideOrders()
        self.pushButton_2.hide()
        self.adminProductBackButton.hide()
        self.splashScreenLabel.hide()
        self.splashScreenLabel1.hide()
        self.splashButton.hide()
        self.amountPaid.hide()
        self.amountPaidTextEdit.hide()
        self.instruction.hide()
        self.instruction1.show()
        self.amountCoinPaid.show()
        self.orderSummaryLabelgroupBox.show()
        self.orderSummaryLabel.show()
        self.totalLabel.show()
        self.textEdit.show()
        self.orderConfirmation.show()
        self.amountCoinPaidTextEdit.hide()
        self.amountTotalPaidTextEdit.show()
        self.temperatureSensor.hide()
        
        totalWeight = self.readOriginalWeight()
        updatedWeight = totalWeight
        with open('CSVFiles/product1Weight.csv', 'w', newline= '') as file:
            newWeight = updatedWeight
            writer = csv.writer(file)
            writer.writerow(["Product weight"])
            writer.writerow([newWeight])
        
            print(updatedWeight)
        
    def checkCoin(self, coin, temp):
            
        if self.previousValue < coin:
            print(coin)
            QtWidgets.QApplication.processEvents()
            self.amountCoinPaidTextEdit.setText(str(coin))    
            self.previousValue = coin
        else:
            pass
    
    ####################################################################################################################
    #-------------------------------------- DISPLAY TOTAL INSERTED AMOUNT PAGE ---------------------------------------->
    ####################################################################################################################   
    def displayTotalInserted(self):
        print("Running Display Total Inserted")
        self.splashScreenLabel.hide()
        self.splashScreenLabel1.hide()
        self.splashButton.hide()
        self.amountPaid.hide()
        self.amountPaidTextEdit.hide()
        self.instruction.hide()
        self.instruction1.hide()
        self.amountCoinPaid.hide()
        self.orderConfirmation.hide()
        self.orderSummaryLabelgroupBox.show()
        self.orderSummaryLabel.show()
        self.totalLabel.show()
        self.textEdit.show() #To Pay Amount
        self.verifyOrderConfirmation.show()
        self.amountTotalPaid.show()
        self.amountTotalPaidTextEdit.show()
        self.temperatureSensor.hide()
        self.amountCoinPaidTextEdit.hide()
        
 
        
    # def temperatureReading(self):
    #     print("temperature sensor running")
    #     temperature_celsius,_= read_temp()
    #     print(temperature_celsius)
    #     self.temperatureSensor.setText(f"{str(temperature_celsius)} Celsius")


    # def loadSensorReading(self):
    #         print("load sensor reading")

    #         inputted_weight = self.productSpinBox1.sender()
    #         inputted_weight = self.productSpinBox1.value()
    #         self.splashScreenLabel1.setText("Mamamooo")
    #         QtWidgets.QApplication.processEvents()
    #         while True:
    #             self.weight = get_load(inputted_weight)

    #             if self.weight != float(inputted_weight):
    #                 self.splashScreenLabel1.setText(str(self.weight))
    #                 QtWidgets.QApplication.processEvents()
    #             else:
    #                 print("staph na baby sheesh")
    #                 self.splashScreenLabel1.setText(str(self.weight))
    #                 QtWidgets.QApplication.processEvents()
    #                 break 
        
    ####################################################################################################################
    #-------------------------------------- SERVO CONTROLLER ------------------------------------------>
    ####################################################################################################################
    # def servoMethod(self):
    #     servoPin = 22
    #     factory = PiGPIOFactory()
    #     servo = AngularServo(servoPin, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)
    #     servo_relay = gpiozero.OutputDevice(servoPin, active_high=True, initial_value=False)
    #     servo.angle = 0
        
    #     amountSpinBox = self.sender()
    #     amountSpinBox = self.productSpinBox1.value()
    #     totalAmountSpinBox = int(amountSpinBox)
        
    #     if totalAmountSpinBox == 1:
    #             servo_relay.on()
    #             servo.angle = 0
    #             print(servo.angle)
    #             sleep(16.5)

    #             servo.angle = 180
    #             print(servo.angle)
    #             sleep(1)
                
    #             servo.angle = 0
    #             print(servo.angle)
                        
    #             servo_relay.off()
           
    #     elif totalAmountSpinBox == 2:
    #             servo_relay.on()
    #             servo.angle = 0
    #             print(servo.angle)
    #             sleep(33)

    #             servo.angle = 180
    #             print(servo.angle)
    #             sleep(1)
                
    #             servo.angle = 0
    #             print(servo.angle)
                
    #             servo_relay.off()
        
    #     elif totalAmountSpinBox == 3:
    #             servo_relay.on()
    #             servo.angle = 0
    #             print(servo.angle)
    #             sleep(49.5)

    #             servo.angle = 180
    #             print(servo.angle)
    #             sleep(1)
                
    #             servo.angle = 0
    #             print(servo.angle)
                
    #             servo_relay.off()
                
    #     elif totalAmountSpinBox == 4:
    #             servo_relay.on()
    #             servo.angle = 0
    #             print(servo.angle)
    #             sleep(66)

    #             servo.angle = 180
    #             print(servo.angle)
    #             sleep(1)
                
    #             servo.angle = 0
    #             print(servo.angle)
                
    #             servo_relay.off()
                
    #     elif totalAmountSpinBox == 5:
    #             servo_relay.on()
    #             servo.angle = 0
    #             print(servo.angle)
    #             sleep(82.5)

    #             servo.angle = 180
    #             print(servo.angle)
    #             sleep(1)
                
    #             servo.angle = 0
    #             print(servo.angle)
                
    #             servo_relay.off()
    #     self.thankYouCard()
        #self.loadSensorReading()
        #QtWidgets.QApplication.processEvents()

    ####################################################################################################################
    #-------------------------------------- RICE DISPENSING METHOD  ------------------------------------------>
    ####################################################################################################################
    def riceDispensing(self):
        self.temperatureSensor.hide()
        self.verifyOrderConfirmation.hide()
        self.orderConfirmation.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.orderSummaryLabel.hide()
        self.totalLabel.hide()
        self.textEdit.hide() #To Pay Amount
        self.orderConfirmation.hide()
        self.amountTotalPaid.hide()
        self.amountTotalPaidTextEdit.hide()
        #call beep
        self.splashScreenLabel.show()
        self.splashScreenLabel1.show()
        self.splashButton.show()
        self.temperatureSensor.hide()
        QtWidgets.QApplication.processEvents()
        
        
        #self.irMethod()
        #call ir method

        #if servo is closed, proceed to thankyoucard metho
    
    ####################################################################################################################
    #----------------------------------- CHECKS THE PRESENCE OF PLASTIC BAGS ---------------------------------------->
    ####################################################################################################################
    # def irMethod(self):
    #     sensor_pin = 23
    #     led_pin = 26

    #     # GPIO setup
    #     GPIO.setwarnings(False)
    #     GPIO.setmode(GPIO.BCM)
    #     GPIO.setup(sensor_pin, GPIO.IN)
    #     while sensor_pin != False:
    #             if GPIO.input(sensor_pin):
    #                     print("no object")
    #                     sleep(0.5)
    #             else:
    #                     # If an object is detected
    #                     print("object detected")
    #                     sleep(1)
    #                     self.dispensingMessage()
    #                     break
    #     self.thankYouCard()

    ####################################################################################################################
    #-------------------------------------- CHECK RICE COST == AMOUNT INPUT  ------------------------------------------>
    ####################################################################################################################
    def verifyInputPrice(self):
        toPayAmount = self.sender()
        toPayAmount = self.textEdit.text()
        PayedAmount = self.sender()
        PayedAmount = self.amountTotalPaidTextEdit.text()
        if toPayAmount == PayedAmount:
            self.riceDispensing()
        else:
            print("Failed to Pay amount")
        
        
    ####################################################################################################################
    #-------------------------------------- CONFIRMATION MESSAGE TO DISPENSE ------------------------------------------>
    ####################################################################################################################
    def dispensingMessage(self):
        reminder = QMessageBox(self)
        reminder.setWindowTitle("Confirmation")
        reminder.setText("Machine is ready to dispense rice. Press Yes if your plastic is ready.")
        reminder.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reminder.setIcon(QMessageBox.Information)
        button = reminder.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
            #self.servoMethod()
        else:
            print("No!")
            
    ####################################################################################################################
    #-------------------------------------- DISPLAY THANK YOU MESSAGE ------------------------------------------>
    ####################################################################################################################
    def thankYouCard(self):
        #self.irMethod()
        self.temperatureSensor.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.orderSummaryLabel.hide()
        self.totalLabel.hide()
        self.textEdit.hide()
        self.instruction.hide()
        self.splashScreenLabel.hide()
        self.splashScreenLabel1.hide()
        self.splashButton.hide()
        self.thankYoulabel.show()
        self.thankYoulabel_2.show()
        self.thankYoupushButton.show()
    
    ####################################################################################################################
    #-------------------------------------- DISPLAY ADMIN LOGIN PAGE ------------------------------------------>
    ####################################################################################################################
    def setAdminLandingPage(self):  #Admin Landing page UI
        self.temperatureSensor.hide()
        self.label2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.adminPasswordLineEdit2.show()
        self.adminPasswordLineEdit2.clear()
        self.adminPasswordLabel2.show()
        self.adminLogoLabel.show()
        self.adminTitleLabel.show()
        self.adminBackButton.show()
        self.adminCreateNewAccount.show()
        self.updateLabel.hide()
        self.adminUpdateButton.hide()
        self.adminNotificationButton.hide()
        self.adminSecurityButton.hide()
        self.adminSalesButton.hide()
        self.notificationLabel.hide()
        self.salesDataLabel.hide()
        self.securityLabel.hide()
        self.adminAccountButton.hide()
        self.adminUpdateBackButton.hide()
        self.spinBox.hide()
        self.adminProduct1Label.hide()
        self.updateProductName1LineEdit.hide()
        self.updateProductPrice1LineEdit.hide()
        self.adminUpdateProductName1Label.hide()
        self.adminUpdateProductPrice1Label.hide()
        self.saveButton.hide()
        self.cancelButton.hide()
        self.salesListView.hide()
        self.salesDataLabel2.hide()
        self.adminProductBackButton.hide()
        self.changePinConfirmButton.hide()
        self.changePinLineEdit.hide()
        self.changePinLabel.hide()
        self.updatePinPushButton.hide()
        self.updatePinLineEdit.hide()
        self.updatePinConfirmLineEdit.hide()
        self.updatePinNewPinLabel.hide()
        self.updatePinConfirmPinLabel.hide()
        self.updatePinLogo.hide()
        self.updatePinPushButton.hide()
        self.updatePinLineEdit.hide()
        self.updatePinConfirmLineEdit.hide()
        self.updatePinNewPinLabel.hide()
        self.updatePinConfirmPinLabel.hide()
        self.updatePinLogo.hide()
        self.hideAlertSettings()
        self.icon1pushButton.show()
        self.icon2pushButton.show()
        self.icon3pushButton.show()
        self.icon4pushButton.show()
        self.icon5pushButton.show()
        self.icon6pushButton.show()
        self.icon7pushButton.show()
        self.icon8pushButton.show()

    ####################################################################################################################
    #-------------------------------------- RETURN TO LOGIN FORM ------------------------------------------>
    ####################################################################################################################
    def adminReminderMessage(self): #To Back to Admin Landing Page - login form
        adminReminder = QMessageBox(self)
        adminReminder.setWindowTitle("Notice")
        adminReminder.setText("Pressing YES will return you to login form.")
        adminReminder.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        adminReminder.setIcon(QMessageBox.Warning)
        adminButton = adminReminder.exec()

        if adminButton == QMessageBox.Yes:
            print("Yes!")
            self.setAdminLandingPage()
        else:
            print("No!")

    ####################################################################################################################
    #------------------------------------- BUTTONS FOR TOUCHSCREEN PIN NUMBERS ----------------------------------------->
    ####################################################################################################################
    
    def icon1Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '1')

    def icon2Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '2')

    def icon4Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '3')

    def icon3Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '4')

    def icon7Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '5')

    def icon5Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '6')

    def icon6Button(self):
        self.adminPasswordLineEdit2.setText(self.adminPasswordLineEdit2.text() + '7')


    ####################################################################################################################
    #-------------------------------------- INPUT ERASER ------------------------------------------>
    ####################################################################################################################
    def pushButton_erase_clicked(self):
        text = self.adminPasswordLineEdit2.text()
        textLength = len(text)
        if(textLength):
            newtext = text[:textLength - 1]
            self.adminPasswordLineEdit2.setText(newtext)


    ####################################################################################################################
    #-------------------------------------- ADMIN BACK BUTTON ------------------------------------------>
    ####################################################################################################################  
    def adminBackButtonLang(self):
        self.setAdminMainMenu()
        self.salesListView.hide()
        self.salesDataLabel2.hide()
        self.adminUpdateBackButton.hide()
        self.icon1pushButton.hide()
        self.icon2pushButton.hide()
        self.icon3pushButton.hide()
        self.icon4pushButton.hide()
        self.icon5pushButton.hide()
        self.icon6pushButton.hide()
        self.icon7pushButton.hide()
        self.icon8pushButton.hide()
        self.temperatureSensor.hide()
        
    ####################################################################################################################
    #-------------------------------------- DISPLAY ADMIN MAIN MENU ------------------------------------------>
    ####################################################################################################################
    def setAdminMainMenu(self): #Admin Main Menu (Update Products, Unregistered Sales, Sales Data)
        self.temperatureSensor.hide()
        self.adminUpdateButton.show()
        self.adminSecurityButton.show()
        self.adminSalesButton.show()
        self.adminNotificationButton.show()
        self.updateLabel.show()
        self.notificationLabel.show()
        self.salesDataLabel.show()
        self.securityLabel.show()
        self.adminAccountButton.show()
        self.adminPasswordLineEdit2.hide()
        self.adminPasswordLabel2.hide()
        self.adminLogoLabel.show()
        self.adminTitleLabel.hide()
        self.adminCreateNewAccount.hide()
        self.changePinConfirmButton.hide()
        self.changePinLineEdit.hide()
        self.changePinLabel.hide()
        self.updatePinLogo.hide()
        self.spinBox_2.hide()
        self.adminUpdateProductName1Label_2.hide()                            
        self.spinBox.hide()
        self.adminProduct1Label.hide()
        self.updateProductName1LineEdit.hide()
        self.updateProductPrice1LineEdit.hide()
        self.adminUpdateProductName1Label.hide()
        self.adminUpdateProductPrice1Label.hide()
        self.saveButton.hide()
        self.cancelButton.hide()
        self.adminToLandingPageButton.hide()
        self.adminUpdateBackButton.hide()
        self.hideAlertSettingsButton() #hide alert settings button
        self.updatePinPushButton.hide()
        self.updatePinLineEdit.hide()
        self.updatePinConfirmLineEdit.hide()
        self.updatePinNewPinLabel.hide()
        self.updatePinConfirmPinLabel.hide()
        self.updatePinLogo.hide()
        self.icon1pushButton.hide()
        self.icon2pushButton.hide()
        self.icon3pushButton.hide()
        self.icon4pushButton.hide()
        self.icon5pushButton.hide()
        self.icon6pushButton.hide()
        self.icon7pushButton.hide()
        self.icon8pushButton.hide()

    ####################################################################################################################
    #-------------------------------------- DISPLAY THANK YOU MESSAGE ------------------------------------------>
    ####################################################################################################################
    def adminUpdateProductDetails(self):    #Update Products
        self.adminUpdateBackButton.show()
        self.adminProduct1Label.show()
        self.updateProductName1LineEdit.show()
        self.updateProductPrice1LineEdit.show()
        self.adminUpdateProductName1Label.show()
        self.adminUpdateProductPrice1Label.show()
        #self.adminLogoLabel.show()
        self.saveButton.show()
        self.cancelButton.show()
        self.spinBox.show()
        self.hideAdminMainMenu()
        self.adminUpdateButton.hide()
        self.adminNotificationButton.hide()
        self.adminSecurityButton.hide()
        self.adminSalesButton.hide()
        self.updateLabel.hide()
        self.notificationLabel.hide()
        self.salesDataLabel.hide()
        self.securityLabel.hide()
        self.updatePinLogo.show()
        self.adminLogoLabel.hide()
        self.spinBox_2.show()
        self.adminUpdateProductName1Label_2.show()    
        self.temperatureSensor.hide()
        # self.adminAccountButton.hide()

    ####################################################################################################################
    #-------------------------------------- HIDE ADMIN MAIN MENU ------------------------------------------>
    ####################################################################################################################
    def hideAdminMainMenu(self): 
        self.adminUpdateButton.hide()
        self.adminNotificationButton.hide()
        self.adminSecurityButton.hide()
        self.adminSalesButton.hide()
        self.notificationLabel.hide()
        self.salesDataLabel.hide()
        self.securityLabel.hide()
        self.adminAccountButton.hide()
        self.adminPasswordLineEdit2.hide()
        self.adminPasswordLabel2.hide()
        self.adminTitleLabel.hide()
        self.adminBackButton.show()
        self.adminCreateNewAccount.hide()
        self.adminProductBackButton.hide()
        self.changePinConfirmButton.hide()
        self.changePinLineEdit.hide()
        self.changePinLabel.hide()
        self.updatePinPushButton.hide()
        self.updatePinLineEdit.hide()
        self.updatePinConfirmLineEdit.hide()
        self.updatePinNewPinLabel.hide()
        self.updatePinConfirmPinLabel.hide()
        self.spinBox_2.hide()
        self.adminUpdateProductName1Label_2.hide()    


    ####################################################################################################################
    #-------------------------------------- DISPLAY SALES DATA (TO BE REMOVED???) ------------------------------------------>
    ####################################################################################################################
    def setSalesData(self): #Show the contents of the Sales Data UI
        self.hideAdminMainMenu()
        self.adminLogoLabel.hide()
        self.salesListView.show()
        self.salesDataLabel2.show()
        self.adminUpdateBackButton.show()
        self.label2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.updateLabel.hide ()
    
    
    ####################################################################################################################
    #-------------------------------------- PRODUCT DETAILS UPDATER ------------------------------------------>
    ####################################################################################################################
    def productRiceLabel(self): #Calls UpdateProductFunctions in every spinbox
        productLabel= self.sender()
        productLabel = self.updateProductName1LineEdit.text()
        productWeight = self.sender()
        productWeight = self.spinBox_2.value()

        print("productLabel = ", productLabel)
        print("productWeight = ", productWeight)
        if self.spinBox.value() == 1:
            if productLabel == None:
                self.getWeight1FromAdmin()
            else:
                self.getWeight1FromAdmin()
                self.getItemInProduct1DetailCSV()

        elif self.spinBox.value() == 2:
            if productLabel == None:
                self.getWeight2FromAdmin()
            else:
                self.getWeight2FromAdmin()
                self.getItemInProduct2DetailCSV()

        elif self.spinBox.value() == 3: # TO FOLLOW
            if productLabel == None:
                self.getWeight3FromAdmin()
            else:
                self.getWeight3FromAdmin()
                self.getItemInProduct3DetailCSV()

    def getItemInProduct1DetailCSV(self): #Product#1
        with open('CSVFiles/product#1NameAndPrice.csv', 'w', newline='') as file:
            updatedProductLabel = self.sender()
            updatedProductLabel = self.updateProductName1LineEdit.text()
            updatedProductPrice = self.sender()
            updatedProductPrice = self.updateProductPrice1LineEdit.text()
            writer = csv.writer(file)
            writer.writerow(["Product name", "Product price"])
            writer.writerow([updatedProductLabel, updatedProductPrice])

    def getItemInProduct2DetailCSV(self): #Product#2
        updatedProductLabel = self.sender()
        updatedProductLabel = self.updateProductName1LineEdit.text()
        updatedProductPrice = self.sender()
        updatedProductPrice = self.updateProductPrice1LineEdit.text()
        with open('CSVFiles/product#2NameAndPrice.csv', 'w', newline='') as file:
            updatedProductLabel = self.sender()
            updatedProductLabel = self.updateProductName1LineEdit.text()
            updatedProductPrice = self.sender()
            updatedProductPrice = self.updateProductPrice1LineEdit.text()
            writer = csv.writer(file)
            writer.writerow(["Product name", "Product price"])
            writer.writerow([updatedProductLabel, updatedProductPrice])

    def getItemInProduct3DetailCSV(self): #Product#3
        updatedProductLabel = self.sender()
        updatedProductLabel = self.updateProductName1LineEdit.text()
        updatedProductPrice = self.sender()
        updatedProductPrice = self.updateProductPrice1LineEdit.text()
        with open('CSVFiles/product#3NameAndPrice.csv', 'w', newline='') as file:
            updatedProductLabel = self.sender()
            updatedProductPrice = self.sender()
            updatedProductLabel = self.updateProductName1LineEdit.text()
            updatedProductPrice = self.updateProductPrice1LineEdit.text()
            writer = csv.writer(file)
            writer.writerow(["Product name", "Product price"])
            writer.writerow([updatedProductLabel, updatedProductPrice])
    
    def getWeight1FromAdmin(self):
        with open('CSVFiles/product1Weight.csv', 'w', newline='') as file:
            product1Weight = self.sender()
            product1Weight = self.spinBox_2.value()
            writer = csv.writer(file)
            writer.writerow(["Product weight",])
            writer.writerow([product1Weight,])
    def getWeight2FromAdmin(self):
        with open('CSVFiles/product2Weight.csv', 'w', newline='') as file:
            product2Weight = self.sender()
            product2Weight = self.spinBox_2.value()
            writer = csv.writer(file)
            writer.writerow(["Product weight",])
            writer.writerow([product2Weight,])
    def getWeight3FromAdmin(self):
        with open('CSVFiles/product3Weight.csv', 'w', newline='') as file:
            product3Weight = self.sender()
            product3Weight = self.spinBox_2.value()
            writer = csv.writer(file)
            writer.writerow(["Product weight",])
            writer.writerow([product3Weight,])

    
    ####################################################################################################################
    #-------------------------------------- PIN UPDATER ------------------------------------------>
    ####################################################################################################################
    def setPinVerification(self):
        self.changePinConfirmButton.show()
        self.changePinLineEdit.show()
        self.changePinLabel.show()
        self.adminNotificationButton.hide()
        self.adminUpdateButton.hide()
        self.adminSecurityButton.hide()
        self.adminSalesButton.hide()
        self.updateLabel.hide()
        self.notificationLabel.hide()
        self.salesDataLabel.hide()
        self.securityLabel.hide()
        self.adminAccountButton.hide()
        self.adminUpdateBackButton.show()
        self.temperatureSensor.hide()
        #self.adminToLandingPageButton.show()

    def setUpdatePinPassword(self):
        self.updatePinPushButton.show()
        self.updatePinLineEdit.show()
        self.updatePinConfirmLineEdit.show()
        self.updatePinNewPinLabel.show()
        self.updatePinConfirmPinLabel.show()
        self.updatePinLogo.show()
        self.changePinConfirmButton.hide()
        self.changePinLineEdit.hide()
        self.changePinLabel.hide()
        self.adminLogoLabel.hide()
        self.temperatureSensor.hide()

    def userUpdatedPinPassword(self):
        updatedPinLabel= self.sender()
        updatedPinLabel = self.updatePinLineEdit.text()
        finalUpdatedPinLabel = self.sender()
        finalUpdatedPinLabel = self.updatePinConfirmLineEdit.text()

        if updatedPinLabel == finalUpdatedPinLabel:
            pinPasswords = [
                [finalUpdatedPinLabel],
            ]

            file = open('CSVFiles/password.csv', 'a', newline='')
            writer = csv.writer(file)
            writer.writerows(pinPasswords)
            file.close()


    ####################################################################################################################
    #-------------------------------------- STORE THE UPDATED PIN TO CSV ------------------------------------------>
    ####################################################################################################################
    def pinVerificationConfirmButton(self): #use CSV to store the updated passwords
        with open('CSVFiles/password.csv', 'r') as csv:
            data = [[x.strip() for x in line.strip().split(',')] for line in csv.readlines()][-1]
            pin = data[0]
        if self.changePinLineEdit.text() == pin:
            self.setUpdatePinPassword()

            # updatedPinPassword = self.sender()
            # updatedPinPassword = self.changePinLineEdit.text()


    ####################################################################################################################
    #-------------------------------------- HIDE ALERT SETTIGS ------------------------------------------>
    ####################################################################################################################
    def hideAlertSettingsButton(self):
        self.temperatureSensor.hide()
        self.alertSettingLabel.hide()
        self.alertSettingItem1.hide()
        self.alertSettingItem2.hide()
        self.alertSettingItem3.hide()
        self.alertSettingItem6.hide()
        self.alertSettingItem7.hide()
        self.checkBoxItem1.hide()
        self.checkBoxItem2.hide()
        self.checkBoxItem3.hide()
        self.checkBoxItem6.hide()
        self.checkBoxItem7.hide()
        self.comboBoxItem2.hide()
        self.comboBoxItem6.hide()



    ####################################################################################################################
    #-------------------------------------- DISPLAY NOTIFICATION ------------------------------------------>
    ####################################################################################################################
    def setAlertSettings(self): #Notifications
        self.alertSettingLabel.show()
        self.alertSettingItem1.show()
        self.alertSettingItem2.show()
        self.alertSettingItem3.show()
        self.alertSettingItem6.show()
        self.alertSettingItem7.show()
        self.checkBoxItem1.show()
        self.checkBoxItem2.show()
        self.checkBoxItem3.show()
        self.checkBoxItem6.show()
        self.checkBoxItem7.show()
        self.comboBoxItem2.show()
        self.comboBoxItem6.show()
        self.hideAdminMainMenu()
        self.adminUpdateBackButton.show()
        self.adminLogoLabel.hide()
        self.label2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.updateLabel.hide()
    
    
    ####################################################################################################################
    #-------------------------------------- HIDE ALERT  ------------------------------------------>
    ####################################################################################################################
    def hideAlertSettings(self):
        self.alertSettingLabel.hide()
        self.alertSettingItem1.hide()
        self.alertSettingItem2.hide()
        self.alertSettingItem3.hide()
        self.alertSettingItem6.hide()
        self.alertSettingItem7.hide()
        self.checkBoxItem1.hide()
        self.checkBoxItem2.hide()
        self.checkBoxItem3.hide()
        self.checkBoxItem6.hide()
        self.checkBoxItem7.hide()
        self.comboBoxItem2.hide()
        self.comboBoxItem6.hide()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())