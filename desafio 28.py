import random
a =  int(input('Escolha um número entre 0 e 5: '))
b = random.randint(0,5)

if a==b:
    print('Você adivinhou o número que eu escolhi, parabéns!!!')
else:
    print('Você errou meu número. Talvez na próxima...')