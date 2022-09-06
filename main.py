import sys
from shapes import Square, Circle, Triangle, canvas_width, canvas_height, frame_rate, shape_array
from PyQt5 import QtWidgets
from app import App

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    ex = App(shape_array, canvas_width, canvas_height, frame_rate)

    sys.exit(app.exec_())
