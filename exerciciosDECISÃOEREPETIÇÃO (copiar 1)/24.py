#Declarar 
valor1: int = 0

#INICIO
valor1 = int(input('Digite o valor que deseja: '))

#saidas
if valor1 % 2 == 0 and valor1 % 3  == 0:
    print('o Valor é divisivel por 2 e 3')

elif valor1 % 2 == 0:
    print('o valor é divisivel por 2, mas não por 3')

elif valor1 % 3 == 0:
    print('o valor é divisivel por 3, mas não por 2')

else:
    print('O valor não é divisivel por 2 nem por 3')