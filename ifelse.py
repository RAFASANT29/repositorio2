condicion = False

print("Condicion verdadera") if condicion else print("Condicion falsa")
if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("La condicion es falsa")
else:
    print("Condicion no reconocida")
    
numero = int(input("Proporciona un entero (1-3): "))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Fuera de rango"
    
    
print(numeroTexto)