velocidade = float(input('qual a velocidade do carro? '))

if (velocidade>80):
    multa = (velocidade - 80.0) *7.0
    print(' iih! vc tá acima da velocidade! Sua multa é de R$ {:.2f}'.format(multa))
else:
    print('Tá otima a velocidade! Continue assim!')