try:
    archivo = open("prueba.txt","w")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    archivo.close()
    #Despues de close ya no se puede usar el archivo
    #archivo.write("hola")
