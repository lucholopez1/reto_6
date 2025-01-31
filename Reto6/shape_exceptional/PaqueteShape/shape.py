class Shape:
    def __init__(self, vertices):
        # Validación de entrada
        if not isinstance(vertices, list):
            raise TypeError("Los vértices deben ser proporcionados en una lista.")
        if len(vertices) < 3:
            raise ValueError("Un polígono debe tener al menos tres vértices.")
        if not all(isinstance(v, tuple) and len(v) == 2 for v in vertices):
            raise TypeError("Cada vértice debe ser una tupla de dos valores (x, y).")

        self._vertices = vertices
        self._edges = self.compute_edges()
        self._inner_angles = []
        self._is_regular = False

    def compute_edges(self):
        try:
            from .line import Line  # Importación diferida
        except ImportError as e:
            raise ImportError("No se pudo importar el módulo 'line'. Verifica su existencia.") from e

        edges = []
        try:
            for i in range(len(self._vertices)):
                start_point = self._vertices[i]
                end_point = self._vertices[(i + 1) % len(self._vertices)]
                edges.append(Line(start_point, end_point))
        except Exception as e:
            raise RuntimeError(f"Error al calcular los bordes: {e}") from e

        return edges
