#analizador de textos
nome = str(input('Nome completo: ')).strip()
print('Maiúsculo: {}'.format(nome.upper()))
print('minúsculo: {}'.format(nome.lower()))
div = nome.split()
print('Quantidade de carácteres: {}'.format(len(''.join(div))))
print('Quant. carac. da 1ª letra: {}'.format(len(div[0])))
