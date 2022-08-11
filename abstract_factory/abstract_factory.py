from abc import ABC, abstractmethod
from typing import Union, TypeVar, Optional

T = TypeVar("T", bound="AbstractFactory")


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class RoundedRectangle(Shape):
    def draw(self):
        print("Inside RoundedRectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class RoundedSquare(Shape):
    def draw(self):
        print("Inside RoundedSquare::draw() method.")


class AbstractFactory(ABC):
    @abstractmethod
    def get_shape(self, shape_type: str) -> Union[Shape, None]:
        pass


class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_type: str) -> Union[Shape, None]:
        if not shape_type:
            return None
        if shape_type.upper() == "RECTANGLE":
            return Rectangle()
        if shape_type.upper() == "SQUARE":
            return Square()
        return None


class RoundedShapeFactory(AbstractFactory):
    def get_shape(self, shape_type: str) -> Union[Shape, None]:
        if not shape_type:
            return None
        if shape_type.upper() == "RECTANGLE":
            return RoundedRectangle()
        if shape_type.upper() == "SQUARE":
            return RoundedSquare()
        return None


class FactoryProducer:
    @staticmethod
    def get_factory(rounded: bool) -> T:
        if rounded:
            return RoundedShapeFactory()
        return ShapeFactory()


if __name__ == "__main__":
    # get shape factory
    shape_factory: ShapeFactory = FactoryProducer.get_factory(False)

    # get an object of Shape Rectangle
    shape1: Optional[Rectangle] = shape_factory.get_shape("RECTANGLE")

    # call draw method of Shape Rectangle
    shape1.draw()

    # get an object of Shape Square
    shape2: Optional[Square] = shape_factory.get_shape("SQUARE")

    # call draw method of Shape Square
    shape2.draw()

    # get shape factory
    shape_factory1: RoundedShapeFactory = FactoryProducer.get_factory(True)

    # get an object of Shape Rectangle
    shape3: Optional[RoundedRectangle] = shape_factory1.get_shape("RECTANGLE")

    # call draw method of Shape Rectangle
    shape3.draw()

    # get an object of Shape Square
    shape4: Optional[RoundedSquare] = shape_factory1.get_shape("SQUARE")

    # call draw method of Shape Square
    shape4.draw()
