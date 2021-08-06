dias = int(input('Quantos dias alugados? '))
kmrodados = float(input('Quantos Km rodados? '))
taxadias = dias*60
taxakm = kmrodados*0.15
total = taxadias + taxakm
print('Total do aluguel a pagar = R$:{:.2f}'.format(total))