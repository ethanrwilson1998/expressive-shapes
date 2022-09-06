# SAMPLE FROM LIVE DEMO IN CLASS

# This sample file has some more complicated interactions, where
# squares move arbitrarily in 3 dimensions and circles
# endlessly chase the nearest square

from abc import abstractmethod

import numpy as np


class Shape:
    def __init__(self, x=0, y=0, color='black'):
        self.x = x
        self.y = y
        self.color = color

    def update_coords(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def move(self, shapes):
        pass


class Rectangle(Shape):
    def __init__(self, w=1, h=1, **kwargs):
        super().__init__(**kwargs)
        self.w = w
        self.h = h

        # your initialization code here, replace this sample code:
        self.x_dir = 1
        self.y_dir = 1
        self.speed = 8
        ##########

    def move(self, shapes):

        def rand_dir():
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-1, 1)
            return x, y

        if self.x < 0 or self.x + self.w >= canvas_width or self.y < 0 or self.y + self.h >= canvas_height:
            self.x_dir, self.y_dir = rand_dir()
        if self.x < 0 and self.x_dir < 0:
            self.x_dir *= -1
        if self.x + self.w >= canvas_width and self.x_dir > 0:
            self.x_dir *= -1
        if self.y < 0 and self.y_dir < 0:
            self.y_dir *= -1
        if self.y + self.h >= canvas_height and self.y_dir > 0:
            self.y_dir *= -1

        norm_term = np.sqrt(np.square(self.x_dir) + np.square(self.y_dir))

        self.x_dir /= norm_term
        self.y_dir /= norm_term

        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        ##########


class Square(Rectangle):
    def __init__(self, s=None, **kwargs):
        super().__init__(**kwargs)
        # NOTE: Square uses s only for a simpler initialization.
        # Changing self.s in move method will not update its size
        if s is not None:
            self.w = s
            self.h = s
        if self.w != self.h:
            raise Exception(f'Invalid square object, s={s} w={self.w} h={self.h}.  w and h must be equal.')

    def move(self, shapes):
        # update if you want to give squares specialized behaviors relative to rectangles:
        super().move(shapes)
        ##########


class Ellipse(Shape):
    def __init__(self, w=1, h=1, **kwargs):
        super().__init__(**kwargs)
        self.w = w
        self.h = h

        # your initialization code here, replace this sample code:
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 5
        ##########

    def move(self, shapes):
        target_x, target_y = 0, 0
        x_off, y_off = 999, 999
        for shape in shapes:
            if type(shape) is Square:

                target_x = shape.x
                target_y = shape.y

                if (self.x - target_x) < x_off or (self.y - target_y) < y_off:
                    x_off = self.x - target_x
                    y_off = self.y - target_y
        norm_term = np.sqrt(np.square(x_off) + np.square(y_off))

        self.x_dir = -x_off / norm_term
        self.y_dir = -y_off / norm_term

        self.x_dir += np.random.uniform(-1, 1)
        self.y_dir += np.random.uniform(-1, 1)

        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        ##########


class Circle(Ellipse):
    def __init__(self, s=None, **kwargs):
        super().__init__(**kwargs)
        # NOTE: Circle uses s only for a simpler initialization.
        # Changing self.s in move method will not update its size
        if s is not None:
            self.w = s
            self.h = s
        if self.w != self.h:
            raise Exception(f'Invalid circle object, s={s} w={self.w} h={self.h}.  w and h must be equal.')

    def move(self, shapes):
        # update if you want to give circles specialized behaviors relative to ellipses:
        super().move(shapes)
        ##########


class Triangle(Shape):
    def __init__(self, x2=1, y2=1, x3=1, y3=1, **kwargs):
        super().__init__(**kwargs)
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

        # your initialization code here, replace this sample code:
        self.frame_count = 0
        self.tick = 2 * frame_rate
        self.direction = 0
        self.move_scale = 3
        ##########

    def move(self, shapes):
        # your movement code here, replace this sample code:

        # toggle direction every half second
        if self.frame_count >= self.tick:
            self.frame_count = 0
            self.direction += 1
            self.direction %= 4

        # determine direction
        x_off, y_off = 0, 0
        if self.direction == 0:
            x_off += self.move_scale
        if self.direction == 1:
            y_off += self.move_scale
        if self.direction == 2:
            x_off -= self.move_scale
        if self.direction == 3:
            y_off -= self.move_scale

        # move all points
        self.x += x_off
        self.x2 += x_off
        self.x3 += x_off
        self.y += y_off
        self.y2 += y_off
        self.y3 += y_off

        self.frame_count += 1
        ##########


# define canvas size HERE

canvas_width = 1200
canvas_height = 800
frame_rate = 30

# define what shapes you want in your scene HERE

shape_array = [Square(color='red', x=100, y=100, s=30),
               Square(color='green', x=800, y=600, s=20),
               Circle(color='blue', x=1000, s=80),
               Circle(color='blue', x=400, y=600, s=80),
               Circle(color='blue', x=60, y=700, s=80), ]

shape_array[1].speed *= .9
shape_array[2].speed *= 1.2
shape_array[3].speed *= 0.5
