class Caja:
    def __init__ (self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def volumen (self):
        return x*y*z
    
x = int(input("Proporciona el largo: "))
y = int(input("Proporciona el ancho: "))
z = int(input("Proporciona el alto: ")) 
box = Caja (x,y,z)
print("El volumen es: ", box.volumen())