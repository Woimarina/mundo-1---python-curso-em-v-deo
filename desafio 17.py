import math
co = float(input('qual o tamanho do cateto oposto? '))
ca = float(input('qual o tamanho do cateto adjascente? '))
hp = math.sqrt(co**2+ca**2)
print('o tamanho da hipotesusa é {:.2f}'.format(hp))
