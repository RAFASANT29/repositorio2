class Persona:
    def __init__ (this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.d = d
    
    def desplegar (this):
        print("Nombre: ", this.nombre)
        print("Edad: ", this.edad)   
        print("Valores (Tupla):", this.valores)
        print("Diccionario: ", this.d)
         
p1 = Persona("Juan", 28)
p1.desplegar()
print(p1.nombre)
print(p1.edad)

p2 = Persona("Karla", 30, 2,4,5)
p2.desplegar()

p3 = Persona("HJOla", 20, 2,4,7, m="Manzana", p= "pera", j="Jicama")
p3.desplegar()