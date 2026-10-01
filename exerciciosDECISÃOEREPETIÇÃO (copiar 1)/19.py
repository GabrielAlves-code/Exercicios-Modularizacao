#declaração de variaveis
valor1: float = 0
valor2: float = 0

#Inicio
valor1 = float(input('declare o primeiro valor: '))
valor2 = float(input('declare o segundo valor: '))
maiorvalor = max(valor1, valor2)

#Saidas
if valor1 == valor2:
    print('Os Valores não podem ser iguais!!!!!!!!!!!')
else:
    print('o maior entre esses dois valores é o valor: ' +str(maiorvalor))