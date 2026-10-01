#Declaração de variaveis
valor1: int = 0
valor2: int = 0
calculo: int = 0

#INICIO
valor1 = int(input('Declare aqui o primeiro valor: '))
valor2 = int(input('Declare aqui o segundo valor: '))
calculo = valor1 - valor2
#Saidas 
if valor1 == valor2: 
    print('NÃO EXISTE DIFERENÇA ENTRE OS DOIS VALORES.')
else:
    print(calculo)


