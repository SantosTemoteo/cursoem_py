'''
tempo = int(input('Quantos anos tem seu carro? ')) # condição simples
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('fim')

'''
'''
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'carro velho')
print('--Fim--')

'''
'''
n1 = float(input('Nota1 ')) # condição composta
n2 = float(input('Nota2 '))
m = (n1+n2)/2
if m >= 6.0:
    print('Aprovado!')
else:
    print('Reprovado!')

'''
n1 = float(input('Nota1 ')) # condição simplificada
n2 = float(input('Nota2 '))
m = (n1+n2)/2
print('APROVADO!' if m >= 6 else 'REPROVADO!')

