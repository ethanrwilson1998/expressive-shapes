import time

from PyQt5 import QtCore, QtWidgets, QtGui
import functools

from shapes import *


@functools.lru_cache()
class GlobalObject(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self._events = {}

    def add_event_listener(self, name, func):
        if name not in self._events:
            self._events[name] = [func]
        else:
            self._events[name].append(func)

    def dispatch_event(self, name):
        functions = self._events.get(name, [])
        for func in functions:
            QtCore.QTimer.singleShot(0, func)


class App(QtWidgets.QWidget):
    def __init__(self, in_shapes, width, height, frame_rate):
        super().__init__()

        self.shapes = in_shapes

        # parameters I could turn into args
        self.frame_rate = frame_rate
        self.width, self.height = width, height

        self.init_gui()
        # Register object as refreshable
        GlobalObject().add_event_listener('refresh', self.refresh)
        GlobalObject().dispatch_event('refresh')

    def init_gui(self):
        self.setWindowTitle('Expressive Shapes')
        self.canvas = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(self.width, self.height)
        pixmap.fill(QtGui.QColor('#dddddd'))
        self.canvas.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    def clear_canvas(self):
        pixmap = self.canvas.pixmap()
        pixmap.fill(QtGui.QColor('#dddddd'))

    def move_shapes(self):
        for shape in self.shapes:
            shape.move(self.shapes)

    def draw_shapes(self):
        for shape in self.shapes:
            if type(shape) is Rectangle or type(shape) is Square:
                self.draw_rectangle(shape)
            if type(shape) is Ellipse or type(shape) is Circle:
                self.draw_ellipse(shape)
            if type(shape) is Triangle:
                self.draw_triangle(shape)

    def draw_rectangle(self, rect):
        painter = self.create_brush(rect.color)
        # draw the rectangle
        painter.drawRect(rect.x, rect.y, rect.w, rect.h)
        painter.end()

    def draw_ellipse(self, elli):
        painter = self.create_brush(elli.color)
        # draw the ellipse
        painter.drawEllipse(elli.x, elli.y, elli.w, elli.h)
        painter.end()

    def draw_triangle(self, tri):
        painter = self.create_brush(tri.color)
        # draw the triangle
        points = [
            QtCore.QPoint(tri.x, tri.y),
            QtCore.QPoint(tri.x2, tri.y2),
            QtCore.QPoint(tri.x3, tri.y3),
        ]
        poly = QtGui.QPolygon(points)
        painter.drawPolygon(poly)
        painter.end()

    def create_brush(self, color):
        painter = QtGui.QPainter(self.canvas.pixmap())
        # outline
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(color))
        # fill brush
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(color))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        # assign to painter
        painter.setPen(pen)
        painter.setBrush(brush)
        return painter

    def refresh(self):
        # update shape information
        self.move_shapes()
        # refresh the canvas with new shape info
        self.clear_canvas()
        self.draw_shapes()
        # display in GUI
        self.update()
        self.show()
        # sleep according to frame rate then send another refresh signal
        time.sleep(1. / self.frame_rate)
        GlobalObject().dispatch_event('refresh')
