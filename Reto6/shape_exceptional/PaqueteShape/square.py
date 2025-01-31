from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        # Validar que el lado sea un número positivo
        if not isinstance(side, (int, float)):
            raise ValueError("El lado debe ser un número")
        if side <= 0:
            raise ValueError("El lado debe ser un valor positivo")

        super().__init__(side, side)

