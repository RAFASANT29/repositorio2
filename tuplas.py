#Tupla mantiene el orden pero no se puede modificar (inmutable)
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

#Largo de la tupla
print(len(frutas))
#accediendo a un elemento
print(frutas[0])
#navigacion inversa
print(frutas[-1])
#rango
print(frutas[0:2])#no incluye el 2
#modificar un valor
#frutas[0] = "Naranjitas"
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
print(frutas)
#iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")
del frutas
#print(frutas)