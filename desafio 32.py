ano = int(input('Qual é o ano? '))

if (ano%4)==0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))