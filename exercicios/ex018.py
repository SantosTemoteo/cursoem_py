from math import radians, sin, cos, tan
n = float(input('Digite um ângulo qualquer: '))
print('Seno de {} = {:.2f}'.format(n, sin(radians(n))))
print('Cosseno de {} = {:.2f}'.format(n, cos(radians(n))))
print('Tangente de {} = {:.2f}'.format(n, tan(radians(n))))