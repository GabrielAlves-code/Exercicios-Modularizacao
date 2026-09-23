#Declarar
n1: int
n2: int
maior: int
menor: int
soma: int
i: int

#inicio
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

soma = 0 

for i in range (menor, maior):
    if i % 2 != 0:
        soma = soma + i

#SAIDA
print('A soma dos numeros impares entre os valores é: ', soma)

