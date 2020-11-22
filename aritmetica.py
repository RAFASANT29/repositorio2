class Aritmetica:
    """Clase aritmetica para realizar operaciones"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 *  self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
    
#Creamos un objeto
aritmetica = Aritmetica(2,4)
print("Resultado de la suma: ", aritmetica.sumar())
print("Resultado de la suma: ", aritmetica.restar())
#Nuevo objeto
operaciones = Aritmetica(5,1)
print(operaciones.sumar())
print(operaciones.restar())
print(operaciones.multiplicar())
print(operaciones.dividir())
