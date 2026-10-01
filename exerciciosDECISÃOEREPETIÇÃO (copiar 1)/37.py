#Declarar
N: int
i: int
a: int
b: int
Fib: int

#Inicio 
N = int(input('Digite até onde ira a sequencia: '))
a = 0
b = 1

for i in range (1, N+1) :
    print(a, "")
    Fib = a + b
    a = b
    b = Fib


