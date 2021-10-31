nome = input('digite seu nome completo: ')
nome = nome.strip().split()
print('primeiro e ultimo nome: {} {}'.format(nome[0],nome[(len(nome)-1)]))