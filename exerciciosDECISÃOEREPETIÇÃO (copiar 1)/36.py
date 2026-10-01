#Declarar 
N: int
i: int
fat: int
soma: float

#inicio 
N = int(input('Digite o valor de N: '))
soma = 1
fat = 1

for i in range(1, N+1 ):
    fat = fat * i
    soma = soma + (1 / fat)

#Saidas
print('O resultado da Serie é: ', soma)
