import random
n_user = int(input('Escolha um número entre 0 e 5: '))
n_pc = random.randint(0, 5)
print('!ACERTOU! :D' if n_user == n_pc else 'Errou :(')
