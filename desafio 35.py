a = float(input("comprimento do primeiro lado: "))
b = float(input('comprimento do segundo lado: '))
c = float(input('comprimento do terceiro lado: '))

if a > b:
    maior = a
    menor = b
    if c < maior:
        medio = menor
        menor = c
    if c < menor:
        medio = maior
        maior = c
else:
    maior = b
    menor = a
    if c > maior:
        medio = maior
        maior = c
    if c < menor:
        medio = menor
        menor = c

if (medio + menor) >= maior:
    print('suas retas podem formar um triângulo.')
else:
    print('suas retas não podem formar um triângulo.')
