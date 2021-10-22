# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic, QtGui

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.state = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        else :
            self.state = 0
        
        self.pb.setIcon(QtGui.QIcon("{}.png".format(self.state)))

            
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