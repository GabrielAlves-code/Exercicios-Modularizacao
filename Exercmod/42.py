#Declarar
i: int
termo: float
soma: float

#Inicio
soma = 0 
for i in range (1, 51):
    termo = i / (2 * i - 1)
    soma = soma + termo

print('Soma da serie: ', soma)