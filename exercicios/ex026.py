frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #gambi
print('A ultima letra apareceu na posição {}'.format(frase.rfind('A')+1))

