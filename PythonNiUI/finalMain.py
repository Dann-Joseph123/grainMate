import sys
from PySide6.QtWidgets import QApplication
from ui_thesisUI1 import Ui_MainWindow
app = QApplication(sys.argv)

window = Ui_MainWindow()
window.show()
app.exec_()

