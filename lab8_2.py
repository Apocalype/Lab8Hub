
import sys
from PySide.QtCore import *
from PySide.QtGui import *

            
class DrawingArea(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self, parent)

        #self.setAcceptDrops(True)

    def mousePressEvent(self, e):
        print('hi')
        
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        for eachPicture in self.pictureBox:
            p.drawImage(QRect(eachPicture.position.x(),eachPicture.position.y()\
                ,eachPicture.width,eachPicture.height),eachPicture.image)
        p.end()

    
    def clear(self):
        p = QPainter()
        p.begin(self)
        p.setBrush(QColor(255,255,255))

        p.drawRect(0,0,self.width(),self.height())

        p.end()
        self.update()

class PictureBoxApp(QWidget):
  
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle('Paint')

        self.pictureArea = DrawingArea(self)

        layout = QVBoxLayout()
        layout.addWidget(self.pictureArea)

        self.clearBt = QPushButton("clear")
        self.clearBt.clicked.connect(self.clear)
        layout.addWidget(self.clearBt)

        self.setLayout(layout)
        self.setMinimumSize(330, 400)

 
              


class Simple_paint_program(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Painting")

    def mousePressedEvent(self, e):
        if event.button() == QtCore.Qt.LeftButton:
            try:
                p = QPainter()
                p.begin(self)

                p.setPen(QColor(0,0,0))
                p.setBrush(QColor(0,0,0))
                p.drawPoint([e.pos()])
       
                p.end()
            except:
                pass
            self.update()
        print('dragging')


def main():
    
    app = QApplication(sys.argv)
    ex = Simple_paint_program()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()