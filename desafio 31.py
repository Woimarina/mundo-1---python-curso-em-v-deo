d = float(input('Qual distância, em quilometros, da viagem? '))
if d>200:
    print('o valor da passagem será R$ {:.2f}'.format(d*0.45))
else:
    print('o valor da passagem será R$ {:.2f}'.format(d*0.5))