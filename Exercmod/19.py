#declaração de variaveis
valor1: float = 0
valor2: float = 0

def main():
    global valor1
    global valor2
    global maiorvalor
    valor1 = float(input('declare o primeiro valor: '))
    valor2 = float(input('declare o segundo valor: '))
    maiorvalor = max(valor1, valor2)
if __name__ == "__main__":
    main()
def Saidas():
    
    if valor1 == valor2:
        print('Os Valores não podem ser iguais!!!!!!!!!!!')
    else:
        print('o maior entre esses dois valores é o valor: ' +str(maiorvalor))


Saidas()