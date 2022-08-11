from abc import ABC, abstractmethod


class DrawAPI(ABC):
    def draw_circle(self, radius: int, x: int, y: int):
        pass


class RedCircle(DrawAPI):
    def draw_circle(self, radius: int, x: int, y: int):
        print(f"Drawing Circle[ color: red, radius: {radius}, x: {x}, {y}]")


class GreenCircle(DrawAPI):
    def draw_circle(self, radius: int, x: int, y: int):
        print(f"Drawing Circle[ color: green, radius: {radius}, x: {x}, {y}]")


class Shape:
    draw_api: DrawAPI

    def __init__(self, draw_api: DrawAPI):
        self.draw_api = draw_api

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    _x: int
    _y: int
    _radius: int

    def __init__(
        self,
        x: int,
        y: int,
        radius: int,
        draw_api: DrawAPI,
    ):
        super(Circle, self).__init__(draw_api)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        self.draw_api.draw_circle(
            self._radius,
            self._x,
            self._y,
        )


if __name__ == "__main__":
    red_circle: Circle = Circle(100, 100, 10, RedCircle())
    green_circle: Circle = Circle(100, 100, 10, GreenCircle())

    red_circle.draw()
    green_circle.draw()
