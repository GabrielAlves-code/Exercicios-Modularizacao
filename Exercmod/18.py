
#Declaração de variaveis
valor1: int = 0
valor2: int = 0
calculo: int = 0

def main():
    global valor1
    global valor2
    global calculo
    valor1 = int(input('Declare aqui o primeiro valor: '))
    valor2 = int(input('Declare aqui o segundo valor: '))
    calculo = valor1 - valor2
if __name__ == "__main__":
    main()
def SAIDA():
    global valor1
    global valor2
    if valor1 == valor2: 
        print('NÃO EXISTE DIFERENÇA ENTRE OS DOIS VALORES.')
    else:
        print(calculo)
#EXECUÇÃO

SAIDA()
