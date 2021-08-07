from random import shuffle
aluno1 = str(input('Aluno(a) 1: '))
aluno2 = str(input('Aluno(a) 2: '))
aluno3 = str(input('Aluno(a) 3: '))
aluno4 = str(input('Aluno(a) 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será:    \n {}'.format(lista))