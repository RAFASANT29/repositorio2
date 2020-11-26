from cuadrado import Cuadrado
from rectangulo import Rectangulo
from figura_geometrica import FiguraGeometrica 

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado)

print(Cuadrado.mro())

rectangulo = Rectangulo(2, 4, "verde")
print(rectangulo.area())
print(rectangulo)

print(Rectangulo.mro())

#No es posible crear objetos de una clase abstracta
#figuraGeometrica = FiguraGeometrica()
