#Declarar 
valor1: int = 0
valor2: int = 0

def main():
    global valor1
    global valor2
    global numeros
    valor1 = int(input('Digite o primeiro valor aqui: '))
    valor2 = int(input('Digite o segundo valor aqui: '))
    numeros = valor1, valor2
if __name__ == "__main__":
    main()
    
def Saida():
    print(sorted(numeros))


Saida()