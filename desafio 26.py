frase = input('escreva uma frase: ')
frase = frase.strip().lower()

print('a letra A aparece {} vezes\na primeira ves que aparece é na posição {}\ne a ultima vez na pósição {}'.format(frase.count('a'),(frase.find(a)+1),(frase.rfind('a')+1)))