print('------------------ Economisando tinta ------------------')
altura = float(input('Digite ALTURA da parede em metros: '))
largura = float(input('Digite a LARGURA da parede em metros: '))
area = altura*largura
print('Área a ser pintada = {} m²'.format(area))
print('{} litros necessários para pintar a parede.'.format(area*2))