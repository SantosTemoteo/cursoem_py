nome = str(input('DIGITE UM NOME DE NOVO! : ')).strip().title()
lista = nome.split()
print('Seu nome tem silva? {}'.format('Silva' in lista)) # in é operador, não método !