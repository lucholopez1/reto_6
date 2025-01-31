class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        # Validar que el valor sea un número
        if not isinstance(value, (int, float)):
            raise ValueError("El valor de x debe ser un número")
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        # Validar que el valor sea un número
        if not isinstance(value, (int, float)):
            raise ValueError("El valor de y debe ser un número")
        self._y = value

    def compute_distance(self, point):
        # Validar que el argumento sea una instancia de la clase Point
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de la clase Point")
        return ((self._x - point.get_x()) ** 2 + (self._y - point.get_y()) ** 2) ** 0.5