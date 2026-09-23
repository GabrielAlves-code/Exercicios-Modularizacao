#Declarar
numero: float
maior: float
menor: float
i: int

#INICIO
for i in range (1, 101):
    numero = float(input('Digite um numero Positivo: '))
    if i == 1:
        maior = numero
        menor = numero 
else:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

#Saidas

print('Maior Valor: ', maior)
print('Menor valor: ', menor)
