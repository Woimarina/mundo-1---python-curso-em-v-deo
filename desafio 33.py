a = int(input('primeiro número: '))
b = int(input('segundo número:'))
c = int(input('terceiro número:'))

if a>b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

if maior>c:
    if c< menor:
        menor = c
        
if c > maior:
    maior = c

print(' {} é o maior número e {} e é o menor'.format(maior, menor))