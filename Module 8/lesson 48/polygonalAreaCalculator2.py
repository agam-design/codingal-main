from abc import ABC, abstractmethod

class Polygon(ABC):
    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, length, width):
        self._length = length    
        self._width = width

    def area(self):
        return self._length * self._width


class Square(Polygon):
    def __init__(self, side):
        self._side = side        

    def area(self):
        return self._side * self._side


class Triangle(Polygon):
    def __init__(self, base, height):
        self._base = base        
        self._height = height

    def area(self):
        return 0.5 * self._base * self._height


if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Square(4),
        Triangle(6, 8)
    ]

    for shape in shapes:
        print("Area:", shape.area())
