#declarar
horaINI: int
MINini: int
horafim: int
minFim: int
inicio: int
Fim: int
duração: int
horas: int
minutos:int

def main():
    global horaINI
    global MINini
    global horafim
    global minFim
    global inicio
    global fim
    horaINI = int(input('Digite a hora de inicio: '))
    MINini = int(input('Digite o minuto de inicio; '))
    horafim = int(input('Digite a hora do fim: '))
    minFim = int(input('Digite o minuto do fim:'))
    inicio = horaINI * 60 + MINini
    fim = horafim * 60 + minFim
if __name__ == "__main__":
    main()
def saidas():
    global horas
    global minutos
    if fim >= inicio:
        duração = fim - inicio
    else:
        duração = (24 * 60 - inicio) + fim
    horas = duração // 60
    minutos = duração % 60
    print('Tempo do jogo: ', horas, 'horas e ',minutos, 'Minutos...' )


saidas()
