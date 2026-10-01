#declarar 
a: int = 0
b: int = 0
c: int = 0
Delta: int = 0
x1: float = 0
x2: float = 0 

#Inicio 
a = int(input("Defina o coeficiente a:"))
if a == 0:
    raise ValueError("o coeficiente a não pode ser 0 cara")
b = int(input("defina o coeficiente b:"))
c = int(input("defina o coeficiente c:"))
Delta = ((b * b ) - 4 * a * c)
if Delta < 0:
    raise ValueError("Delta não pode ser menor que zero")

#Coeficientes x1 e x2
import math
x1 = (- b + math.sqrt(Delta)) / (2 * a)
x2 = (- b - math.sqrt(Delta)) / (2 * a)

#SAIDA
print("O valor de x1 é:" + str(x1))
print("O valor de x2 é:" + str(x2))