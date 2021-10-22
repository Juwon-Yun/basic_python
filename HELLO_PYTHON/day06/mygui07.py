import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic
import random

form_class = uic.loadUiType("mygui07.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qb.clicked.connect(self.myClick)

    def myClick(self):
        arr = [1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45]
        n = 0
        while n < 100:
            rnd = random.randint(1,44)
            a = arr[0]
            b = arr[rnd]
            arr[rnd] = a
            arr[0] = b
            n += 1
            
        self.lblA.setText(str(arr[0]))
        self.lblB.setText(str(arr[1]))
        self.lblC.setText(str(arr[2]))
        self.lblD.setText(str(arr[3]))
        self.lblE.setText(str(arr[4]))
        self.lblF.setText(str(arr[5]))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()