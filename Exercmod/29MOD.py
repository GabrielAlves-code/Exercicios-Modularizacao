#Decalrar 
tipo: int
valorInvest: int

def main():
    global tipo
    global valorInvest
    tipo = int(input('digite o tipo de investimento: (1/poupança)ou(2/RendaFixa): '))
    valorInvest = int(input('digite o valor do investimento: '))
if __name__ == '__main__':
    main()

def Inves(tipo, valorInvest):
    if tipo == 1:
        resultado = valorInvest + (valorInvest * 0.03)
        print(('o valor do investimento em poupança rendeu em 30 dias: ' +str(resultado)))
    elif tipo ==2:
        resultado = valorInvest + (valorInvest * 0.05)
        print(('o valor do investimento em Renda Fixa rendeu em 30 dias: ' +str(resultado)))
    else:
        print('Não é um tipo de renda valido!!!!!!')
    return resultado
Inves(tipo, valorInvest)
