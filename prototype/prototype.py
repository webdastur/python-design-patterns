import copy
from abc import ABC, abstractmethod
from typing import Dict, Any


class Shape(ABC):
    _id: str
    _type: str

    def __init__(self, t: str):
        self._type = t

    @abstractmethod
    def draw(self):
        pass

    def get_type(self) -> str:
        return self._type

    def get_id(self) -> str:
        return self._id

    def set_id(self, value: str):
        self._id = value

    def clone(self) -> Any:
        return copy.deepcopy(self)


class Rectangle(Shape):
    def __init__(self):
        super().__init__("Rectangle")

    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def __init__(self):
        super().__init__("Square")

    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def __init__(self):
        super().__init__("Circle")

    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeCache:
    shape_map: Dict[str, Shape] = dict()

    @staticmethod
    def get_shape(shape_id: str) -> Shape:
        return ShapeCache.shape_map.get(shape_id).clone()

    @staticmethod
    def load_cache():
        circle: Circle = Circle()
        circle.set_id("1")
        ShapeCache.shape_map[circle.get_id()] = circle

        square: Square = Square()
        square.set_id("2")
        ShapeCache.shape_map[square.get_id()] = square

        rectangle: Rectangle = Rectangle()
        rectangle.set_id("3")
        ShapeCache.shape_map[rectangle.get_id()] = rectangle


if __name__ == '__main__':
    ShapeCache.load_cache()

    cloned_shape: Shape = ShapeCache.get_shape("1")
    print(f"Shape : {cloned_shape.get_type()}")

    cloned_shape2: Shape = ShapeCache.get_shape("2")
    print(f"Shape : {cloned_shape2.get_type()}")

    cloned_shape3: Shape = ShapeCache.get_shape("3")
    print(f"Shape : {cloned_shape3.get_type()}")
