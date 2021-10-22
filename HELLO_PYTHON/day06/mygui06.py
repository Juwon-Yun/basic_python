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
        if a in "����" :
            aa = 1
        elif a in "����":
            aa = 2
        elif a in "��":
            aa = 3
        
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.leB.setText("����")
        elif rnd == 2:
            self.leB.setText("����")
        elif rnd == 3:
            self.leB.setText("��")
        
        if aa == rnd:
            self.leC.setText("���� �����ϴ�")
        elif (aa == 1 and rnd == 3) or (aa == 2 and rnd == 1) or (aa == 3 and rnd == 2):
            self.leC.setText("���� �̰���ϴ�.")
        else :
            self.leC.setText("���� �����ϴ�.")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()