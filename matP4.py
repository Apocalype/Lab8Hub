import sys
from PySide.QtGui import*
from PySide.QtCore import*

class Pole(QObject):
    def __init__(self,name,x,y):
        QObject.__init__(self,None)

        self.name = name
        self.top = 50
        self.height = 200
        self.thick = 20
        self.x = x
        self.y = y
        self.color = QColor('red')
        self.stack = []

    def showpole(self,p):

        p.setPen(self.color)
        p.setBrush(self.color)
        p.drawRect(self.x-self.thick/2,self.y,self.thick,self.height)


    def pushdisk(self,d):
        if(type(d)== type(Disk('eiei',0,0,10,10))):
            self.stack+=[d]
            
            d.newpos(self.x,400- self.y - (len(self.stack)*d.h))
      
        else:
            print('hielse')
        
    def popdisk(self):
        if(len(self.stack)!=0):
            disk = self.stack.pop()

            disk.newpos(self.x,self.top)
            return disk

class Disk(QObject):
    updateSignal = Signal()

    def __init__(self,name = "Disk",x = 0,y = 0,h = 30,w = 150,c = "Black"):
        QObject.__init__(self,None)
        
        self.name = name
        self.xpos = x
        self.ypos = y
        self.h = h
        self.w = w
        self.color = c
        
    def showdisk(self,p):
        p.setPen(QColor(self.color))
        p.setBrush(QColor(self.color))
        p.drawRect(self.xpos-self.w/2,self.ypos-self.h/2,self.w,self.h)
        
    def newpos(self,x,y):
        self.xpos = x
        self.ypos = y
        self.updateSignal.emit()
        self.thread().msleep(500)
        
    def cleardisk(self,p):
        
        p.eraseRect(self.xpos-self.w/2,self.ypos-self.h/2,self.w,self.h)


class Hanoi(QWidget):
    def __init__(self, n = 3, start = "A", workspace = "B", destination = "C"):
        QWidget.__init__(self,None)

        self.setGeometry(100,100,550,400)

        self.poleBox = [Pole(start,100,100), Pole(workspace,250,100),Pole(destination,400,100)]

        self.diskBox=[]
        for i in range(n):
            self.diskBox+=[Disk("d"+str(i),100,300- (i*20),20,(n-i)*30)]
            self.diskBox[len(self.diskBox)-1].updateSignal.connect(self.repaint)

        for each in self.diskBox:
            self.poleBox[0].pushdisk(each)

        self.repaint()

    
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        for eachPole in self.poleBox:
            eachPole.showpole(p)
        for eachDisk in self.diskBox:
            eachDisk.showdisk(p)
        p.end()
        self.update()

    def move_disk(self,start,destination):
        disk = start.popdisk()
        self.repaint()
        destination.pushdisk(disk)
        self.repaint()

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.poleBox[0],self.poleBox[2],self.poleBox[1])

def main():
    
    app = QApplication(sys.argv)
    ex = Hanoi()
    ex.show()
    ex.solve()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
