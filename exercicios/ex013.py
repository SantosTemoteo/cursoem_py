nome = str(input('Nome do funcionário: '))
salario = float(input('Valor Salarial R$:'))
print('Reajuste Salarial de 15% para o funcionário:\n {}'.format(nome))
print('Novo Salário = R$:{:.2f}'.format(salario+(salario*15)/100))