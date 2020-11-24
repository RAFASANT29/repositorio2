from cuadrado import Cuadrado
from rectangulo import Rectangulo

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado)

print(Cuadrado.mro())

rectangulo = Rectangulo(2, 4, "verde")
print(rectangulo.area())
print(rectangulo)

print(Rectangulo.mro())