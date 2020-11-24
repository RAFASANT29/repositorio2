
from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return FiguraGeometrica.get_alto(self) * FiguraGeometrica.get_ancho(self)
        
    def __str__ (self):
        return FiguraGeometrica.__str__(self) + Color.__str__(self)
    
    