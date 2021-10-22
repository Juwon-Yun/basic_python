import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic

form_class = uic.loadUiType("mygui05.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.multiplicationTable)

    def multiplicationTable(self):
        dan = int(self.leDan.text())
        result = ""
        for i in range(1 ,20):
            result += str(dan) + " X " + str(i) + " = " + str(i*dan) + "\n"
            
        self.te.setText(result)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()