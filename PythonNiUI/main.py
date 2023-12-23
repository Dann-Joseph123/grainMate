import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui, QtWidgets

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
        self.pushButton.clicked.connect(self.setOrderPage)
        font = QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(720, 30, 51, 41))
        self.pushButton_2.setStyleSheet(u"image: url(home.png)")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.clicked.connect(self.setAdminLandingPage)
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
        self.orderLabel5.setGeometry(QRect(620, 260, 100, 41))
        self.orderLabel5.setFont(font1)
        self.orderLabel5.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.orderLabel5.setText("Red Rice")
        self.orderLabel5.hide()
        self.orderLabel6 = QLabel(self.centralwidget)
        self.orderLabel6.setObjectName(u"orderLabel6")
        self.orderLabel6.setGeometry(QRect(100, 310, 81, 21))
        font2 = QFont()
        font2.setPointSize(10       )
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
        self.orderLabel8.setText("P. 48.00")
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
        icon3.addFile(u"Graphics\Red rice.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderPushButton4.setIcon(icon3)
        self.orderPushButton4.setIconSize(QSize(195, 140))
        self.orderPushButton4.hide()
        


        #Dinorado Order Amount
        self.productTitle1 = QLabel(self.centralwidget)
        self.productTitle1.setObjectName(u"label")
        self.productTitle1.setGeometry(QRect(290, 40, 211, 61))
        font = QFont()
        font.setPointSize(24)
        self.universalGroupBox = QGroupBox(self.centralwidget)
        self.universalGroupBox.setObjectName(u"productGroupBox1")
        self.universalGroupBox.setGeometry(QRect(281, 120, 431, 201))
        self.universalGroupBox.hide()
        self.universalTextEdit = QTextEdit(self.universalGroupBox)
        self.universalTextEdit.setObjectName(u"productTextEdit1")
        self.universalTextEdit.setEnabled(True)
        self.universalTextEdit.setGeometry(QRect(290, 30, 104, 51))
        self.universalTextEdit.setReadOnly(True)
        self.universalTextEdit.setFont(font1)
        self.universalTextEdit.hide()
        self.universalConfirmButton = QPushButton(self.universalGroupBox)
        self.universalConfirmButton.setObjectName(u"productConfirmButton1")
        self.universalConfirmButton.setGeometry(QRect(300, 150, 91, 31))
        self.universalConfirmButton.setStyleSheet(u"background-color: rgb(66, 107, 31);\n" "color: rgb(240, 240, 240);\n" "font: 10pt \"MS Shell Dlg 2\";")
        self.universalConfirmButton.setText(u"Confirm")
        self.universalCancelButton = QPushButton(self.universalGroupBox)
        self.universalCancelButton.setObjectName(u"productCancelButton1")
        self.universalCancelButton.setGeometry(QRect(200, 150, 91, 31))
        self.universalCancelButton.setStyleSheet(u"background-color: rgb(254, 0, 0);\n""font: 10pt \"MS Shell Dlg 2\";\n""color: rgb(240, 240, 240);")
        self.universalCancelButton.setText(u"Cancel")
        self.productTitle1.setFont(font)
        self.productTitle1.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle1.setText(u"Dinorado")
        self.productTitle1.hide()
        self.productLabel1 = QLabel(self.universalGroupBox)
        self.productLabel1.setObjectName(u"productLabel1")
        self.productLabel1.setGeometry(QRect(30, 10, 121, 31))
        self.productLabel1.setText(u"Dinorado")
        font1 = QFont()
        font1.setPointSize(14)
        self.productLabel1.setFont(font1)
        self.productLabel1.hide()
        self.productPrice1 = QTextEdit(self.universalGroupBox)
        self.productPrice1.setObjectName(u"productPrice1")
        self.productPrice1.setGeometry(QRect(30, 40, 80, 31))
        self.productPrice1.setEnabled(True)
        self.productPrice1.setReadOnly(False)
        font2 = QFont()
        font2.setPointSize(11)
        self.productPrice1.setFont(font2)
        self.productPrice1.hide()
        self.productView1= QGraphicsView(self.centralwidget)
        self.productView1.setObjectName(u"productView1")
        self.productView1.setGeometry(QRect(80, 120, 201, 201))
        self.productView1.hide()
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        self.universalConfirmButton.clicked.connect(self.setOrderSummary)
        self.productSpinBox1 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox1.setObjectName(u"productSpinBox1")
        spinBoxFontSize = QFont()
        spinBoxFontSize.setPointSize(15)
        self.productSpinBox1.setFont(spinBoxFontSize)
        self.productSpinBox1.setGeometry(QRect(30, 90, 81, 41))
        self.productSpinBox1.setMaximum(10      )
        self.productSpinBox1.hide()

        self.productSpinBox1.valueChanged.connect(self.displayToTotal1)
        self.productPrice1.textChanged.connect(self.priceToAmount1)

        #Sinandomeng Order Amount
        self.productTitle2 = QLabel(self.centralwidget)
        self.productTitle2.setObjectName(u"label")
        self.productTitle2.setGeometry(QRect(290, 40, 211, 61))
        self.productTitle2.setFont(font)
        self.productTitle2.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle2.setText(u"Sinandomeng")
        self.productTitle2.hide()
        self.productLabel2 = QLabel(self.universalGroupBox)
        self.productLabel2.setObjectName(u"sinandomengLabel")
        self.productLabel2.setGeometry(QRect(30, 10, 121, 31))
        self.productLabel2.setText(u"Sinandomeng")
        self.productLabel2.setFont(font1)
        self.productLabel2.hide()
        self.productPrice2 = QTextEdit(self.universalGroupBox)
        self.productPrice2.setObjectName(u"sinandomengPrice")
        self.productPrice2.setGeometry(QRect(30, 40, 80, 31))
        self.productPrice2.setEnabled(True)
        self.productPrice2.setReadOnly(False)
        self.productPrice2.setFont(font2)
        self.productPrice2.hide()
        self.productView2 = QGraphicsView(self.centralwidget)
        self.productView2.setObjectName(u"sinandomengView")
        self.productView2.setGeometry(QRect(80, 120, 201, 201))
        self.productView2.hide()
        self.productSpinBox2 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox2.setObjectName(u"productSpinBox2")
        self.productSpinBox2.setFont(spinBoxFontSize)
        self.productSpinBox2.setGeometry(QRect(30, 90, 81, 41))
        self.productSpinBox2.setMaximum(10      )
        self.productSpinBox2.hide()
        self.productPrice2.textChanged.connect(self.priceToAmount2)  
        self.productSpinBox2.valueChanged.connect(self.displayToTotal2)
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        self.universalConfirmButton.clicked.connect(self.setOrderSummary)
        
        #jasmine Rice

        self.productTitle3 = QLabel(self.centralwidget)
        self.productTitle3.setObjectName(u"label")
        self.productTitle3.setGeometry(QRect(290, 40, 211, 61))
        self.productTitle3.setFont(font)
        self.productTitle3.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle3.setText(u"Sinandomeng")
        self.productTitle3.hide()
        self.productLabel3 = QLabel(self.universalGroupBox)
        self.productLabel3.setObjectName(u"productLabel3")
        self.productLabel3.setGeometry(QRect(30, 10, 121, 31))
        self.productLabel3.setText(u"Sinandomeng")
        self.productLabel3.setFont(font1)
        self.productLabel3.hide()
        self.productPrice3 = QTextEdit(self.universalGroupBox)
        self.productPrice3.setObjectName(u"productPrice3")
        self.productPrice3.setGeometry(QRect(30, 40, 80, 31))
        self.productPrice3.setEnabled(True)
        self.productPrice3.setReadOnly(False)
        self.productPrice3.setFont(font2)
        self.productPrice3.hide()
        self.productView3 = QGraphicsView(self.centralwidget)
        self.productView3.setObjectName(u"productView3")
        self.productView3.setGeometry(QRect(80, 120, 201, 201))
        self.productView3.hide()
        self.productSpinBox3 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox3.setObjectName(u"productSpinBox3")
        self.productSpinBox3.setFont(spinBoxFontSize)
        self.productSpinBox3.setGeometry(QRect(30, 90, 81, 41))
        self.productSpinBox3.setMaximum(10      )
        self.productSpinBox3.hide()
        self.productPrice3.textChanged.connect(self.priceToAmount3)  
        self.productSpinBox3.valueChanged.connect(self.displayToTotal3)
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        self.universalConfirmButton.clicked.connect(self.setOrderSummary)


        #RED RICE
        self.productTitle4 = QLabel(self.centralwidget)
        self.productTitle4.setObjectName(u"productTitle4")
        self.productTitle4.setGeometry(QRect(350, 40, 131, 61))
        self.productTitle4.setFont(font)
        self.productTitle4.setStyleSheet(u"color: rgb(33, 123, 88);")
        self.productTitle4.setText(u"Red Rice")
        self.productLabel4 = QLabel(self.universalGroupBox)
        self.productLabel4.setObjectName(u"productLabel4")
        self.productLabel4.setGeometry(QRect(30, 10, 121, 31))
        self.productLabel4.setFont(font1)
        self.productLabel4.setText(u"Red Rice")
        self.productPrice4 = QTextEdit(self.universalGroupBox)
        self.productPrice4.setObjectName(u"productPrice4")
        self.productPrice4.setGeometry(QRect(30, 40, 80, 31))
        self.productPrice4.setFont(font2)
        self.productPrice4.setReadOnly(False)
        self.productPrice4.setEnabled(True)
        self.productView4 = QGraphicsView(self.centralwidget)
        self.productView4.setObjectName(u"productView4")
        self.productView4.setGeometry(QRect(90, 120, 201, 201))
        self.productSpinBox4 = QDoubleSpinBox(self.universalGroupBox)
        self.productSpinBox4.setObjectName(u"productSpinBox4")
        self.productSpinBox4.setFont(spinBoxFontSize)
        self.productSpinBox4.setGeometry(QRect(30, 90, 81, 41))
        self.productSpinBox4.setMaximum(10      )
        self.productSpinBox4.hide()
        self.productTitle4.hide()
        self.productView4.hide()
        self.productPrice4.hide()
        self.productLabel4.hide()
        self.universalCancelButton.clicked.connect(self.setOrderPage)
        self.universalConfirmButton.clicked.connect(self.setOrderSummary)
        self.productPrice4.textChanged.connect(self.priceToAmount4)  
        self.productSpinBox4.valueChanged.connect(self.displayToTotal4)

        #OrderSummary
        self.orderSummaryLabelgroupBox = QGroupBox(self.centralwidget)
        self.orderSummaryLabelgroupBox.setObjectName(u"groupBox")
        self.orderSummaryLabelgroupBox.setGeometry(QRect(110, 10, 581, 361))
        self.orderSummaryLabel = QLabel(self.orderSummaryLabelgroupBox)
        self.orderSummaryLabel.setObjectName(u"orderSummaryLabel")
        self.orderSummaryLabel.setGeometry(QRect(50, 50, 261, 51))
        font = QFont()
        font.setPointSize(26)
        self.orderSummaryLabel.setFont(font)
        self.orderSummaryLabel.setText(u"Order Summary")
        self.totalLabel = QLabel(self.orderSummaryLabelgroupBox)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setGeometry(QRect(60, 120, 91, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.totalLabel.setFont(font1)
        self.totalLabel.setText("Total")
        self.textEdit = QTextEdit(self.orderSummaryLabelgroupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(350, 110, 181, 61))
        font2 = QFont()
        font2.setPointSize(22)
        self.textEdit.setFont(font2)
        self.textEdit.setReadOnly(True)
        self.orderConfirmation = QPushButton(self.orderSummaryLabelgroupBox)
        self.orderConfirmation.setObjectName(u"orderConfirmation")
        self.orderConfirmation.setGeometry(QRect(100, 280, 381, 41))
        font3 = QFont()
        font3.setPointSize(10       )
        self.orderConfirmation.setFont(font3)
        self.orderConfirmation.setMouseTracking(True)
        self.orderConfirmation.setTabletTracking(True)
        self.orderConfirmation.setStyleSheet(u"background-color: rgb(109, 109, 109); ""\n""color: rgb(241, 251, 249);")
        self.orderConfirmation.setFlat(False)
        self.orderConfirmation.setText("Continue to Payment")
        self.instructionLabel = QLabel(self.orderSummaryLabelgroupBox)
        self.instructionLabel.setObjectName(u"instructionLabel")
        self.instructionLabel.setGeometry(QRect(190, 250, 221, 16))
        self.instructionLabel.setFont(font3)
        self.instructionLabel.setText(u"Please insert the exact amount")
        self.backPushButton = QPushButton(self.orderSummaryLabelgroupBox)
        self.backPushButton.setObjectName(u"pushButton")
        self.backPushButton.setGeometry(QRect(20, 20, 51, 24))
        backIcon = QIcon()
        backIcon.addFile(u"Graphics/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backPushButton.setIcon(backIcon)
        self.backPushButton.setFlat(True)
        self.backPushButton.clicked.connect(self.reminderMessage)
        
        self.orderSummaryLabel.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.textEdit.hide()
        self.orderConfirmation.hide()
        self.instructionLabel.hide()
        self.backPushButton.hide()
        self.totalLabel.hide()


        #Admin Landing Page
        self.adminUserNameTextEdit = QTextEdit(self.centralwidget)
        self.adminUserNameTextEdit.setObjectName(u"adminUserNameTextEdit")
        self.adminUserNameTextEdit.setGeometry(QRect(310, 230, 261, 41))
        adminTextEditFont = QFont()
        adminTextEditFont.setPointSize(14)
        self.adminUserNameTextEdit.setFont(adminTextEditFont)
        self.adminUserNameTextEdit.setFrameShape(QFrame.Panel)
        self.adminPasswrodTextEdit2 = QTextEdit(self.centralwidget)
        self.adminPasswrodTextEdit2.setObjectName(u"adminPasswrodTextEdit2")
        self.adminPasswrodTextEdit2.setFont(adminTextEditFont)
        self.adminPasswrodTextEdit2.setGeometry(QRect(310, 290, 261, 41))
        self.adminPasswrodTextEdit2.setFrameShape(QFrame.Panel)
        self.adminUserNameLabel = QLabel(self.centralwidget)
        self.adminUserNameLabel.setObjectName(u"adminUserNameLabel")
        self.adminUserNameLabel.setGeometry(QRect(200, 240, 101, 21))
        self.adminUserNameLabel.setFont(adminTextEditFont)
        self.adminUserNameLabel.setStyleSheet(u"color: rgb(32, 119, 85);")
        self.adminUserNameLabel.setText("Username:")
        self.adminPasswordLabel2 = QLabel(self.centralwidget)
        self.adminPasswordLabel2.setObjectName(u"adminPasswordLabel2")
        self.adminPasswordLabel2.setGeometry(QRect(200, 290, 91, 31))
        self.adminPasswordLabel2.setFont(adminTextEditFont)
        self.adminPasswordLabel2.setStyleSheet(u"color: rgb(30, 112, 80);")
        self.adminPasswordLabel2.setText("Password:")
        self.adminLogoLabel = QLabel(self.centralwidget)
        self.adminLogoLabel.setObjectName(u"adminLogoLabel")
        self.adminLogoLabel.setGeometry(QRect(50, -60, 701, 291))
        self.adminLogoLabel.setStyleSheet(u"background-image: url(:/newPrefix/ricemate.png);")
        self.adminLogoLabel.setFrameShape(QFrame.NoFrame)
        self.adminLogoLabel.setLineWidth(1)
        self.adminLogoLabel.setPixmap(QPixmap(u"ricemate.png"))
        self.adminLogoLabel.setScaledContents(False)
        self.adminLogoLabel.setAlignment(Qt.AlignCenter)
        self.adminTitleLabel = QLabel(self.centralwidget)
        self.adminTitleLabel.setObjectName(u"adminTitleLabel")
        self.adminTitleLabel.setGeometry(QRect(300, 190, 241, 21))
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
        self.adminBackButton.setFlat(True)
        self.adminBackButton.clicked.connect(self.displayHomePage)
        self.adminCreateNewAccount = QPushButton(self.centralwidget)
        self.adminCreateNewAccount.setObjectName(u"adminCreateNewAccount")
        self.adminCreateNewAccount.setGeometry(QRect(230, 350, 371, 24))
        adminBackButtonFont3 = QFont()
        adminBackButtonFont3.setPointSize(12)
        self.adminCreateNewAccount.setFont(adminBackButtonFont3)
        self.adminCreateNewAccount.setStyleSheet(u"color: rgb(31, 115, 82);")
        self.adminCreateNewAccount.setFlat(True)
        self.adminCreateNewAccount.setText("Create New Account")

        self.adminUserNameTextEdit.hide()
        self.adminPasswrodTextEdit2.hide()
        self.adminUserNameLabel.hide()
        self.adminPasswordLabel2.hide()
        self.adminLogoLabel.hide()
        self.adminTitleLabel.hide()
        self.adminBackButton.hide()
        self.adminCreateNewAccount.hide()
        

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
        self.userPrice3 = int(priceValue)

    def priceToAmount4(self): #price of the product#4
        priceBox = self.sender()
        priceValue = priceBox.toPlainText()
        self.userPrice4 = int(priceValue)

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

    def displayToTotal4(self): #amount bought by the buyer in product#4
        spinbox4 = self.sender()
        value = spinbox4.value() * self.userPrice4
        self.universalTextEdit.setText(str(int(value)))
        self.textEdit.setText(str(int(value)))

    def displayHomePage(self):
        self.hideOrders()
        self.label2.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.adminUserNameTextEdit.hide()
        self.adminPasswrodTextEdit2.hide()
        self.adminUserNameLabel.hide()
        self.adminPasswordLabel2.hide()
        self.adminLogoLabel.hide()
        self.adminTitleLabel.hide()
        self.adminBackButton.hide()
        self.adminCreateNewAccount.hide()
    
    def reminderMessage(self):
        reminder = QMessageBox(self)
        reminder.setWindowTitle("Notice")
        reminder.setText("This is a question dialog")
        reminder.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reminder.setIcon(QMessageBox.Question)
        button = reminder.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
            self.displayHomePage()
        else:
            print("No!")

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
        self.productSpinBox4.hide()
        self.universalTextEdit.hide()
        self.universalConfirmButton.hide()
        self.universalCancelButton.hide()
        self.productView2.hide()
        self.productTitle3.hide()
        self.productLabel3.hide()
        self.productView3.hide()
        self.productPrice3.hide()
        self.productTitle4.hide()
        self.productView4.hide()
        self.productPrice4.hide()
        self.productLabel4.hide()
        self.orderSummaryLabelgroupBox.hide()
    
    def hideMainMenus(self):
        self.label2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()


    def setOrderPage(self): #MainMenue page
        self.hideOrders()
        self.hideMainMenus()
        self.adminBackButton.hide()
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
        self.clearInputs()
        self.orderPushButton1.clicked.connect(self.setProduct1)
        self.orderPushButton2.clicked.connect(self.setProduct2)
        self.orderPushButton3.clicked.connect(self.setProduct3)
        self.orderPushButton4.clicked.connect(self.setProduct4)
        

        #Order Summary
        self.orderSummaryLabel.hide()
        self.orderSummaryLabelgroupBox.hide()
        self.textEdit.hide()
        self.orderConfirmation.hide()
        self.instructionLabel.hide()
        self.totalLabel.hide()

    def clearInputs(self):  # Clear Total and Amount fields 
        self.universalTextEdit.clear()
        self.productSpinBox1.clear()
        self.productSpinBox2.clear()
        self.productSpinBox3.clear()
        self.productSpinBox4.clear()
        self.textEdit.clear()

    def setProduct1(self): # UI_2.Product1
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
        self.productTitle1.show()
        self.productView1.show()
        self.productLabel1.show()
        self.productPrice1.show()
        self.productView1.show()
        self.productSpinBox1.show()
        self.showUniversalGroupBox()
        self.pushButton_2.hide()
          
    def setProduct2(self): # UI_2.Product2
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
        self.productTitle2.show()
        self.productView2.show()
        self.productLabel2.show()
        self.productPrice2.show()
        self.productSpinBox2.show()
        self.showUniversalGroupBox()
        self.pushButton_2.hide()
  
    def setProduct3(self): # UI_2.Product3
        self.productTitle3.show()
        self.productView3.show()
        self.productLabel3.show()
        self.productPrice3.show()
        self.productSpinBox3.show()
        self.showUniversalGroupBox()
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
        self.pushButton_2.hide()
        
    def setProduct4(self): # UI_2.Product4
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
        self.productTitle4.show()
        self.productView4.show()
        self.productLabel4.show()
        self.productPrice4.show()
        self.productSpinBox4.show()
        self.showUniversalGroupBox()
        self.pushButton_2.hide()

    def setOrderSummary(self):
        self.hideOrders()
        self.orderSummaryLabel.show()
        self.orderSummaryLabelgroupBox.show()
        self.textEdit.show()
        self.orderConfirmation.show()
        self.instructionLabel.show()
        self.backPushButton.show()
        self.totalLabel.show()
        self.pushButton_2.hide()

    def showUniversalGroupBox(self):
        self.universalGroupBox.show()
        self.universalTextEdit.show()
        self.universalConfirmButton.show()
        self.universalCancelButton.show()  

    def setAdminLandingPage(self):
        self.label2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.adminUserNameTextEdit.show()
        self.adminPasswrodTextEdit2.show()
        self.adminUserNameLabel.show()
        self.adminPasswordLabel2.show()
        self.adminLogoLabel.show()
        self.adminTitleLabel.show()
        self.adminBackButton.show()
        self.adminCreateNewAccount.show()
        
    # def productRiceLabel(self):
    #     #self.
    #     ricename = "Dinorado"
    #     updateRiceName = str(ricename)
    #     return updateRiceName
        




        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())