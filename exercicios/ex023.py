n = int(input('Informe um número: '))
print('Analizando o número {}'.format(n))
u = n // 1 % 10
d = n // 10 % 10 # não entendo kkkkj
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))