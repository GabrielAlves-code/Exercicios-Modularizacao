#DECLARAR  
i: int
soma: float

#inicio
soma = 0

for i in range(1, 16):
    if i % 2 == 0:
        soma = soma - (i / (i * i))
    else:
        soma = soma + (i / (i * i))

print('Resultado da Serie = ', soma)