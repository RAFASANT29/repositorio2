try:
    archivo = open("prueba.txt","r")
    #print(archivo.read())
    #leer algunos caracteres
    #print(archivo.read(5))
    #print(archivo.read(3))
    #leer lineas completas 
    #print(archivo.readline())
    #print(archivo.readline())
    #for linea in archivo:
    #    print (linea)
    #leer lineas
    #print(archivo.readlines())
    #print(archivo.readlines()[2])
    #abrimos nuevo archivo
    #con a anexamos informacion a nuestro archivo
    #archivo2 = open ("copia.txt", "a")
    archivo2 = open ("copia.txt", "w")
    archivo2.write(archivo.read())
    
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()