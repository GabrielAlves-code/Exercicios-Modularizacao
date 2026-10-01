#Declarar
N: int
i: int
soma: float

#Inicio
N = int(input('digite o um numero: '))
soma = 0

for i in range (1, N+1):
    soma = soma + (1 / i);

print('Resultado da serie: ', soma)
