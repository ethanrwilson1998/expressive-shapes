import sys
from parameters import *
from shapes import Square, Circle, Triangle
from PyQt5 import QtWidgets
from app import App

if __name__ == "__main__":
    shapes = [Square(color='red', x=100, y=100, s=20),
              Circle(color='blue', x=300, s=50),
              Triangle(color='green', x=120, y=100, x2=100, y2=80, x3=150, y3=93)]

    app = QtWidgets.QApplication([])
    ex = App(shapes, canvas_width, canvas_height, frame_rate)

    sys.exit(app.exec_())
