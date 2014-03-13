from PySide import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.view = View(self)
        self.button = QtGui.QPushButton("Clear")
        self.button.clicked.connect(self.Clear)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
        layout.addWidget(self.button)
    
    def Clear(self):
        self.view.Clear()

class View(QtGui.QGraphicsView):
    def __init__(self, parent):
        self.pressing = False
        self.scene = QtGui.QGraphicsScene()
        self.x = 0
        self.y = 0

        QtGui.QGraphicsView.__init__(self, parent)
        self.setScene(self.scene)
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))
    def Clear(self):
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)

    def mouseMoveEvent(self, event):
        if(self.pressing):
            rad = 1
            pos = self.mapToScene(event.pos())
            self.scene.addLine(self.x,self.y,pos.x()-rad,pos.y()-1, QtGui.QPen())
        self.x = pos.x()-rad
        self.y = pos.y()-rad

    def mousePressEvent(self, event):
        rad = 1
        self.pressing = True
        pos = self.mapToScene(event.pos())
        self.x = pos.x()-rad
        self.y = pos.y()-rad

    def mouseReleaseEvent(self, event):
        self.pressing = False

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())