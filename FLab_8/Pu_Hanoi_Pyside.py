from PySide.QtCore import *
from PySide.QtGui import *
from turtle import *


class Disk:
    def __init__(self,name = "Disk",x = 0,y = 0,h = 30,w = 150,c = "Black"):
        self.name = name
        self.xpos = x
        self.ypos = y
        self.h = h
        self.w = w
        self.color = c
        
    def showdisk(self,p):
        p.setPen(QColor(self.color))
        p.setBrush(QColor(self.color))
        p.drawRec(self.xpos,self.ypos,self.w,self.h)
        
    def newpos(self,x,y):
        self.xpos = x
        self.ypos = y
        
    def cleardisk(self,p):
        p.eraseRect(self.xpos,self.ypos,self.w,self.h)
       
