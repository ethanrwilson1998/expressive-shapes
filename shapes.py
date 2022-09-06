from abc import abstractmethod


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
        self.direction = 1
        self.speed = 8
        ##########

    def move(self, shapes):
        # your movement code here, replace this sample code:
        if self.x < 0:
            self.direction = 1
        if self.x + self.w >= canvas_width:
            self.direction = -1

        self.x += self.speed * self.direction
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
        self.direction = 1
        self.speed = 5
        ##########

    def move(self, shapes):
        # your movement code here, replace this sample code:
        if self.y < 0:
            self.direction = 1
        if self.y + self.h >= canvas_height:
            self.direction = -1

        self.y += self.speed * self.direction
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

canvas_width = 600
canvas_height = 400
frame_rate = 30

# define what shapes you want in your scene HERE

shape_array = [Square(color='red', x=100, y=100, s=20),
               Circle(color='blue', x=300, s=50),
               Triangle(color='green', x=120, y=100, x2=100, y2=80, x3=150, y3=93)]
