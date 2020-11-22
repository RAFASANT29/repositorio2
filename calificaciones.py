n = float (input("Proporciona un valor entre 0 y 10: "))
cal = None
if n <= 10 and n >= 9:
    cal = 'A'
elif n >= 8 and n < 9:
    cal = 'B'
elif n >= 7 and n < 8:
    cal = 'C'
elif n >= 6 and n < 7:
    cal = 'D'
elif n >= 0 and n < 6:
    cal = 'F'
else : 
    cal = "Valor desconocido"
    
print(cal)
    
     