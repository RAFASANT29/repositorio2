class Rectangulo:
    def __init__ (self, b, h):
        self.b = b
        self.h = h
    
    def area(self):
        return self.b * self.h
    
    def perimetro(self):
        return ((2*self.b) + (2*self.h))
    
#b = int(input("Proporciona la base: "))
#h = int(input("Proporciona la altura:"))
b = 2
h = 3
figura = Rectangulo(b,h)

print("El area es: ", figura.area())
print("El perimetro es: ",figura.perimetro())

