#Declarar variavel
Valor1: int 
Valor2: int 

def main():
    global Valor1
    global Valor2
    Valor1 = int(input('Declare o primeiro valor: '))
    Valor2 = int(input('Declare o segundo valor: '))
if __name__ == "__main__":
    main()
def saida():
    if Valor1 % Valor2 == 0:
        print('O primeiro valor é multiplo do segundo')
    elif Valor2 % Valor1 == 0:
        print('O segundo valor é multiplo do primeiro')
    else:
        print('O primeiro valor NÃO é multiplo do segundo, nem ao contrario')

saida()