resultado = None
a = 10
b = 0
try:
    resultado = a/b
except Exception as e: 
    print("Ocurrió un error", e)
    print(type(e))

print("Resultado: ", resultado)
print("continuamos...")