import os
#Variaveis Globais
numero: int = 0
dir: str = ''
arq: str = ''

def grava(c, resultado):
    file: str = '' 
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    enc = 'utf-8'
    file = dir + '/' + arq
    linha = str(resultado) + '\n'
    
    if os.path.exists(dir) and os.path.isdir(dir):
        if os.path.exists(file) and os.path.isfile(file):
            tipo = 'w'

            if c > 0:
              tipo = "a"  

        else:
            tipo = "w"

        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha)
    
    


def mult(numero, tabuada):
    resultado: int = 0 
    resultado = tabuada * numero
    return resultado

def main():
    

    
    global valor, dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)
    numero = int(input('Digite o numero: '))
    if numero > 10:
        print('Não pode ser maior do que 10')
    else:
        for tabuada in range(1,11):  
            mult(numero, tabuada)
            grava(tabuada, mult(numero, tabuada)) 
if __name__ == '__main__':
    main()


