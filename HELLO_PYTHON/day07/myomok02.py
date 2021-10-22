# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic, QtGui, QtCore

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        for i in range(10):
            for j in range(10):
                btn = QPushButton('',self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(i*40, j*40, 40, 40))
                
        # self.btn = QPushButton(self)
        # self.btn.resize(40,40)
        # self.btn.setIcon(QtGui.QIcon("0.png"))
        # self.btn.setIconSize(QtCore.QSize(40,40))
        # self.btn.setGeometry(QtCore.QRect(100, 50, 40, 40))

    def myclick(self):
        pass
    # self.printButton = QtGui.QPushButton(tab_name)
    # self.printButton.setIcon(QtGui.QIcon('icons/printer.tif'))
    # self.printButton.setIconSize(QtCore.QSize(130,130))
    # self.printButton.setGeometry(QtCore.QRect(1030, 500, 161, 61))
    #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()