dias = int(input('por quantos dias você ficou com o carro? '))
km = float(input('quilometros percorridos: '))
valor = (dias*60) + (km*0.15)
print('valor total a pagar: R$ {}'.format(valor))
