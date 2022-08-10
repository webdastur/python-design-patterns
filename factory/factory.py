from abc import ABC, abstractmethod
from typing import Union, Optional


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeFactory:
    @classmethod
    def get_shape(cls, shape_type: str) -> Union[Shape, None]:
        if not shape_type:
            return None
        if shape_type.upper() == "CIRCLE":
            return Circle()
        if shape_type.upper() == "RECTANGLE":
            return Rectangle()
        if shape_type.upper() == "SQUARE":
            return Square()
        return None


if __name__ == "__main__":
    shape_factory: ShapeFactory = ShapeFactory()

    # get an object of Circle and call its draw method.
    shape1: Optional[Circle] = shape_factory.get_shape("CIRCLE")

    # call draw method of Circle
    shape1.draw()

    # get an object of Rectangle and call its draw method.
    shape2: Optional[Rectangle] = shape_factory.get_shape("RECTANGLE")

    # call draw method of Rectangle
    shape2.draw()

    # get an object of Square and call its draw method.
    shape3: Optional[Square] = shape_factory.get_shape("SQUARE")

    # call draw method of Square
    shape3.draw()
