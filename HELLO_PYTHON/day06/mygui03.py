import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic

form_class = uic.loadUiType("mygui03.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
            
    def myClick(self):
        a = int(self.leA.text())
        b = int(self.leB.text())
        self.leC.setText(str(a*b))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()