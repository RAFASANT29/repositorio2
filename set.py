#set es una coleccion sin orden y sin indices, no permite elemento repetidos
# y lo elementos no se puedesn modificar, pero si agreagr nuevos o eliminar
planetas = {"Marte" , "Jupiter", "Venus"}
print(planetas)
#largo
print(len(planetas))
#Revisar si un elemento esta presente
print("Tierra" in planetas)
#agregar elementos
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")#No se pueden agregar elementos duplicados
print(planetas)
#eliminar
planetas.remove("Tierra")
print(planetas)
#eliminar con discard no arroja excepeción
planetas.discard("Jupiters")
print(planetas)
#limpiar el ser
planetas.clear()
print(planetas)
#eliminar el set
del planetas
#print(planetas)