import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic

form_class = uic.loadUiType("mygui02.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
            
    def myClick(self):
        a = str(int(self.le.text())+1)
        self.le.setText(a)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()