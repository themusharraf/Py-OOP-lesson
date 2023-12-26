from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

    def draw(self):
        print("Drawing a Circle")


class Triangle(Shape):

    def __init__(self):
        super().__init__("triangle")

    def draw(self):
        print("Drawing a Triangle")


# create a circle object
circle = Circle()
circle.draw()

# create a triangle object
triangle = Triangle()
triangle.draw()