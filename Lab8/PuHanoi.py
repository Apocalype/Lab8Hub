import sys
from PySide.QtCore import *
from PySide.QtGui import *
from turtle import *

class Pole:
    def __init__(self,name = "Pole", x = 0, y = 0, h = 100, w = 30, c = "Black"):
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = c
        pencolor(self.color)
    
    def showPole(self):
        penup()
        goto(self.x,self.y)
        pendown()
        self.fd(self.w)
        self.lt(90)
        self.fd(self.h)
        self.lt(90)
        self.fd(self.w)
        self.lt(90)
        self.fd(self.h)
        self.lt(90)
        self.penup()



class Disk:
    def __init__(self,name = "Disk",x = 0,y = 0,h = 30,w = 150,c = "Black"):
        self.name = name
        self.xpos = x
        self.ypos = y
        self.h = h
        self.w = w
        self.color = c
        pencolor(self.color)
    def showdisk(self):
        penup()
        goto(self.xpos,self.ypos)
        pendown()
        fd(self.w/2)
        lt(90)
        fd(self.h)
        lt(90)
        fd(self.w)
        lt(90)
        fd(self.h)
        lt(90)
        fd(self.w/2)
        seth(0)
    def newpos(self,x,y):
        penup()
        goto(x,y)
        pendown()
        self.xpos = x
        self.ypos = y
    def cleardisk(self):
        seth(0)
        pencolor('white')
        fd(self.w/2)
        lt(90)
        fd(self.h)
        lt(90)
        fd(self.w)
        lt(90)
        fd(self.h)
        lt(90)
        fd(self.w/2)
        pencolor(self.color)
        seth(0)



class Hanoi(object):
    def __init__(self, n = 3, start = "A", workspace = "B", destination = "C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)

h = Hanoi()
h.solve()





# test run of Disk class
'''
d = Disk()
d.showdisk()
d.cleardisk()
d.newpos(50,50)
d.showdisk()

'''
