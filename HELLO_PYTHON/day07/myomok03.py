# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *  # @UnusedWildImport
from PyQt5 import uic, QtGui, QtCore, QtWidgets

form_class = uic.loadUiType("myomok03.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.state = 1
        self.stateOver = False
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,],
            [0,0,0,0,0, 0,0,0,0,0,]
                
        ]
        self.pb2d = []
        self.setupUi(self)
        
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton('',self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                btn.setToolTip("{},{}".format(i, j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2d.append(line)
        
        self.myrender()
        self.pb.clicked.connect(self.resetBoard)
    def myrender(self):
        #self.pb2d[0][0].setIcon(QtGui.QIcon("1.png"))
        #self.pb2d[9][9].setIcon(QtGui.QIcon("2.png"))
        for x in range(10):
            for y in range(10):
                if( self.arr2D[x][y] == 1 ):
                    self.pb2d[x][y].setIcon(QtGui.QIcon("1.png"))   
                elif( self.arr2D[x][y] == 2 ):
                    self.pb2d[x][y].setIcon(QtGui.QIcon("2.png"))
                else :
                    self.pb2d[x][y].setIcon(QtGui.QIcon("0.png"))
                   
        # self.btn = QPushButton(self)
        # self.btn.resize(40,40)
        # self.btn.setIcon(QtGui.QIcon("0.png"))
        # self.btn.setIconSize(QtCore.QSize(40,40))
        # self.btn.setGeometry(QtCore.QRect(100, 50, 40, 40))

    def myclick(self):
        if self.stateOver:
            return
        
        x = self.sender().toolTip().split(',')[0]
        y = self.sender().toolTip().split(',')[1]
        
        #self.arr2D[x][y]=1
        #self.myrender()
        
        if(self.state == 3):
            self.state = 1

        if self.arr2D[int(x)][int(y)] > 0:
            return
            
        stone = -1     
            
        if(self.state == 1):
            # ?????? ?????? ???????????? ??? ???????????????
                #self.pb2d[int(x)][int(y)].setIcon(QtGui.QIcon("1.png"))
                self.arr2D[int(x)][int(y)] = 1
                stone = 1
        elif(self.state == 2):
                #self.pb2d[int(x)][int(y)].setIcon(QtGui.QIcon("2.png"))
                self.arr2D[int(x)][int(y)] = 2
                stone = 2
        
        up = self.checkUP(int(x),int(y),stone)
        dw = self.checkDW(int(x),int(y),stone)
        ri = self.checkRI(int(x),int(y),stone)
        lf = self.checkLF(int(x),int(y),stone)
        
        #????????? ??????
        ur = self.checkUR(int(x),int(y),stone)
        #???????????? ??????
        dr = self.checkDR(int(x),int(y),stone)
        #?????? ??????
        ul = self.checkUL(int(x),int(y),stone)
        #????????? ??????
        dl = self.checkDL(int(x),int(y),stone)
        
        d1 = up + dw + 1
        d2 = ri + lf + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        #myrender ??????
        self.myrender()

        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.stateOver = True
            if self.state == 1:
                QtWidgets.QMessageBox.about(self,"omok","?????? ??????")
            elif self.state == 2:
                QtWidgets.QMessageBox.about(self,"omok","????????? ??????")
                
                
        self.state += 1
        
    def checkUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += -1
                #???????????? ????????? -1 ???????????? ?????????????????? 0 ?????? ????????? ??????
                if i < 0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else : 
                    return cnt
        except:
            return cnt
            
    def checkDW(self, i, j, stone):
        cnt = 0
        #i??? ????????? 9?????? ?????? ?????????????????? ????????? cnt ??????
        try:
            while True:
                i += 1

                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def checkRI(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1

                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def checkLF(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += -1

                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def checkUR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                i += -1
                
                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def checkDR(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                i += 1
                
                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def checkUL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += -1
                i += -1
                
                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def checkDL(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += -1
                i += 1
                
                if i < 0 :
                    return cnt

                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt

    def resetBoard(self):
        for x in range(10):
            for y in range(10):
                self.arr2D[x][y]= 0
        
        self.myrender()
  
        self.state = 1
        self.stateOver = False
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec()