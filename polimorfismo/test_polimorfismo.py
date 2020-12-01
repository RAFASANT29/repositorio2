from empleado import Empleado
from gerente import Gerente 

def imprimir_detalles(tipo_padre):
    print(tipo_padre)
    print(type(tipo_padre), end="\n\n")
    if isinstance(tipo_padre, Gerente):
        print(tipo_padre.departamento)
    
empleado = Empleado("Juan", 1000.00)
imprimir_detalles(empleado)

empleado = Gerente("Karla", 2000.00, "Sistemas")
imprimir_detalles(empleado)
