#Declarar
Ana: float
Maria: float
Anos: int

Ana = 1.10
Maria = 1.50
Anos = 0

while Ana <= Maria:
    Ana = Ana + 0.03
    Maria = Maria + 0.02
    Anos = Anos + 1;

print('Serão necessarios: ', Anos, "Anos")
print('Altura de Ana: ', Ana,"M")
print('Altura de Maria: ', Maria,"M")
