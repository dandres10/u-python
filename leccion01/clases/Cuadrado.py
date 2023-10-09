from clases.Color import Color
from clases.FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho