import random

aluno1 = input('digite o nome do primeiro aluno: ')
aluno2 = input('digite o nome do segundo aluno: ')
aluno3 = input('digite o nome do terceiro aluno: ')
aluno4 = input('digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(' a sequencia de apresentação será: {}'.format(lista))

