#Declarar
N1: int
N2: int
N: int
I: int
Divisores: int

#inicio
N1 = int(input('Digite o primeiro valor: '))
N2 = int(input('Digite o segundo Valor: '))

for N in range(N1, N2 + 1):
    Divisores = 0
    for i in range(1, N + 1):
        if N % i == 0:
            Divisores = Divisores + 1
    if Divisores == 2:
        print(N, "")

