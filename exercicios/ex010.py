#conversor de moedas
n = float(input('Digite um valor em Reais R$:'))
print('Considerando a cotação atual (05/08/2021) USD$: 1 = R$: 5.25 ...')
print('Com {:.2f} Reais, você tem {:.2f} Dorales!'.format(n, n/5.25))
