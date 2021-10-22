# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic
from PyQt5.uic.Compiler.qtproxies import QtWidgets

form_class = uic.loadUiType("mygui09.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbCall.clicked.connect(self.myCall)
        self.pb1.clicked.connect(lambda:self.showTF(1))
        self.pb2.clicked.connect(lambda:self.showTF(2))
        self.pb3.clicked.connect(lambda:self.showTF(3))
        self.pb4.clicked.connect(lambda:self.showTF(4))
        self.pb5.clicked.connect(lambda:self.showTF(5))
        self.pb6.clicked.connect(lambda:self.showTF(6))
        self.pb7.clicked.connect(lambda:self.showTF(7))
        self.pb8.clicked.connect(lambda:self.showTF(8))
        self.pb9.clicked.connect(lambda:self.showTF(9))
        self.pb0.clicked.connect(lambda:self.showTF(0))
        
        
    def showTF(self, num):
        str_new = str(num)
        str_old = self.le.text()    #str_new = self.sender().text() <--���ٸ� �Ƚᵵ��
        txt = str_old + str_new
        self.le.setText(txt)
    
    def myCall(self):
        #QtWidgets.QMessageBox.about(self,"Calling...",pbCall)
        QMessageBox.question(self, 'message', 'Are you sure about '+self.le.text()+' calling?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()