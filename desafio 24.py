cidade = input('digite o nome da cidade: ')
cidade = cidade.lower().strip().split()

print('o nome dessa cidade começa com santo? {}'.format('santo' in cidade[0]))