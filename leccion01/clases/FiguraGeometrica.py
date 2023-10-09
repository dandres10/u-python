from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @abstractmethod
    def calcular_area(self):
        pass