#Declaração
voltas: int
tamanho: float
tempo: float
distancia: float
tempohrs: float
velocidade: float

#inicio
voltas = int(input('Digite o Numero de Voltas: '))
tamanho = float(input('Digite o tamanho do circuito em metros: '))
tempo = float(input('Digite o tempo de duração da corrida em minutos; '))
distancia = (voltas * tamanho) / 1000
tempohrs = tempo / 60
velocidade = distancia /tempohrs

print('A velocidade média é: ', velocidade, 'KM/h')