#Declarar 
valor1: int = 0
valor2: int = 0

#Inicio
valor1 = int(input('Digite o primeiro valor aqui: '))
valor2 = int(input('Digite o segundo valor aqui: '))
numeros = valor1, valor2
#Saida
print(sorted(numeros))