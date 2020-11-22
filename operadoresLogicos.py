#a = int(input("Proporciona un entero: "))
a = 1
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a<= valorMaximo)
print(dentroRango)

if(dentroRango):
    print("dentro de rango")
else:
    print("fuera de rango")
    
    
vacaciones = True
diaDescanso = False
if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes")
    
print(not(vacaciones))
    