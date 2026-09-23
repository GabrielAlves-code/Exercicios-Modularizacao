#Declarar
N: int
i: int
Fat: int

#inicio
N = int(input('Escreva o valor de N: '))
Fat = 1
for i in range(1, N + 1):
    Fat = Fat * i

print('Fatorial =', str(Fat))
    