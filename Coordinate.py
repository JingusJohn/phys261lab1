
class Coordinate:
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y

    def get_slope(self, other, reverse: bool = False):
        if not reverse:

            dy = self.y - other.y
            dx = self.x - other.x
            return dy / dx
        else:
            dy = other.y - self.y
            dx = other.x - self.x
            return dy / dx

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    # getters and setters for x and y values
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
