valor = float(input('qual o valor do seu salário: '))
if valor > 1250:
    print('seu aumento será de 10% com o valor final de R$ {:.2f}'.format(valor*1.10))
else:
    print('seu aumento será de 15% com o valor final de {:.2f}'.format(valor*1.15))
