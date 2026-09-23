#declarar variaveis
valor1: int = 0
valor2: int = 0
valor3: int = 0
valor4: int = 0

def main():
    global valor1
    global valor2
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o Segundo valor: '))
if __name__ == "__main__":
    main()
def Saidas():
    if valor2 <= valor1:
        print(ValueError('Os valores devem estar em ordem crescente'))
    else: valor3 = int(input('digite o terceiro valor: '))
    

    if valor3 <= valor2:
        ValueError('OS VALORES DEVEM ESTAR EM ORDEM CRESCENTE!!!!!!!!!!')
    else:
        valor4 = int(input('digite o quarto valor: '))
        numeros = valor1, valor2, valor3, valor4
        print('os numeros ordenados são:' +str(sorted(numeros)))


Saidas()