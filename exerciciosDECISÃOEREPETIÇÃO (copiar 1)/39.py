#Declarar
Casa: int
grãos: float
total: float

#Inicio
grãos = 1
total = 0 

for casa in range(1, 65):
    total = total + grãos
    grãos = grãos * 2

print('A Quantidade total de grãos é: ', total)