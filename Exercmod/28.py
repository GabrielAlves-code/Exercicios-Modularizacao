#declarar
preçoatual: float = 0
vendamensal: float = 0
acrnovopreço: float = 0

#inicio
vendamensal = float(input('insira a venda media mensal do produto: '))
preçoatual = float(input('insira o preço atual de um produto: '))

if vendamensal <500 and preçoatual <30.00:
    acrnovopreço = preçoatual + (preçoatual * 0.10)

elif 500 <= vendamensal < 1000 and 30.00 <= preçoatual < 80.00:
    acrnovopreço = preçoatual + (preçoatual* 0.15)

elif vendamensal >= 1000 and preçoatual >= 80.00:
    acrnovopreço = preçoatual - (preçoatual * 0.05)

else:
    acrnovopreço = preçoatual

#Saida 
print('o novo preço do produto é: '  +str(acrnovopreço))

    
    