# -*- coding: cp949 -*- 
import sys
import random
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic

form_class = uic.loadUiType("mygui06.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qb.clicked.connect(self.myClick)

    def myClick(self):
        a = self.leA.text()
        aa = 0
        if a in "가위" :
            aa = 1
        elif a in "바위":
            aa = 2
        elif a in "보":
            aa = 3
        
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.leB.setText("가위")
        elif rnd == 2:
            self.leB.setText("바위")
        elif rnd == 3:
            self.leB.setText("보")
        
        if aa == rnd:
            self.leC.setText("서로 비겼습니다")
        elif (aa == 1 and rnd == 3) or (aa == 2 and rnd == 1) or (aa == 3 and rnd == 2):
            self.leC.setText("내가 이겼습니다.")
        else :
            self.leC.setText("내가 졌습니다.")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()