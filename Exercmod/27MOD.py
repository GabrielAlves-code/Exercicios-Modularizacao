#Declaração
voltas: int
tamanho: float
tempo: float
distancia: float
tempohrs: float
velocidade: float

def main():
    global voltas
    global tamanho
    global tempo
    voltas = int(input('Digite o Numero de Voltas: '))
    tamanho = float(input('Digite o tamanho do circuito em metros: '))
    tempo = float(input('Digite o tempo de duração da corrida em minutos; '))
if __name__ == '__main__':
    main()

def calcVM(voltas, tamanho, tempo):
    distancia = (voltas * tamanho) / 1000
    tempohrs = tempo / 60
    velocidade = distancia /tempohrs
    return velocidade
print('A velocidade média é: ', calcVM(voltas, tamanho, tempo), 'KM/h')