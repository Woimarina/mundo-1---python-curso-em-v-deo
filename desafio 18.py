import math
num = int(input('diga um angulo em graus: '))
a = math.radians(num)
print('o cosseno de {} é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}'.format(num, math.cos(a), math.sin(a), math.tan(a)))
