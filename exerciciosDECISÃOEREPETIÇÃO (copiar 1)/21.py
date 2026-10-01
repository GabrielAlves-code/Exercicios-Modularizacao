#declarar variaveis
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0

#inicio
nota1 = float(input('digite a nota no primeiro bimestre: '))
nota2 = float(input('digite a nota no segundo bimestre: '))
nota3 = float(input('digite a nota no quarto bimestre: '))
nota4 = float(input('digite a nota do ultimo bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) /4

#Saidas
if media >= 6:
    print('o aluno foi aprovado.')
elif media >= 3:
    print('o aluno deve prestar um exame.')
else:
    print('ta reprovado')