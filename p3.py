from turtle import*
speed(0)

class Pole:
    def __init__(self,name,x,y):
        self.name = name
        self.top = 220
        self.height = 200
        self.thick = 20
        self.x = x
        self.y = y
        self.color = 'red'
        self.stack = []
    def showpole(self):
        penup()
        goto(self.x,self.y)
        pendown()

        color(self.color)
        begin_fill()
        fd(self.thick/2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.thick)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.thick/2+1)
        end_fill()
       
        
    def pushdisk(self,d):
        #d.cleardisk()
        d.newpos(self.x,self.top)
        
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
        color(self.color)
        begin_fill()
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
        end_fill()
    def newpos(self,x,y):
        penup()
        goto(x,y)
        pendown()
        self.xpos = x
        self.ypos = y
    def cleardisk(self):
        seth(0)
        penup()
        goto(self.xpos,self.ypos)
        pendown()
        pencolor('white')
        color('white')
        begin_fill()
        
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
        
        end_fill()

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