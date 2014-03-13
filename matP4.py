import sys
from PySide.QtGui import*
from PySide.QtCore import*

class Pole(QObject):
    def __init__(self,name,x,y):
        QObject.__init__(self,None)

        self.name = name
        self.top = 220
        self.height = 200
        self.thick = 20
        self.x = x
        self.y = y
        self.color = QColor('red')
        self.stack = []

    def showpole(self,p):

        p.setPen(self.color)
        p.setBrush(self.color)
        p.drawRect(self.x,self.y,self.thick,self.height)


    def pushdisk(self,d):

        d.newpos(self.x,self.top)
        d.showdisk()
        
        d.cleardisk()
        d.newpos(self.x,self.y + (len(self.stack)*d.h))
        d.showdisk()
        
        self.stack+=[d]
        
    def popdisk(self):
        self.stack[len(self.stack)-1].cleardisk()
        
        disk = self.stack.pop()

        disk.cleardisk()
        disk.newpos(self.x,self.top)
        disk.showdisk()
        disk.cleardisk()
            
        return disk

class Hanoi(QWidget):
    def __init__(self, n = 3, start = "A", workspace = "B", destination = "C"):
        QWidget.__init__(self,None)

        self.setGeometry(100,100,550,400)

        self.poleBox = [Pole(start,100,100), Pole(workspace,250,100),Pole(destination,400,100)]

        self.repaint()

    
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        for eachPole in self.poleBox:
            eachPole.showpole(p)

        p.end()

    def move_disk(self,start,destination):
        desk = start.popdisk()
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

def main():
    
    app = QApplication(sys.argv)
    ex = Hanoi()
    ex.show()
    #ex.solve()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
